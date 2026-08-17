#!/usr/bin/env python3
"""
CVAH VAU quality gate. Institutionalises the audits this project has had to run by hand.

    python3 00_Project_Control/qa_check.py            # report, exit 1 on any FAIL
    python3 00_Project_Control/qa_check.py --release  # additionally enforce release-only gates

Checks
  1  assessment answer-leakage      key-position bias and longest-answer giveaway
  2  duplicate IDs                  question, skill, and knowledge-base identifiers
  3  broken internal references     every referenced repo path exists
  4  regulatory citation integrity  §32-2281 never used as an assistant-scope statute
  5  T2 scope verification          higher-risk rows may not read permitted while unverified
  6  controlled-reference status    register consistent; production console leaks no draft values
  7  knowledge-base provenance      every entry traces to a real source document
  8  console freshness              generated console matches current sources
  9  stale regulatory verification  verification not older than one year
 10  placeholder tags               [CVAH-SPECIFIC INPUT REQUIRED] count (release gate)
 11  pilot build gate               remaining skill specs not authored before pilot
 12  human review gate              flagship material unreviewed cannot fail a learner (release gate)
"""
import re, sys, json, csv, glob, statistics, argparse, subprocess
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
FAILS, WARNS, NOTES = [], [], []

def fail(c, m): FAILS.append((c, m))
def warn(c, m): WARNS.append((c, m))
def note(c, m): NOTES.append((c, m))
def rd(p): return (ROOT / p).read_text(encoding="utf-8")

# ---- 1. assessment answer leakage -----------------------------------------
def check_assessment():
    pos = {"A":0,"B":0,"C":0,"D":0}; longest = total = 0
    per_bank = {}
    for f in sorted((ROOT / "14_Question_Banks").glob("QB-*.md")):
        bank_pos = {"A":0,"B":0,"C":0,"D":0}; bank_long = bank_n = 0
        for it in re.split(r"\n### ", f.read_text(encoding="utf-8"))[1:]:
            m = re.search(r"^KEY:\s*([A-D])", it, re.M)
            o = re.search(r"^A\)(.*?)B\)(.*?)C\)(.*?)D\)(.*)$", it, re.M | re.S)
            if not m or not o: continue
            total += 1; bank_n += 1; k = m.group(1); pos[k] += 1; bank_pos[k] += 1
            L = {"A":len(o.group(1)),"B":len(o.group(2)),"C":len(o.group(3)),"D":len(o.group(4).split("\n")[0])}
            med = statistics.median([v for kk,v in L.items() if kk != k])
            if L[k] == max(L.values()) and med and L[k] > 1.5 * med:
                longest += 1; bank_long += 1
        if bank_n: per_bank[f.name] = (bank_pos, bank_long, bank_n)
    if not total:
        return warn("assessment", "no question items found")
    worst = max(pos.values()) / total
    lg = longest / total
    note("assessment", f"{total} items · key positions {pos} · longest-answer giveaway {longest} ({lg:.0%})")
    if worst > 0.40: fail("assessment", f"key-position bias {worst:.0%} exceeds 40% ceiling (was 91% pre-2026-08)")
    elif worst > 0.35: warn("assessment", f"key-position bias {worst:.0%} above 35% target")
    if lg > 0.25: fail("assessment", f"longest-answer giveaway {lg:.0%} exceeds 25% ceiling (was 88% pre-2026-08)")
    elif lg > 0.15: warn("assessment", f"longest-answer giveaway {lg:.0%} above 15% target")
    for name, (bp, bl, bn) in per_bank.items():
        if bn >= 10 and max(bp.values()) / bn > 0.55:
            warn("assessment", f"{name}: {max(bp.values())}/{bn} keys share one position")

# ---- 2. duplicate IDs ------------------------------------------------------
def check_dupe_ids():
    qids = [m.group(1) for f in (ROOT / "14_Question_Banks").glob("QB-*.md")
            for m in re.finditer(r"^### (\S+)\s*\|", f.read_text(encoding="utf-8"), re.M)]
    dupes = {i for i in qids if qids.count(i) > 1}
    if dupes: fail("ids", f"duplicate question IDs: {sorted(dupes)[:8]}")
    else: note("ids", f"{len(qids)} question IDs unique")
    rows = list(csv.DictReader((ROOT / "05_Technical_Skills_Library/Skills_Inventory.csv").open(encoding="utf-8")))
    sids = [r["skill_id"] for r in rows]
    d2 = {i for i in sids if sids.count(i) > 1}
    if d2: fail("ids", f"duplicate skill IDs: {sorted(d2)}")
    else: note("ids", f"{len(sids)} skill IDs unique")
    kb = json.loads(rd("28_Knowledge_Base/Troubleshooting_Index.json"))["entries"]
    kids = [e["id"] for e in kb]
    if len(set(kids)) != len(kids): fail("ids", "duplicate knowledge-base IDs")

