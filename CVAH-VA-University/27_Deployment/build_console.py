#!/usr/bin/env python3
"""Build the CVAH VAU operator console: reads repo markdown, emits one self-contained HTML file."""
import os, re, json, html, glob

ROOT = "/home/user/hello-world/CVAH-VA-University"
OUT = "/home/user/hello-world/CVAH-VA-University/27_Deployment/cvah_university_console.html"

# ---------- minimal markdown -> html ----------
def esc(s):
    return html.escape(s, quote=False)

def inline(s):
    s = esc(s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'<em>\1</em>', s)
    # skill / question / card IDs get the mono treatment
    s = re.sub(r'\b((?:TS|PA|CSC|QB|CRC|SIM|INT|VID|EQ|WDF|ANE|SCOPE)-[A-Z0-9\-]{2,})', r'<span class="id">\1</span>', s)
    return s

def md2html(md):
    lines = md.split("\n")
    out, i = [], 0
    in_ul = in_ol = False
    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul: out.append("</ul>"); in_ul = False
        if in_ol: out.append("</ol>"); in_ol = False
    while i < len(lines):
        ln = lines[i].rstrip()
        # table
        if ln.startswith("|") and i + 1 < len(lines) and re.match(r'^\|[\s:\-\|]+\|?$', lines[i+1].strip()):
            close_lists()
            head = [c.strip() for c in ln.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            t = ['<div class="tw"><table><thead><tr>']
            t += [f"<th>{inline(c)}</th>" for c in head]
            t.append("</tr></thead><tbody>")
            for r in rows:
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table></div>")
            out.append("".join(t))
            continue
        if not ln.strip():
            close_lists(); i += 1; continue
        m = re.match(r'^(#{1,6})\s+(.*)$', ln)
        if m:
            close_lists()
            lvl = min(len(m.group(1)) + 1, 6)
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            i += 1; continue
        if re.match(r'^(---+|___+)$', ln.strip()):
            close_lists(); out.append("<hr>"); i += 1; continue
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
            close_lists(); out.append(f"<blockquote>{inline(ln.lstrip('> '))}</blockquote>"); i += 1; continue
        close_lists()
        out.append(f"<p>{inline(ln)}</p>")
        i += 1
    close_lists()
    return "\n".join(out)

def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()

def strip_tags(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)).strip()

DOCS = []
def add(sid, title, group, body_md, meta=""):
    h = md2html(body_md)
    DOCS.append({"id": sid, "title": title, "group": group, "meta": meta,
                 "html": h, "text": strip_tags(h)[:20000]})

def add_file(sid, title, group, rel, meta=""):
    md = read(rel)
    md = re.sub(r'^#\s+.*\n', '', md, count=1)  # drop dup H1
    add(sid, title, group, md, meta)

# ---------- CLINICAL SKILL COURSES ----------
CSC = [
    ("csc-ven01", "Canine cephalic venipuncture", "CSC-VEN-01_Canine_Cephalic_Venipuncture.md", "TS-VEN-CEPH-001"),
    ("csc-ven02", "Feline medial saphenous", "CSC-VEN-02_Feline_Medial_Saphenous.md", "TS-VEN-SAPH-001"),
    ("csc-ven03", "Jugular venipuncture", "CSC-VEN-03_Jugular_Venipuncture.md", "TS-VEN-JUG-001"),
    ("csc-ivc01", "Cephalic IV catheter", "CSC-IVC-01_Cephalic_IV_Catheter.md", "TS-IVC-CEPH-001"),
    ("csc-res01", "Canine restraint", "CSC-RES-01_Canine_Restraint.md", "TS-RES-001/2/3"),
    ("csc-res02", "Feline restraint", "CSC-RES-02_Feline_Restraint.md", "TS-RES-002/3"),
    ("csc-asm01", "TPR & basic assessment", "CSC-ASM-01_TPR_Basic_Assessment.md", "TS-ASM-001"),
    ("csc-sur01", "Surgical patient prep", "CSC-SUR-01_Surgical_Patient_Prep.md", "TS-SUR-PREP-001"),
    ("csc-flu01", "Fluid lines & pumps", "CSC-FLU-01_Fluid_Lines_Monitoring.md", "TS-FLU-001/2"),
    ("csc-ane01", "Anesthesia monitoring", "CSC-ANE-01_Foundational_Anesthesia_Monitoring.md", "TS-ANE-103"),
]
for sid, title, fn, spec in CSC:
    add_file(sid, title, "Skill courses", f"05_Technical_Skills_Library/Clinical_Skill_Courses/{fn}", spec)

# ---------- LESSONS ----------
for wk, folder in [("Week 0", "Week_0"), ("Week 1", "Week_1"), ("Week 2", "Week_2"), ("Week 3", "Week_3"),
                   ("Week 4", "Week_4"), ("Week 5", "Week_5"), ("Week 6", "Week_6"), ("Week 7", "Week_7"), ("Week 8", "Week_8")]:
    for p in sorted(glob.glob(os.path.join(ROOT, "04_Core_VA_Academy", folder, "*.md"))):
        base = os.path.basename(p)
        code = base.split("_")[0]
        t = base.replace(".md", "").split("_", 1)[1].replace("_", " ")
        add_file(f"lsn-{code.lower()}", f"{code} · {t}", "Lessons",
                 f"04_Core_VA_Academy/{folder}/{base}", wk)

