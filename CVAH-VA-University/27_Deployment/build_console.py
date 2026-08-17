#!/usr/bin/env python3
"""
Build the CVAH VAU operator console.

Reads Markdown/JSON/CSV from the repository and emits one self-contained HTML file.

    python3 27_Deployment/build_console.py            # production build (default)
    python3 27_Deployment/build_console.py --review   # medical-reviewer build

PRODUCTION BUILD CONTRACT
  - Contains NO unapproved high-risk numeric clinical values. Not hidden behind a
    click, not collapsed, not obfuscated: absent from the file.
  - An unapproved Controlled Reference Card renders as a placeholder naming the card,
    its owner, and what it is waiting for.

REVIEW BUILD CONTRACT
  - Written to a separate filename, watermarked on every card, intended for the
    Medical Reviewer only. Never deploy it to learners.

This script RENDERS clinical content. It must never AUTHOR any. Clinically
meaningful text belongs in the repository (see 28_Knowledge_Base/README.md).
"""
import os, re, json, html, glob, csv, argparse, subprocess, hashlib
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # …/CVAH-VA-University
REPO = ROOT.parent                                   # repository root
STALE_AFTER_DAYS = 90

# ---------------------------------------------------------------- markdown
def esc(s):
    return html.escape(s, quote=False)

def inline(s):
    s = esc(s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'\[(SAFETY|LAW|IFU|EVIDENCE|HOUSE|SCORED|GUIDE)\]',
               r'<span class="lvl lvl-\1">\1</span>', s)
    s = re.sub(r'\b((?:TS|PA|CSC|QB|CRC|SIM|INT|VID|EQ|WDF|ANE|SCOPE|TSI)-[A-Z0-9\-]{2,})',
               r'<span class="id">\1</span>', s)
    return s

def md2html(md):
    lines, out, i = md.split("\n"), [], 0
    in_ul = in_ol = False
    def close():
        nonlocal in_ul, in_ol
        if in_ul: out.append("</ul>"); in_ul = False
        if in_ol: out.append("</ol>"); in_ol = False
    while i < len(lines):
        ln = lines[i].rstrip()
        if ln.startswith("|") and i + 1 < len(lines) and re.match(r'^\|[\s:\-\|]+\|?$', lines[i+1].strip()):
            close()
            head = [c.strip() for c in ln.strip().strip("|").split("|")]
            i += 2; rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            t = ['<div class="tw"><table><thead><tr>'] + [f"<th>{inline(c)}</th>" for c in head] + ["</tr></thead><tbody>"]
            for r in rows:
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table></div>"); out.append("".join(t)); continue
        if not ln.strip(): close(); i += 1; continue
        m = re.match(r'^(#{1,6})\s+(.*)$', ln)
        if m:
            close(); out.append(f"<h{min(len(m.group(1))+1,6)}>{inline(m.group(2))}</h{min(len(m.group(1))+1,6)}>"); i += 1; continue
        if re.match(r'^(---+|___+)$', ln.strip()): close(); out.append("<hr>"); i += 1; continue
        m = re.match(r'^\s*[-*]\s+(.*)$', ln)
        if m:
            if in_ol: out.append("</ol>"); in_ol = False
            if not in_ul: out.append("<ul>"); in_ul = True
            out.append(f"<li>{inline(m.group(1))}</li>"); i += 1; continue
        m = re.match(r'^\s*\d+[\.\)]\s+(.*)$', ln)
        if m:
            if in_ul: out.append("</ul>"); in_ul = False
            if not in_ol: out.append("<ol>"); in_ol = True
            out.append(f"<li>{inline(m.group(1))}</li>"); i += 1; continue
        if ln.startswith(">"):
            close(); out.append(f"<blockquote>{inline(ln.lstrip('> '))}</blockquote>"); i += 1; continue
        close(); out.append(f"<p>{inline(ln)}</p>"); i += 1
    close()
    return "\n".join(out)

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

def strip_tags(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)).strip()

# ---------------------------------------------------------------- collect
SOURCES = []            # every source path consumed, for the drift hash
DOCS = []

def add_file(sid, title, group, rel, meta=""):
    md = re.sub(r'^#\s+.*\n', '', read(rel), count=1)
    SOURCES.append(rel)
    h = md2html(md)
    DOCS.append({"id": sid, "title": title, "group": group, "meta": meta,
                 "html": h, "text": strip_tags(h)[:20000]})