# ---- 3. broken internal references -----------------------------------------
def check_refs():
    pat = re.compile(r"`((?:\d\d_[A-Za-z_]+/)[A-Za-z0-9_\-./]+\.(?:md|csv|json|py|html))`")
    missing = set()
    for f in ROOT.rglob("*.md"):
        for m in pat.finditer(f.read_text(encoding="utf-8")):
            if not (ROOT / m.group(1)).exists():
                missing.add((str(f.relative_to(ROOT)), m.group(1)))
    if missing:
        for src, tgt in sorted(missing)[:10]: fail("refs", f"{src} → missing {tgt}")
        if len(missing) > 10: fail("refs", f"…and {len(missing)-10} more")
    else:
        note("refs", "all backticked repo paths resolve")

# ---- 4. regulatory citation integrity --------------------------------------
def check_citations():
    bad = []
    for f in ROOT.rglob("*.md"):
        txt = f.read_text(encoding="utf-8")
        for m in re.finditer(r"[^\n]*32-2281[^\n]*", txt):
            line = m.group(0)
            # Legitimate mentions: dispensing context; explicit warnings not to cite it;
            # and any line naming BOTH statutes, which is discussing their relationship.
            if (re.search(r"dispens", line, re.I) or "never cite" in line
                    or "wrong section" in line or "correction" in line.lower()
                    or "32-2211" in line):
                continue
            bad.append(f"{f.relative_to(ROOT)}: {line.strip()[:90]}")
    if bad:
        for b in bad[:6]: fail("citations", f"§32-2281 used outside dispensing context — {b}")
    else:
        note("citations", "§32-2281 appears only in dispensing context; assistant scope cites §32-2211(5)")
    if "32-2211(5)" not in rd("02_Scope_and_Regulatory/Arizona_Scope_Matrix.md"):
        fail("citations", "scope matrix does not cite §32-2211(5)")

# ---- 5. T2 scope verification ----------------------------------------------
def check_scope():
    rows = list(csv.DictReader((ROOT / "02_Scope_and_Regulatory/Arizona_Scope_Matrix.csv").open(encoding="utf-8")))
    t2 = [r for r in rows if r.get("risk_tier") == "T2"]
    bad = [r["task_id"] for r in t2
           if r.get("board_rule_verified") != "VERIFIED" and r.get("assistant_permitted_pending_verification") == "YES"]
    if bad: fail("scope", f"T2 rows marked permitted without Board-rule verification: {bad}")
    unver = [r["task_id"] for r in t2 if r.get("board_rule_verified") != "VERIFIED"]
    note("scope", f"{len(t2)} T2 rows · {len(unver)} awaiting Board-rule verification")

# ---- 6. controlled references ----------------------------------------------
DRAFT_MARKERS = ["100.0–102.5", "160–220", "<25 or >55", "<60 mmHg", "Reviewing veterinarian: ________"]
def check_crc():
    reg = list(csv.DictReader((ROOT / "18_Controlled_References/crc_register.csv").open(encoding="utf-8")))
    approved = [r for r in reg if r["status"].strip().lower() == "approved"]
    for r in approved:
        if not (r["approved_by"] and r["approval_date"] and r["next_review"]):
            fail("crc", f"{r['crc_id']} marked approved but missing reviewer/date/next-review")
    note("crc", f"{len(approved)}/{len(reg)} reference cards approved")
    prod = ROOT / "27_Deployment/cvah_university_console.html"
    if prod.exists():
        t = prod.read_text(encoding="utf-8")
        leaks = [m for m in DRAFT_MARKERS if m in t]
        if leaks: fail("crc", f"PRODUCTION console contains unapproved clinical values: {leaks}")
        else: note("crc", "production console carries no unapproved clinical values")

# ---- 7. knowledge-base provenance ------------------------------------------
def check_kb():
    kb = json.loads(rd("28_Knowledge_Base/Troubleshooting_Index.json"))
    miss = [e["id"] for e in kb["entries"] if not (ROOT / e["source_document"]).exists()]
    if miss: fail("kb", f"entries whose source_document does not exist: {miss}")
    unrev = [e["id"] for e in kb["entries"] if e["review_status"] != "approved"]
    note("kb", f"{len(kb['entries'])} entries · {len(unrev)} awaiting review")
    src = rd("27_Deployment/build_console.py")
    if re.search(r'^\s*TROUBLE\s*=\s*\[\s*\(', src, re.M):
        fail("kb", "build_console.py authors clinical content inline — it must render only")

