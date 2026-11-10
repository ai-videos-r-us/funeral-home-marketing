#!/usr/bin/env python3
"""UK adaptation, between the Gate 1 pull and Gate 2: keep only the listings inside one English
region and fill the columns the rest of the Blueprint expects (state, state_code, county).

DataForSEO's address_info.region holds what Google writes for a UK address (usually the nation,
such as "England"), never an English region such as "South West". So the pull is wide and this
script narrows it by postcode.

Two ways to decide whether a postcode is in the region, best first:
  1. --lookup (default): ask postcodes.io (free, no key, ONS data) for each postcode's official
     region, county and district. A row is kept when its ONS region equals --ons-region.
  2. Fallback, or --no-lookup: the postcode area list in AREAS below, minus the districts in
     EXCLUDE that sit in a neighbouring region. Rough at the edges; the report says which rule decided.

Usage:
  python3 scripts/uk_region_filter.py input/listings-raw.csv --out input/listings-raw-sw.csv
  python3 scripts/uk_region_filter.py input/listings-raw.csv --out input/listings-raw-sw.csv --no-lookup

Then Gate 2 runs on the output with `--state SW`.
"""
import argparse, csv, json, os, re, sys, time, urllib.request, urllib.error
from collections import Counter

# South West England by postcode area (fallback only). Districts that cross into the South East
# or elsewhere are listed in EXCLUDE. Verify edge cases with --lookup; this list is a safety net.
AREAS = {"BA", "BH", "BS", "DT", "EX", "GL", "PL", "SN", "SP", "TA", "TQ", "TR"}
EXCLUDE = {"BH24", "BH25", "SP6", "SP10", "SP11", "SN7"}   # Hampshire / Oxfordshire districts

PC_RX = re.compile(r"\b([A-Z]{1,2}\d[A-Z\d]?)\s*(\d[A-Z]{2})\b")
API = "https://api.postcodes.io/postcodes"


def norm_pc(raw):
    m = PC_RX.search((raw or "").upper())
    return f"{m.group(1)} {m.group(2)}" if m else ""


def outward(pc):
    return pc.split(" ")[0] if pc else ""


def area(pc):
    m = re.match(r"[A-Z]{1,2}", pc or "")
    return m.group(0) if m else ""


def lookup(postcodes):
    """postcodes.io bulk lookup, 100 at a time. Returns {postcode: result-or-None}."""
    out, todo = {}, sorted(set(p for p in postcodes if p))
    for i in range(0, len(todo), 100):
        chunk = todo[i:i + 100]
        body = json.dumps({"postcodes": chunk}).encode()
        for attempt in range(3):
            try:
                req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(req, timeout=60) as r:
                    data = json.loads(r.read().decode())
                break
            except (urllib.error.URLError, TimeoutError) as e:
                if attempt == 2:
                    raise SystemExit(f"postcodes.io unreachable ({e}). Rerun with --no-lookup to use the postcode-area fallback.")
                time.sleep(2 * (attempt + 1))
        for item in data.get("result") or []:
            out[item.get("query", "").upper()] = item.get("result")
        time.sleep(0.2)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("src")
    ap.add_argument("--out", required=True)
    ap.add_argument("--ons-region", default="South West", help='ONS region name as postcodes.io returns it')
    ap.add_argument("--state-name", default="South West England", help="written into the state column")
    ap.add_argument("--state-code", default="SW", help="written into state_code; pass the same to Gate 2 --state")
    ap.add_argument("--no-lookup", action="store_true", help="skip postcodes.io and use the postcode-area fallback")
    a = ap.parse_args()

    rows = list(csv.DictReader(open(a.src, newline="", encoding="utf-8")))
    if not rows:
        sys.exit("No rows in the source CSV.")
    fields = list(rows[0].keys())
    for f in ("state", "state_code", "county", "postal_code"):
        if f not in fields:
            fields.append(f)

    for r in rows:
        r["postal_code"] = norm_pc(r.get("postal_code")) or norm_pc(r.get("address"))
    found = {}
    if not a.no_lookup:
        found = lookup([r["postal_code"] for r in rows])

    kept, why = [], Counter()
    for r in rows:
        pc = r["postal_code"]
        res = found.get(pc) if found else None
        if res:
            if res.get("region") != a.ons_region:
                why["outside region (ONS lookup)"] += 1
                continue
            r["county"] = res.get("admin_county") or res.get("admin_district") or r.get("county", "")
            r["district"] = res.get("admin_district") or ""
            why["kept (ONS lookup)"] += 1
        else:
            if not pc:
                why["no postcode"] += 1
                continue
            if area(pc) not in AREAS or outward(pc) in EXCLUDE:
                why["outside region (postcode area)"] += 1
                continue
            why["kept (postcode area fallback)"] += 1
        r["state"], r["state_code"] = a.state_name, a.state_code
        kept.append(r)

    if "district" not in fields and any("district" in r for r in kept):
        fields.append("district")
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(kept)

    counties = Counter(r.get("county") or "(unknown)" for r in kept)
    report = [f"# UK region filter: {a.state_name}", "",
              f"- Rows in: {len(rows):,}", f"- Rows kept: {len(kept):,}", ""]
    report += [f"- {k}: {v:,}" for k, v in why.most_common()]
    report += ["", "## Kept rows by county or unitary authority", ""] + [f"- {k}: {v:,}" for k, v in counties.most_common()]
    rp = os.path.splitext(a.out)[0] + "-region-report.md"
    open(rp, "w", encoding="utf-8").write("\n".join(report) + "\n")
    print("\n".join(report[:5 + len(why)]))
    print(f"Report: {rp}\nNext: Gate 2 with --state {a.state_code}")


if __name__ == "__main__":
    main()