# ---------- RUBRICS ----------
RUB = [
    ("rub-ven", "Venipuncture practical", "PA-VEN-CEPH-001.md"),
    ("rub-ivc", "IV catheter practical", "PA-IVC-CEPH-001.md"),
    ("rub-res", "Restraint practical A–D", "PA-RES-001.md"),
    ("rub-tpr", "TPR practical", "PA-ASM-TPR-001.md"),
    ("rub-compact", "Compact set: injections, meds, fluids, surgery, imaging, SBAR-V", "PA-Compact_Set.md"),
    ("rub-spec", "Specialty practicals", "PA-Specialty_Set.md"),
    ("rub-grad", "Core graduation — 13 stations", "Core_Graduation_Practical_Stations.md"),
    ("rub-std", "Scoring standards & critical fails", "Rubric_Standards.md"),
]
for sid, title, fn in RUB:
    add_file(sid, title, "Assess", f"15_Practical_Competencies/{fn}", "printable")

add_file("case-reps", "Repetition requirements", "Assess", "16_Case_Logs/Repetition_Requirements.md")
add_file("case-log", "Case log & pocket card", "Assess", "16_Case_Logs/Case_Log_Specification.md")

# ---------- FRAMEWORK / RUN IT ----------
add_file("grad", "Graduation — the nine gates", "Run it", "03_Competency_Framework/Graduation_Requirements.md")
add_file("valev", "VA1 / VA2 / VA3 standards", "Run it", "03_Competency_Framework/VA_Levels.md")
add_file("workload", "Clinical workload ownership", "Run it", "03_Competency_Framework/Clinical_Workload_Ownership_Matrix.md")
add_file("impl", "Implementation guide", "Run it", "27_Deployment/Implementation_Guide.md")
add_file("roles", "Governance roles", "Run it", "01_University_Governance/Governance_Roles.md")
add_file("scope", "Arizona scope matrix", "Run it", "02_Scope_and_Regulatory/Arizona_Scope_Matrix.md", "verify before use")
add_file("periop", "Perioperative pathways & tiers", "Run it", "06_Perioperative_Anesthesia_Academy/Role_Based_Pathways.md")
add_file("qa", "QA report", "Run it", "27_Deployment/QA_Report.md")

# ---------- CONTROLLED REFERENCE CARDS (gated) ----------
CRC = []
for fn, title in [("CRC-001_Vital_Sign_Bands.md", "CRC-001 · Vital-sign bands"),
                  ("CRC-002_CPR_Quick_Reference.md", "CRC-002 · CPR quick reference"),
                  ("CRC-003_Anesthesia_Alert_Thresholds.md", "CRC-003 · Anesthesia alert thresholds"),
                  ("CRC-005_Crash_Cart_Checklist.md", "CRC-005 · Crash cart checklist")]:
    md = re.sub(r'^#\s+.*\n', '', read(f"18_Controlled_References/{fn}"), count=1)
    CRC.append({"title": title, "html": md2html(md)})