# ---- 8. console freshness ---------------------------------------------------
def check_console_fresh():
    prod = ROOT / "27_Deployment/cvah_university_console.html"
    if not prod.exists():
        return warn("console", "no production console built")
    m = re.search(r'"fingerprint":\s*"([0-9a-f]+)"', prod.read_text(encoding="utf-8"))
    if not m:
        return warn("console", "console has no source fingerprint")
    sys.path.insert(0, str(ROOT / "27_Deployment"))
    try:
        import importlib, build_console
        importlib.reload(build_console)
        current = build_console.source_fingerprint()
    except Exception as e:
        return warn("console", f"could not recompute fingerprint: {e}")
    if current != m.group(1):
        fail("console", f"console is stale — sources changed since build (built {m.group(1)}, now {current}); run build_console.py")
    else:
        note("console", f"console matches current sources ({current})")

# ---- 9. stale regulatory verification --------------------------------------
def check_reg_age():
    rows = list(csv.DictReader((ROOT / "02_Scope_and_Regulatory/Arizona_Scope_Matrix.csv").open(encoding="utf-8")))
    dates = [r["verified_date"] for r in rows if r.get("verified_date")]
    if not dates:
        return warn("regulatory", "no scope row has ever been verified against Board rules")
    newest = max(dates)
    try:
        age = (datetime.now(timezone.utc) - datetime.fromisoformat(newest).replace(tzinfo=timezone.utc)).days
    except ValueError:
        return warn("regulatory", f"unparseable verified_date: {newest}")
    if age > 365: fail("regulatory", f"most recent verification is {age} days old — annual re-verification overdue")
    else: note("regulatory", f"most recent verification {age} days ago")

# ---- 10/11/12 release gates -------------------------------------------------
def check_placeholders(release):
    n = sum(len(re.findall(r"CVAH-SPECIFIC INPUT REQUIRED", f.read_text(encoding="utf-8")))
            for f in list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.csv")))
    note("placeholders", f"{n} unresolved [CVAH-SPECIFIC INPUT REQUIRED] tags")
    if release and n: fail("placeholders", f"{n} unresolved placeholders block a release build")

def check_pilot_gate():
    rows = list(csv.DictReader((ROOT / "05_Technical_Skills_Library/Skills_Inventory.csv").open(encoding="utf-8")))
    specced = len(list((ROOT / "05_Technical_Skills_Library").glob("TS-*.md")))
    pending = sum(1 for r in rows if r.get("spec_status") == "inventoried")
    pilot_done = "PILOT VALIDATED" in rd("00_Project_Control/Go_Live_Status.md").split("## The ladder")[0]
    note("pilot", f"{specced} skill specs written · {pending} awaiting the pilot gate")
    if pending == 0 and not pilot_done:
        fail("pilot", "all skill specs authored without a completed pilot cycle — see Pilot_Feedback_Loop.md §4")

def check_human_review(release):
    unreviewed = [p.name for p in (ROOT / "05_Technical_Skills_Library/Clinical_Skill_Courses").glob("CSC-*.md")
                  if "Pending human review at pilot" in p.read_text(encoding="utf-8")]
    note("review", f"{len(unreviewed)} skill courses awaiting the R1a human review question")
    if release and unreviewed:
        fail("review", f"{len(unreviewed)} courses unreviewed — may teach, may not be the basis of a failing assessment")

# ---- run --------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--release", action="store_true", help="enforce release-only gates")
    a = ap.parse_args()
    for fn in (check_assessment, check_dupe_ids, check_refs, check_citations,
               check_scope, check_crc, check_kb, check_console_fresh, check_reg_age):
        try: fn()
        except Exception as e: fail(fn.__name__, f"check errored: {e}")
    check_placeholders(a.release); check_pilot_gate(); check_human_review(a.release)

    w = max((len(c) for c, _ in NOTES + WARNS + FAILS), default=10)
    print("CVAH VAU quality gate" + (" — RELEASE MODE" if a.release else ""))
    print("-" * 74)
    for c, m in NOTES: print(f"  ok    {c:<{w}}  {m}")
    for c, m in WARNS: print(f"  WARN  {c:<{w}}  {m}")
    for c, m in FAILS: print(f"  FAIL  {c:<{w}}  {m}")
    print("-" * 74)
    print(f"{len(NOTES)} passed · {len(WARNS)} warnings · {len(FAILS)} failures")
    return 1 if FAILS else 0

if __name__ == "__main__":
    sys.exit(main())
