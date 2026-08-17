# Question Bank Format Specification

Canonical banks live here as Markdown (one file per domain), portable and reviewable. Deployment: converted to Moodle GIFT/XML by `20_LMS/` tooling (regex-friendly format below is designed for that).

## Item format
```
### <ID> | <Skill/Obj ID> | D<1-3> | <Recall|Apply|Analyze> | SC:<Y|N>
Q: <stem>
A) ... B) ... C) ... D) ...
KEY: <letter> — <explanation>. [DIST: <distractor rationale when non-obvious>]
```
SC:Y = safety-critical (must-be-correct on passing attempts; 100% rule). Source default: the bound skill spec / lesson references; item-specific sources noted inline. All SC items require Medical Reviewer sign-off before entering exam pools (workflow doc). Bank sizes at launch and growth targets tracked in the manifest.