CSC = [("csc-ven01","Canine cephalic venipuncture","CSC-VEN-01_Canine_Cephalic_Venipuncture.md","TS-VEN-CEPH-001"),
       ("csc-ven02","Feline medial saphenous","CSC-VEN-02_Feline_Medial_Saphenous.md","TS-VEN-SAPH-001"),
       ("csc-ven03","Jugular venipuncture","CSC-VEN-03_Jugular_Venipuncture.md","TS-VEN-JUG-001"),
       ("csc-ivc01","Cephalic IV catheter","CSC-IVC-01_Cephalic_IV_Catheter.md","TS-IVC-CEPH-001"),
       ("csc-res01","Canine restraint","CSC-RES-01_Canine_Restraint.md","TS-RES-001/2/3"),
       ("csc-res02","Feline restraint","CSC-RES-02_Feline_Restraint.md","TS-RES-002/3"),
       ("csc-asm01","TPR & basic assessment","CSC-ASM-01_TPR_Basic_Assessment.md","TS-ASM-001"),
       ("csc-sur01","Surgical patient prep","CSC-SUR-01_Surgical_Patient_Prep.md","TS-SUR-PREP-001"),
       ("csc-flu01","Fluid lines & pumps","CSC-FLU-01_Fluid_Lines_Monitoring.md","TS-FLU-001/2"),
       ("csc-ane01","Anesthesia monitoring","CSC-ANE-01_Foundational_Anesthesia_Monitoring.md","TS-ANE-103")]
for sid, title, fn, spec in CSC:
    add_file(sid, title, "Skill courses", f"05_Technical_Skills_Library/Clinical_Skill_Courses/{fn}", spec)

for wk in range(9):
    for p in sorted((ROOT / "04_Core_VA_Academy" / f"Week_{wk}").glob("*.md")):
        code = p.name.split("_")[0]
        add_file(f"lsn-{code.lower()}", f"{code} · {p.stem.split('_',1)[1].replace('_',' ')}",
                 "Lessons", f"04_Core_VA_Academy/Week_{wk}/{p.name}", f"Week {wk}")

for sid, title, fn in [("rub-ven","Venipuncture practical","PA-VEN-CEPH-001.md"),
                       ("rub-ivc","IV catheter practical","PA-IVC-CEPH-001.md"),
                       ("rub-res","Restraint practical A–D","PA-RES-001.md"),
                       ("rub-tpr","TPR practical","PA-ASM-TPR-001.md"),
                       ("rub-compact","Compact set: injections, meds, fluids, surgery, imaging, SBAR-V","PA-Compact_Set.md"),
                       ("rub-spec","Specialty practicals","PA-Specialty_Set.md"),
                       ("rub-grad","Core graduation — 13 stations","Core_Graduation_Practical_Stations.md"),
                       ("rub-std","Scoring standards & critical fails","Rubric_Standards.md")]:
    add_file(sid, title, "Assess", f"15_Practical_Competencies/{fn}", "printable")
add_file("case-reps","Repetition requirements","Assess","16_Case_Logs/Repetition_Requirements.md")
add_file("case-log","Case log & pocket card","Assess","16_Case_Logs/Case_Log_Specification.md")

for sid, title, rel, meta in [
    ("focus","Now / Next / Later — learner focus model","03_Competency_Framework/Learner_Focus_Model.md",""),
    ("grad","Graduation — the nine gates","03_Competency_Framework/Graduation_Requirements.md",""),
    ("valev","VA1 / VA2 / VA3 standards","03_Competency_Framework/VA_Levels.md",""),
    ("workload","Clinical workload ownership","03_Competency_Framework/Clinical_Workload_Ownership_Matrix.md",""),
    ("hcis","Human-Centered Instruction Standard","01_University_Governance/Human_Centered_Instruction_Standard.md","binding"),
    ("status","Go-live status ladder","00_Project_Control/Go_Live_Status.md","current stage"),
    ("pilot","Pilot feedback loop","00_Project_Control/Pilot_Feedback_Loop.md","build gate"),
    ("impl","Implementation guide","27_Deployment/Implementation_Guide.md",""),
    ("roles","Governance roles","01_University_Governance/Governance_Roles.md",""),
    ("scope","Arizona scope matrix","02_Scope_and_Regulatory/Arizona_Scope_Matrix.md","verify before use"),
    ("scopecls","Scope & supervision definitions","02_Scope_and_Regulatory/Scope_Classification_System.md",""),
    ("periop","Perioperative pathways & tiers","06_Perioperative_Anesthesia_Academy/Role_Based_Pathways.md",""),
    ("sweep","Language precision sweep","00_Project_Control/Language_Precision_Sweep.md",""),
    ("qa","QA report","27_Deployment/QA_Report.md","")]:
    add_file(sid, title, "Run it", rel, meta)