# ---------- TROUBLESHOOTING INDEX (hand-authored routing layer) ----------
TROUBLE = [
    ("No flash on venipuncture", "Withdraw to just under the skin, re-palpate, redirect once — that is still the same attempt. Never sweep the needle side-to-side underground.", "csc-ven01"),
    ("Flash, then flow stops", "Drop the angle flat, advance 1–2 mm, rotate a quarter-turn, ease the plunger. Two cycles with nothing = attempt over.", "csc-ven01"),
    ("Catheter won't thread", "Advance the unit 1 mm more and flatten; slight rotation while threading. If it still resists, remove catheter AND stylet together — never re-advance over the stylet.", "csc-ivc01"),
    ("Flush meets resistance", "Stop. Never force. Check limb position, aspirate gently, report. Forcing can fire a clot or push fluid subcutaneously.", "csc-ivc01"),
    ("Is it infiltration or phlebitis?", "Cool, doughy, swelling, sluggish flush = infiltration. Warm, red, cord-like, painful on flush = phlebitis. Both get reported; phlebitis usually gets a removal order.", "csc-ivc01"),
    ("Pump keeps alarming occlusion", "Trace the line first: kink, closed clamp, positional limb — then the site. Never silence and walk, never raise the pressure limit.", "csc-flu01"),
    ("Air-in-line alarm", "Clamp, disconnect at the port per protocol, re-prime or replace the set. Never open the door and flick bubbles toward the patient.", "csc-flu01"),
    ("Pump says delivered, bag says otherwise", "Stop and trace — a free path or mis-loaded set. Pumps count volume pushed, not where it went.", "csc-flu01"),
    ("Smear has no feathered edge", "Angle too steep or drop too big. Lower the spreader angle, smaller drop, remake.", "csc-ven01"),
    ("Sample came back hemolyzed", "Usually operator-side: aspirating too hard, needle-through-stopper transfer, or shaking. Gentle and prompt beats fast.", "csc-ven01"),
    ("Cat starts open-mouth breathing", "Stop immediately, release the position, alert the CVT. This is decompensation, not stress that settles.", "csc-res02"),
    ("Cat won't come out of the carrier", "Take the top off; work in the bottom half with a towel. Never dump, never drag.", "csc-res02"),
    ("Dog is frozen and staring", "That is closer to a bite than a growling dog. Decompress, slow down, replan — do not push through.", "csc-res01"),
    ("EtCO2 just went flat", "Hands on patient and circuit NOW while you announce it. SpO2 stays falsely reassuring for minutes on oxygen.", "csc-ane01"),
    ("Capnogram baseline won't return to zero", "Rebreathing — exhausted absorbent, stuck valve, or inadequate fresh gas. Report; the anesthetist acts.", "csc-ane01"),
    ("SpO2 low but waveform is ragged", "Report AND reposition the probe — simultaneously, never silently. If a new site agrees, it was never artifact.", "csc-ane01"),
    ("ECG looks chaotic but the pulse is fine", "Check electrode contact, fix it, and still report what you found. Artifact is explained, never assumed.", "csc-ane01"),
    ("Blood pressure reading looks wrong", "Patient check, then technique check (cuff width ≈ 40% of limb circumference), then repeat one cycle. Report the number with your verification attached.", "csc-ane01"),
    ("Post-extubation noisy breathing", "Stridor = airway narrowing. Emergency-tier report, oxygen, re-intubation kit at hand. Brachycephalics obstruct late.", "csc-ane01"),
    ("How do I open a sterile pack?", "Check integrity and indicators, first flap away from you, touch only outer surfaces, never reach over the field. Doubt = contaminated, declare it.", "rub-compact"),
    ("Whiteboard and record disagree on the surgical site", "Full stop. Nothing gets clipped until the DVM resolves it.", "csc-sur01"),
    ("Clipper blade feels hot", "Swap or cool it, check the skin, report any lesion you find or cause. Concealment is the offense, not the burn.", "csc-sur01"),
    ("How many attempts do I get?", "Two, then hand off — counted per person, not per site or per patient. Anyone may call a stop at any time.", "csc-ven01"),
    ("What can an assistant legally do in Arizona?", "Anything delegated except diagnosis, prognosis, prescription, and surgery — under DVM supervision. CVAH policy may restrict further.", "scope"),
]

# ---------- PHASE A CHECKLIST ----------
GATE = [
    ("Assign the four roles", "Program administrator, medical reviewer (DVM), assessors (CVT/DVM), supervising techs.", "roles", "30 min"),
    ("Approve the reference cards", "Medical director reviews and signs CRC-001, 002, 003, 005. Until signed they stay watermarked and unusable.", None, "2 h"),
    ("Decide the scope policy column", "Especially: may assistants place IV catheters here? Plus IV push, intubation, dental polishing.", "scope", "1 h"),
    ("Verify the statute rows", "Check the scope matrix against current text at vetboard.az.gov and log it.", "scope", "1 h"),
    ("Fill the local-input items", "44 flagged facts and decisions across the curriculum — equipment models, products, protocols.", None, "1 h"),
    ("Run the equipment survey", "Walk the hospital with a phone camera; record analyzer, pump, machine, and imaging models.", None, "1 h"),
    ("Calibrate your assessors", "Two assessors score the same performance and compare. Gaps over 2 points get discussed.", "rub-std", "half day"),
]

payload = {"docs": DOCS, "crc": CRC, "trouble": TROUBLE, "gate": GATE}
data_json = json.dumps(payload, ensure_ascii=False)

groups = ["Start", "Skill courses", "Lessons", "Assess", "Reference", "Run it"]

