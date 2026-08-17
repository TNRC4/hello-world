#!/usr/bin/env python3
"""Answer-leakage audit for QB-*.md banks: key-position balance + longest-option giveaway."""
import re, glob, statistics
pos = {"A":0,"B":0,"C":0,"D":0}; long_key = 0; total = 0
for f in sorted(glob.glob("14_Question_Banks/QB-*.md")):
    for it in re.split(r"\n### ", open(f).read())[1:]:
        m = re.search(r"^KEY:\s*([A-D])", it, re.M)
        opt = re.search(r"^A\)(.*?)B\)(.*?)C\)(.*?)D\)(.*)$", it, re.M|re.S)
        if not m or not opt: continue
        total += 1; k = m.group(1); pos[k] += 1
        lens = {"A":len(opt.group(1)),"B":len(opt.group(2)),"C":len(opt.group(3)),"D":len(opt.group(4).split("\n")[0])}
        if lens[k]==max(lens.values()) and lens[k] > 1.5*statistics.median(v for kk,v in lens.items() if kk!=k): long_key += 1
print(f"items={total} positions={pos} long-key-giveaways={long_key} ({100*long_key//max(total,1)}%)")