# ---------------------------------------------------------------- knowledge base
kb = json.loads(read("28_Knowledge_Base/Troubleshooting_Index.json"))
SOURCES.append("28_Knowledge_Base/Troubleshooting_Index.json")
TROUBLE = [{"id": e["id"], "symptom": e["symptom"], "answer": e["answer"],
            "target": e["console_target"], "src": e["source_document"],
            "approved": e["review_status"] == "approved"} for e in kb["entries"]]

# ---------------------------------------------------------------- controlled references
def load_crc(review_mode):
    reg = list(csv.DictReader((ROOT / "18_Controlled_References/crc_register.csv").open(encoding="utf-8")))
    SOURCES.append("18_Controlled_References/crc_register.csv")
    files = {"CRC-001": "CRC-001_Vital_Sign_Bands.md", "CRC-002": "CRC-002_CPR_Quick_Reference.md",
             "CRC-003": "CRC-003_Anesthesia_Alert_Thresholds.md", "CRC-005": "CRC-005_Crash_Cart_Checklist.md"}
    cards, withheld = [], 0
    for row in reg:
        cid, approved = row["crc_id"], row["status"].strip().lower() == "approved"
        card = {"id": cid, "title": row["title"], "approved": approved,
                "version": row["version"], "approved_by": row["approved_by"],
                "approval_date": row["approval_date"], "next_review": row["next_review"],
                "posted": row["location_posted"], "body": None}
        if approved and cid in files:
            card["body"] = md2html(re.sub(r'^#\s+.*\n', '', read(f"18_Controlled_References/{files[cid]}"), count=1))
            SOURCES.append(f"18_Controlled_References/{files[cid]}")
        elif review_mode and cid in files:
            card["body"] = md2html(re.sub(r'^#\s+.*\n', '', read(f"18_Controlled_References/{files[cid]}"), count=1))
            SOURCES.append(f"18_Controlled_References/{files[cid]}")
        elif cid in files:
            withheld += 1
        cards.append(card)
    return cards, withheld

# ---------------------------------------------------------------- metadata
def git(*args, default=""):
    try:
        return subprocess.run(["git", *args], cwd=str(REPO), capture_output=True,
                              text=True, timeout=10).stdout.strip() or default
    except Exception:
        return default

def all_source_paths():
    """Deterministic set of every file that can affect a console build.

    Must not depend on call order — the QA freshness check recomputes this
    without running a full build, so anything gathered lazily would give a
    different answer and produce a phantom 'stale console' failure.
    """
    paths = set(SOURCES)
    paths |= {str(p.relative_to(ROOT)) for p in (ROOT / "05_Technical_Skills_Library/Clinical_Skill_Courses").glob("CSC-*.md")}
    paths |= {str(p.relative_to(ROOT)) for p in ROOT.glob("04_Core_VA_Academy/Week_*/*.md")}
    paths |= {str(p.relative_to(ROOT)) for p in (ROOT / "15_Practical_Competencies").glob("*.md")}
    paths |= {str(p.relative_to(ROOT)) for p in (ROOT / "18_Controlled_References").glob("*")}
    paths |= {"28_Knowledge_Base/Troubleshooting_Index.json",
              "02_Scope_and_Regulatory/Arizona_Scope_Matrix.csv",
              "02_Scope_and_Regulatory/Arizona_Scope_Matrix.md",
              "00_Project_Control/Go_Live_Status.md",
              "00_Project_Control/BUILD_MANIFEST.json",
              "27_Deployment/console_template.html"}
    return sorted(p for p in paths if (ROOT / p).exists())

def source_fingerprint():
    h = hashlib.sha256()
    for rel in all_source_paths():
        h.update(rel.encode()); h.update((ROOT / rel).read_bytes())
    return h.hexdigest()[:16]

def regulatory_verification():
    """Latest verified_date across scope rows; and how many T2 rows remain unverified."""
    rows = list(csv.DictReader((ROOT / "02_Scope_and_Regulatory/Arizona_Scope_Matrix.csv").open(encoding="utf-8")))
    SOURCES.append("02_Scope_and_Regulatory/Arizona_Scope_Matrix.csv")
    dates = [r["verified_date"] for r in rows if r.get("verified_date")]
    t2 = [r for r in rows if r.get("risk_tier") == "T2"]
    unver = [r["task_id"] for r in t2 if r.get("board_rule_verified", "") != "VERIFIED"]
    return (max(dates) if dates else None), len(t2), unver