HTML = """<title>CVAH Veterinary Assistant University</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
:root{
  --ink:#16232b; --ink-2:#41545f; --ink-3:#5c7078;
  --bg:#f4f7f7; --surface:#ffffff; --surface-2:#eef3f3; --line:#d8e3e3; --line-2:#c2d3d3;
  --accent:#0f6b6b; --accent-ink:#0b5252; --accent-wash:#e2efee;
  --warn:#9a6f0d; --warn-bg:#fdf4dd; --warn-line:#e6c76a;
  --stop:#a3322a; --stop-bg:#fbeceb; --stop-line:#e0a49e;
  --ok:#2e7d4f; --ok-bg:#e6f2ea;
  --radius:10px; --maxw:74ch;
  --sans:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ink:#e6eeee; --ink-2:#a8bcc2; --ink-3:#7e949c;
    --bg:#0e1719; --surface:#152225; --surface-2:#1b2b2e; --line:#27383c; --line-2:#33484d;
    --accent:#4fb3ac; --accent-ink:#7fcdc6; --accent-wash:#16302f;
    --warn:#e8c46a; --warn-bg:#2c2410; --warn-line:#6b5720;
    --stop:#f0a49b; --stop-bg:#331917; --stop-line:#7a3b35;
    --ok:#6fc493; --ok-bg:#14291f;
  }
}
:root[data-theme="dark"]{
  --ink:#e6eeee; --ink-2:#a8bcc2; --ink-3:#7e949c;
  --bg:#0e1719; --surface:#152225; --surface-2:#1b2b2e; --line:#27383c; --line-2:#33484d;
  --accent:#4fb3ac; --accent-ink:#7fcdc6; --accent-wash:#16302f;
  --warn:#e8c46a; --warn-bg:#2c2410; --warn-line:#6b5720;
  --stop:#f0a49b; --stop-bg:#331917; --stop-line:#7a3b35;
  --ok:#6fc493; --ok-bg:#14291f;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);
  font-size:16px;line-height:1.62;-webkit-text-size-adjust:100%}
a{color:var(--accent-ink);text-underline-offset:2px}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:3px}
code,.id{font-family:var(--mono);font-size:.86em;letter-spacing:-.01em}
.id{color:var(--accent-ink);white-space:nowrap}
code{background:var(--surface-2);padding:.1em .34em;border-radius:4px}

header.top{position:sticky;top:0;z-index:20;background:var(--surface);
  border-bottom:1px solid var(--line);padding:10px 18px;display:flex;gap:14px;align-items:center;flex-wrap:wrap}
.brand{display:flex;flex-direction:column;line-height:1.15;margin-right:auto}
.brand b{font-size:15px;letter-spacing:-.015em}
.brand span{font-size:11px;color:var(--ink-3);text-transform:uppercase;letter-spacing:.1em}
#q{flex:1 1 260px;min-width:180px;max-width:460px;font:inherit;font-size:15px;
  padding:9px 12px;border:1px solid var(--line-2);border-radius:8px;background:var(--bg);color:var(--ink)}
#q::placeholder{color:var(--ink-3)}
.pill{font-family:var(--mono);font-size:11px;padding:4px 9px;border-radius:999px;white-space:nowrap;
  border:1px solid var(--warn-line);background:var(--warn-bg);color:var(--warn)}

.wrap{display:grid;grid-template-columns:238px minmax(0,1fr);gap:0;align-items:start}
nav{position:sticky;top:59px;max-height:calc(100vh - 59px);overflow-y:auto;
  padding:16px 10px 40px;border-right:1px solid var(--line)}
nav h3{font-size:10.5px;text-transform:uppercase;letter-spacing:.13em;color:var(--ink-3);
  margin:16px 8px 5px;font-weight:600}
nav h3:first-child{margin-top:0}
nav button{display:block;width:100%;text-align:left;background:none;border:0;color:var(--ink-2);
  font:inherit;font-size:13.5px;padding:5px 9px;border-radius:6px;cursor:pointer;line-height:1.35}
nav button:hover{background:var(--surface-2);color:var(--ink)}
nav button[aria-current="true"]{background:var(--accent-wash);color:var(--accent-ink);font-weight:600}
nav .meta{display:block;font-family:var(--mono);font-size:10px;color:var(--ink-3);margin-top:1px}

main{padding:26px 30px 90px;min-width:0}
.doc{max-width:var(--maxw)}
.doc.wide{max-width:100%}
h1.page{font-size:27px;letter-spacing:-.022em;margin:0 0 4px;text-wrap:balance;line-height:1.2}
.sub{color:var(--ink-3);font-size:12.5px;margin:0 0 22px;font-family:var(--mono);letter-spacing:.01em}
.lead{color:var(--ink-2);font-size:15.5px;margin:0 0 22px;max-width:66ch;line-height:1.6}
.doc h2{font-size:19px;letter-spacing:-.015em;margin:30px 0 8px;text-wrap:balance;
  padding-bottom:5px;border-bottom:1px solid var(--line)}
.doc h3{font-size:15.5px;margin:22px 0 5px;color:var(--ink);text-wrap:balance}
.doc h4,.doc h5,.doc h6{font-size:14px;margin:16px 0 4px;color:var(--ink-2)}
.doc p{margin:.6em 0}
.doc ul,.doc ol{margin:.5em 0;padding-left:1.35em}
.doc li{margin:.24em 0}
.doc hr{border:0;border-top:1px solid var(--line);margin:24px 0}
.doc blockquote{margin:.8em 0;padding:.5em 0 .5em 14px;border-left:3px solid var(--accent);
  color:var(--ink-2);background:var(--accent-wash);border-radius:0 6px 6px 0}
.tw{overflow-x:auto;margin:14px 0;border:1px solid var(--line);border-radius:var(--radius);background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:13.5px}
th,td{text-align:left;padding:8px 11px;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--surface-2);font-size:11px;text-transform:uppercase;letter-spacing:.07em;
  color:var(--ink-2);font-weight:600;white-space:nowrap}
tbody tr:last-child td{border-bottom:0}
td{font-variant-numeric:tabular-nums}

.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:16px 18px;margin:14px 0}
.grid{display:grid;gap:12px;margin:16px 0}
@media(min-width:700px){.grid.two{grid-template-columns:1fr 1fr}.grid.four{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1050px){.grid.four{grid-template-columns:repeat(4,1fr)}}
.rolecard{background:var(--surface);border:1px solid var(--line);border-left:3px solid var(--accent);
  border-radius:var(--radius);padding:14px 16px;cursor:pointer;text-align:left;font:inherit;color:inherit;width:100%}
.rolecard:hover{border-color:var(--line-2);border-left-color:var(--accent);background:var(--surface-2)}
.rolecard b{display:block;font-size:14.5px;margin-bottom:3px}
.rolecard span{font-size:13px;color:var(--ink-2);line-height:1.5}

.banner{border-radius:var(--radius);padding:14px 16px;margin:0 0 20px;border:1px solid}
.banner.warn{background:var(--warn-bg);border-color:var(--warn-line);color:var(--warn)}
.banner.stop{background:var(--stop-bg);border-color:var(--stop-line);color:var(--stop)}
.banner b{display:block;margin-bottom:3px;font-size:14px}
.banner p{margin:0;font-size:13.5px;line-height:1.55}

ol.gate{list-style:none;padding:0;margin:16px 0;counter-reset:g}
ol.gate li{counter-increment:g;display:flex;gap:12px;align-items:flex-start;background:var(--surface);
  border:1px solid var(--line);border-radius:var(--radius);padding:12px 14px;margin-bottom:8px}
ol.gate li::before{content:counter(g);font-family:var(--mono);font-size:11px;color:var(--accent-ink);
  background:var(--accent-wash);width:22px;height:22px;border-radius:50%;display:grid;place-items:center;flex:0 0 22px;margin-top:2px}
ol.gate input{width:17px;height:17px;margin-top:4px;accent-color:var(--accent);flex:0 0 17px;cursor:pointer}
ol.gate .g-b{flex:1;min-width:0}
ol.gate b{display:block;font-size:14px}
ol.gate p{margin:2px 0 0;font-size:13px;color:var(--ink-2)}
ol.gate .t{font-family:var(--mono);font-size:11px;color:var(--ink-3);white-space:nowrap;margin-top:3px}
ol.gate li.done b{text-decoration:line-through;color:var(--ink-3)}
.prog{height:5px;background:var(--surface-2);border-radius:99px;overflow:hidden;margin:6px 0 0}
.prog i{display:block;height:100%;background:var(--accent);transition:width .3s}

.tlist{margin:14px 0;display:grid;gap:7px}
.trow{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);
  padding:11px 14px;cursor:pointer;text-align:left;font:inherit;color:inherit;width:100%;display:block}
.trow:hover{background:var(--surface-2);border-color:var(--line-2)}
.trow b{display:block;font-size:14px;margin-bottom:2px}
.trow span{font-size:13px;color:var(--ink-2);line-height:1.5}
.trow em{display:block;font-family:var(--mono);font-size:10.5px;color:var(--ink-3);font-style:normal;margin-top:5px}

.crc{border:1px solid var(--stop-line);border-radius:var(--radius);margin:14px 0;overflow:hidden;background:var(--surface)}
.crc .h{background:var(--stop-bg);color:var(--stop);padding:11px 15px;font-size:14px;font-weight:600;
  display:flex;justify-content:space-between;gap:10px;align-items:center;flex-wrap:wrap}
.crc .h .tag{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em}
.crc .body{padding:2px 16px 14px;display:none}
.crc.open .body{display:block}
.crc .body::before{content:"UNAPPROVED DRAFT — NOT FOR CLINICAL USE";display:block;font-family:var(--mono);
  font-size:10.5px;letter-spacing:.09em;color:var(--stop);background:var(--stop-bg);
  padding:6px 10px;border-radius:6px;margin:12px 0}
button.rev{font:inherit;font-size:12.5px;font-family:var(--mono);background:var(--surface);color:var(--stop);
  border:1px solid var(--stop-line);border-radius:6px;padding:5px 11px;cursor:pointer}
button.rev:hover{background:var(--stop-bg)}

#results{margin:0 0 18px}
.res{display:block;width:100%;text-align:left;font:inherit;color:inherit;background:var(--surface);
  border:1px solid var(--line);border-radius:var(--radius);padding:11px 14px;margin-bottom:7px;cursor:pointer}
.res:hover{background:var(--surface-2)}
.res b{font-size:14px}
.res .g{font-family:var(--mono);font-size:10.5px;color:var(--ink-3);margin-left:7px}
.res p{margin:3px 0 0;font-size:13px;color:var(--ink-2);line-height:1.5}
.res mark{background:var(--warn-bg);color:inherit;padding:0 2px;border-radius:2px}
.empty{color:var(--ink-3);font-size:14px;padding:14px 0}

.tools{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 18px}
.tools button{font:inherit;font-size:12.5px;background:var(--surface);color:var(--ink-2);
  border:1px solid var(--line-2);border-radius:7px;padding:6px 12px;cursor:pointer}
.tools button:hover{background:var(--surface-2);color:var(--ink)}
.navtoggle{display:none}

@media(max-width:860px){
  .wrap{grid-template-columns:1fr}
  nav{position:static;max-height:none;border-right:0;border-bottom:1px solid var(--line);display:none}
  nav.open{display:block}
  .navtoggle{display:inline-block;font:inherit;font-size:12.5px;background:var(--surface);
    border:1px solid var(--line-2);color:var(--ink-2);border-radius:7px;padding:7px 12px;cursor:pointer}
  main{padding:20px 16px 70px}
  h1.page{font-size:23px}
}
@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
@media print{
  header.top,nav,.tools,#results{display:none!important}
  .wrap{display:block}
  main{padding:0}
  body{background:#fff;color:#000;font-size:11pt}
  .doc{max-width:none}
  .card,.tw,.crc{break-inside:avoid}
  a{text-decoration:none;color:#000}
}
</style>

<header class="top">
  <div class="brand"><b>CVAH Veterinary Assistant University</b><span>Learn it · Practice it · Prove it · Use it</span></div>
  <input id="q" type="search" placeholder="Search everything — try &quot;won't thread&quot; or &quot;flat capnograph&quot;" autocomplete="off" aria-label="Search the university">
  <span class="pill" id="statuspill">4 cards await DVM sign-off</span>
  <button class="navtoggle" id="navtoggle" aria-expanded="false">Menu</button>
</header>

<div class="wrap">
  <nav id="nav" aria-label="Sections"></nav>
  <main>
    <div id="results" hidden></div>
    <div id="view"></div>
  </main>
</div>

<script>
const DATA = __DATA__;
const $ = s => document.querySelector(s);
const byId = Object.fromEntries(DATA.docs.map(d => [d.id, d]));
const GROUPS = __GROUPS__;

/* ---------- navigation ---------- */
function buildNav(){
  const n = $('#nav'); n.innerHTML = '';
  GROUPS.forEach(g => {
    const items = g === 'Start'
      ? [{id:'start',title:'Start here',meta:'first 5 hours'},{id:'find',title:'Find it fast',meta:'symptom index'},{id:'passport',title:'Passport states',meta:'1 → 14'}]
      : g === 'Reference' ? [{id:'cards',title:'Clinical reference cards',meta:'gated'}]
      : DATA.docs.filter(d => d.group === g);
    if(!items.length) return;
    const h = document.createElement('h3'); h.textContent = g; n.appendChild(h);
    items.forEach(d => {
      const b = document.createElement('button');
      b.dataset.id = d.id;
      b.innerHTML = esc(d.title) + (d.meta ? '<span class="meta">'+esc(d.meta)+'</span>' : '');
      b.onclick = () => show(d.id);
      n.appendChild(b);
    });
  });
}
function esc(s){const d=document.createElement('div');d.textContent=s;return d.innerHTML}

/* ---------- built pages ---------- */
function startPage(){
  const done = JSON.parse(localStorage.getItem('cvah_gate') || '[]');
  const pct = Math.round(done.length / DATA.gate.length * 100);
  return `<div class="doc">
  <h1 class="page">Start here</h1>
  <p class="lead">Nothing clinical goes live until a veterinarian signs. That is roughly five hours of work.</p>
  <div class="banner warn"><b>Current state: usable for training, not yet cleared for clinical numbers</b>
  <p>Every lesson, skill course, rubric and case log below is ready to use today. The four controlled reference cards carry draft values and stay watermarked until your medical director approves them. The Arizona scope rows need verification against current statute text before anyone acts on them.</p></div>

  <h2>The five hours that gate everything</h2>
  <div class="prog"><i style="width:${pct}%"></i></div>
  <ol class="gate">${DATA.gate.map((g,i)=>{
    const isDone = done.includes(i);
    return `<li class="${isDone?'done':''}" data-i="${i}">
      <input type="checkbox" ${isDone?'checked':''} aria-label="Mark complete">
      <div class="g-b"><b>${esc(g[0])}</b><p>${esc(g[1])}</p>
      ${g[2]?`<div class="t">→ <a href="#" data-go="${g[2]}">open the document</a></div>`:''}</div>
      <div class="t">${esc(g[3])}</div></li>`;
  }).join('')}</ol>

  <h2>Then start someone on Monday</h2>
  <div class="grid two">
    <div class="card"><b>With no technology at all</b>
      <p style="font-size:13.5px;color:var(--ink-2);margin:.4em 0 0">Print the Week 0 and Week 1 lessons, the restraint and TPR skill courses, their two rubrics, and the pocket case-log card. That is a complete first fortnight. Use the print button on any page.</p></div>
    <div class="card"><b>When you want the LMS</b>
      <p style="font-size:13.5px;color:var(--ink-2);margin:.4em 0 0">Moodle, roughly $10–50 a month. Import Weeks 0–2 first and pilot before loading the rest. The content lives in the repository either way — the LMS is a delivery layer.</p></div>
  </div>

  <h2>Who are you today?</h2>
  <div class="grid four">
    <button class="rolecard" data-go="lsn-w0-01"><b>New hire</b><span>Start at W0-01, then the Week 1 lessons in order.</span></button>
    <button class="rolecard" data-go="rub-std"><b>Assessor</b><span>Scoring standards, then the rubric for the skill you are observing.</span></button>
    <button class="rolecard" data-go="workload"><b>Manager</b><span>What workload transfers at each sign-off, and the nine graduation gates.</span></button>
    <button class="rolecard" data-go="cards"><b>Medical director</b><span>The four cards awaiting your signature, plus the scope matrix rows.</span></button>
  </div>

  <h2>The rule that keeps this honest</h2>
  <blockquote>Graduation is nine gates, not eight weeks. The moment someone graduates a learner because Week 8 arrived, this becomes an ordinary onboarding packet with extra paperwork.</blockquote>
  </div>`;
}

function findPage(){
  return `<div class="doc">
  <h1 class="page">Find it fast</h1>
  <p class="lead">Symptom in, answer out. Tap any row for the full course.</p>
  <div class="tlist">${DATA.trouble.map(t=>`<button class="trow" data-go="${t[2]}">
    <b>${esc(t[0])}</b><span>${esc(t[1])}</span><em>${esc((byId[t[2]]||{}).title||t[2])}</em></button>`).join('')}</div></div>`;
}

const STATES = [["Not introduced",""],["Theory assigned",""],["Theory complete","knowledge check passed"],
["Demonstration observed",""],["Practicing with direct supervision","S1"],["Repetition requirement in progress","case log accruing"],
["Practical assessment ready","trainer flags"],["Practical assessment passed","assessor signs"],
["Competent under defined supervision","consolidation"],["Independently assignable within hospital policy","assessor + DVM"],
["Remediation required",""],["Revalidation due",""],["Temporarily restricted","DVM review ≤48 h"],["Competency expired",""]];
function passportPage(){
  return `<div class="doc"><h1 class="page">Passport states</h1>
  <p class="lead">Every skill, every employee, one state at a time. States 1–10 are the ladder; 11–14 are the exits.</p>
  <div class="banner warn"><b>The word "independent" never appears alone</b><p>State 10 reads "independently assignable within hospital policy" and always displays alongside its supervision level and scope class. Nothing here changes anyone's legal scope of practice.</p></div>
  <div class="tw"><table><thead><tr><th>#</th><th>State</th><th>Set by / note</th></tr></thead><tbody>
  ${STATES.map((s,i)=>`<tr><td><span class="id">${i+1}</span></td><td>${esc(s[0])}</td><td>${esc(s[1])}</td></tr>`).join('')}
  </tbody></table></div>
  <p style="font-size:13.5px;color:var(--ink-2)">Promotion to state 8 requires a passed rubric with zero critical fails. Promotion to state 10 requires an assessor and a veterinarian together. Any veterinarian may drop a skill to state 13 immediately.</p></div>`;
}

function cardsPage(){
  return `<div class="doc"><h1 class="page">Clinical reference cards</h1>
  <p class="lead">All high-risk numbers live here, versioned and signed — never scattered through lessons.</p>
  <div class="banner stop"><b>These four cards are drafts and must not be used clinically</b>
  <p>The values below were drafted from cited sources as a starting point for your medical director to correct, adjust to this hospital's population, and sign. Until that signature exists they are study material only. Open each card deliberately.</p></div>
  ${DATA.crc.map((c,i)=>`<div class="crc" data-c="${i}">
    <div class="h"><span>${esc(c.title)}</span><span class="tag">PENDING DVM SIGN-OFF</span></div>
    <div style="padding:11px 15px"><button class="rev" data-rev="${i}">Show unapproved draft values</button></div>
    <div class="body">${c.html}</div></div>`).join('')}
  <div class="card"><b>What "approved" will look like</b>
  <p style="font-size:13.5px;color:var(--ink-2);margin:.4em 0 0">Each card carries version, approval date, reviewing veterinarian, sources, and next review date. A card past its review date automatically flags as expired on dashboards and gets pulled from the walls.</p></div></div>`;
}

/* ---------- render ---------- */
function show(id, scrollTo){
  const v = $('#view');
  if(id === 'start') v.innerHTML = startPage();
  else if(id === 'find') v.innerHTML = findPage();
  else if(id === 'passport') v.innerHTML = passportPage();
  else if(id === 'cards') v.innerHTML = cardsPage();
  else {
    const d = byId[id]; if(!d) return;
    v.innerHTML = `<div class="tools">
      <button data-print>Print this page</button>
      <button data-back>← All sections</button></div>
      <div class="doc ${d.group==='Assess'||d.group==='Run it'?'wide':''}">
      <h1 class="page">${esc(d.title)}</h1>
      <p class="sub">${esc(d.group)}${d.meta?' · '+esc(d.meta):''}</p>${d.html}</div>`;
  }
  document.querySelectorAll('nav button').forEach(b =>
    b.setAttribute('aria-current', b.dataset.id === id ? 'true' : 'false'));
  $('#nav').classList.remove('open');
  $('#navtoggle').setAttribute('aria-expanded','false');
  window.scrollTo(0,0);
  if(scrollTo){
    const needle = scrollTo.toLowerCase();
    for(const el of v.querySelectorAll('p,li,td,h2,h3,blockquote')){
      if(el.textContent.toLowerCase().includes(needle)){ el.scrollIntoView({block:'center'});
        el.style.background='var(--warn-bg)'; el.style.borderRadius='4px'; break; }
    }
  }
}

/* ---------- search ---------- */
function snippet(text, q){
  const needle = q.toLowerCase();
  const i = text.toLowerCase().indexOf(needle);
  const s = i < 0 ? 0 : Math.max(0, i - 60);
  const end = i < 0 ? 150 : i + q.length + 110;
  let rest = (s ? '…' : '') + text.slice(s, end) + '…', out = '';
  while(needle){
    const k = rest.toLowerCase().indexOf(needle);
    if(k < 0) break;
    out += esc(rest.slice(0,k)) + '<mark>' + esc(rest.slice(k, k + q.length)) + '</mark>';
    rest = rest.slice(k + q.length);
  }
  return out + esc(rest);
}
function search(q){
  const box = $('#results');
  if(q.trim().length < 2){ box.hidden = true; box.innerHTML = ''; return; }
  const needle = q.trim().toLowerCase();
  const hits = [];
  DATA.trouble.forEach(t => {
    if((t[0]+' '+t[1]).toLowerCase().includes(needle))
      hits.push({id:t[2], title:t[0], group:'Find it fast', snip:snippet(t[1], q.trim()), q:t[0]});
  });
  DATA.docs.forEach(d => {
    const inTitle = d.title.toLowerCase().includes(needle);
    const at = d.text.toLowerCase().indexOf(needle);
    if(inTitle || at >= 0)
      hits.push({id:d.id, title:d.title, group:d.group, snip:snippet(d.text, q.trim()), q:q.trim(), rank:inTitle?0:1});
  });
  hits.sort((a,b)=>(a.rank??0)-(b.rank??0));
  box.hidden = false;
  box.innerHTML = hits.length
    ? `<p class="sub">${hits.length} match${hits.length>1?'es':''} for “${esc(q.trim())}”</p>` +
      hits.slice(0,40).map(h=>`<button class="res" data-go="${h.id}" data-q="${esc(h.q)}">
        <b>${esc(h.title)}</b><span class="g">${esc(h.group)}</span><p>${h.snip}</p></button>`).join('')
    : `<p class="empty">Nothing matches “${esc(q.trim())}”. Try a symptom in plain words — “swollen leg”, “no flash”, “alarm”.</p>`;
}

/* ---------- events ---------- */
document.addEventListener('click', e => {
  const go = e.target.closest('[data-go]');
  if(go){ e.preventDefault();
    if(go.classList.contains('res')){ const b=$('#results'); b.hidden=true; b.innerHTML=''; }
    show(go.dataset.go, go.dataset.q); return; }
  if(e.target.closest('[data-print]')){ window.print(); return; }
  if(e.target.closest('[data-back]')){ show('start'); return; }
  const rev = e.target.closest('[data-rev]');
  if(rev){ rev.closest('.crc').classList.add('open'); rev.remove(); return; }
  const gate = e.target.closest('ol.gate input');
  if(gate){
    const li = gate.closest('li'), i = +li.dataset.i;
    let done = JSON.parse(localStorage.getItem('cvah_gate') || '[]');
    done = gate.checked ? [...new Set([...done, i])] : done.filter(x => x !== i);
    localStorage.setItem('cvah_gate', JSON.stringify(done));
    li.classList.toggle('done', gate.checked);
    const pct = Math.round(done.length / DATA.gate.length * 100);
    const bar = document.querySelector('.prog i'); if(bar) bar.style.width = pct + '%';
  }
});
$('#q').addEventListener('input', e => search(e.target.value));
$('#q').addEventListener('focus', e => { if(e.target.value.trim().length>1 && $('#results').hidden) search(e.target.value); });
$('#navtoggle').addEventListener('click', e => {
  const n = $('#nav'), open = n.classList.toggle('open');
  e.target.setAttribute('aria-expanded', String(open));
});
document.addEventListener('keydown', e => {
  if(e.key === '/' && document.activeElement !== $('#q')){ e.preventDefault(); $('#q').focus(); }
  if(e.key === 'Escape'){ $('#q').value = ''; search(''); }
});

buildNav();
show('start');
</script>
"""

HTML = HTML.replace("__DATA__", data_json).replace("__GROUPS__", json.dumps(groups))
with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print("wrote", OUT, round(len(HTML)/1024), "KB")
print("docs:", len(DOCS), "| trouble:", len(TROUBLE), "| crc:", len(CRC))