def build_meta(mode, cards, withheld):
    manifest = json.loads(read("00_Project_Control/BUILD_MANIFEST.json"))
    stage = "UNKNOWN"
    m = re.search(r'\*\*Current stage: `([A-Z /]+)`\*\*', read("00_Project_Control/Go_Live_Status.md"))
    if m: stage = m.group(1)
    reg_date, t2_count, t2_unver = regulatory_verification()
    now = datetime.now(timezone.utc)
    return {
        "mode": mode,
        "stage": stage,
        "curriculum_version": manifest.get("version", "?"),
        "built_utc": now.strftime("%Y-%m-%d %H:%M UTC"),
        "built_epoch": int(now.timestamp()),
        "stale_after_days": STALE_AFTER_DAYS,
        "commit": git("rev-parse", "--short", "HEAD", default="not-a-git-checkout"),
        "branch": git("rev-parse", "--abbrev-ref", "HEAD", default="?"),
        "dirty": bool(git("status", "--porcelain")),
        "fingerprint": source_fingerprint(),
        "regulatory_verified": reg_date,
        "t2_rows": t2_count,
        "t2_unverified": len(t2_unver),
        "crc_total": len(cards),
        "crc_approved": sum(1 for c in cards if c["approved"]),
        "crc_withheld": withheld,
        "kb_entries": len(TROUBLE),
        "kb_unreviewed": sum(1 for t in TROUBLE if not t["approved"]),
        "doc_count": len(DOCS),
        "lesson_count": sum(1 for d in DOCS if d["group"] == "Lessons"),
        "csc_count": sum(1 for d in DOCS if d["group"] == "Skill courses"),
        "rubric_count": sum(1 for d in DOCS if d["group"] == "Assess"),
        "placeholders": sum(len(re.findall(r'CVAH-SPECIFIC INPUT REQUIRED', (ROOT / p).read_text(encoding="utf-8")))
                            for p in [str(x.relative_to(ROOT)) for x in ROOT.rglob("*.md")]),
    }

GATE = [
    ("Assign the four roles", "Program administrator, medical reviewer (DVM), assessors (CVT/DVM), supervising techs.", "roles", "30 min"),
    ("Verify the T2 scope rows", "Ten higher-risk rows need current Board-rule verification plus a written CVAH policy decision. Until then they read NOT PERMITTED.", "scope", "2 h"),
    ("Approve the reference cards", "Medical director reviews and signs the controlled cards. Their values are absent from this build until then.", "status", "2 h"),
    ("Answer the R1a review question", "A senior CVT reads each skill course and answers: would we actually teach it this way?", "hcis", "2 h"),
    ("Fill the local-input items", "Flagged facts and decisions across the curriculum — equipment models, products, protocols.", None, "1 h"),
    ("Run the equipment survey", "Walk the hospital with a phone camera; record analyzer, pump, machine, and imaging models.", None, "1 h"),
    ("Calibrate your assessors", "Two assessors score the same performance and compare. Gaps over 2 points get discussed.", "rub-std", "half day"),
]

# ---------------------------------------------------------------- template
TEMPLATE = Path(__file__).with_name("console_template.html").read_text(encoding="utf-8")

def build(review_mode):
    cards, withheld = load_crc(review_mode)
    meta = build_meta("review" if review_mode else "production", cards, withheld)
    payload = {"docs": DOCS, "crc": cards, "trouble": TROUBLE, "gate": GATE, "meta": meta}
    out = TEMPLATE.replace("__DATA__", json.dumps(payload, ensure_ascii=False))
    out = out.replace("__GROUPS__", json.dumps(["Start", "Skill courses", "Lessons", "Assess", "Reference", "Run it"]))
    name = "cvah_university_console.review.html" if review_mode else "cvah_university_console.html"
    dest = ROOT / "27_Deployment" / name
    dest.write_text(out, encoding="utf-8")
    return dest, meta

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--review", action="store_true", help="build the Medical Reviewer copy (exposes pending CRC values)")
    args = ap.parse_args()
    dest, meta = build(args.review)
    print(f"wrote {dest.relative_to(REPO)}  ({dest.stat().st_size // 1024} KB)  mode={meta['mode']}")
    print(f"  stage={meta['stage']}  commit={meta['commit']}{'+dirty' if meta['dirty'] else ''}  fingerprint={meta['fingerprint']}")
    print(f"  docs={meta['doc_count']} (lessons {meta['lesson_count']}, courses {meta['csc_count']}, rubrics {meta['rubric_count']})")
    print(f"  CRC approved {meta['crc_approved']}/{meta['crc_total']}"
          + (f", {meta['crc_withheld']} withheld from this build" if meta["crc_withheld"] else ""))
    print(f"  KB entries {meta['kb_entries']} ({meta['kb_unreviewed']} unreviewed)"
          f"  T2 scope rows unverified {meta['t2_unverified']}/{meta['t2_rows']}"
          f"  placeholders {meta['placeholders']}")
    if not args.review and meta["crc_withheld"]:
        print("  NOTE: production build — unapproved clinical values are absent, not hidden.")
