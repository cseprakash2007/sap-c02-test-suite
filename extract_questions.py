"""Rebuild src/data/questions.json from the original uploaded SAP-C02 PDF.
Requires pip install pymupdf. Keep the original source private and check its licensing.
"""
import fitz,re,json,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parent
pdf=Path('/mnt/data/SAP-C02V33.2.pdf')
if not pdf.exists():
    raise SystemExit('Place SAP-C02V33.2.pdf at /mnt/data/SAP-C02V33.2.pdf or update pdf variable.')
t='\n'.join(p.get_text() for p in fitz.open(pdf))
t=re.sub(r'(?m)^\s*Certify For Sure with IT Exam Dumps\nThe No.1 IT Certification Dumps\n\d+\n','\n',t)
# Question numbering in the source is sequential; avoid false matches in option text.
allstarts=list(re.finditer(r'(?m)^(\d{1,3})\.\s',t))
starts=[]; expected=1
for m in allstarts:
    if int(m.group(1))==expected:
        starts.append(m);expected+=1
assert expected==675,(expected,len(starts))
# Recover prior domain grouping without inferring official AWS domains.
domains={}
for d in range(1,5):
    p=Path(f'/mnt/data/SAP-C02_Domain_{d}_Desktop.pdf')
    if not p.exists():continue
    for page in fitz.open(p):
        m=re.search(r'(?im)^\s*Question\s+(\d+)\s*\|\s*SAP-C02|^\s*QUESTION\s+(\d+)\s*$',page.get_text())
        if m:domains[int(m.group(1) or m.group(2))]=d
# Q1-100 explanations as written in earlier study guide (not independently verified).
notes={}
prior=Path('/mnt/data/SAP-C02_Q001-100_Desktop_Aligned_Draft.pdf')
if prior.exists():
    heads=['IN PLAIN WORDS','WHY THE CORRECT ANSWER WORKS','WHY THE OTHER OPTIONS FAIL','REMEMBER','HEADS-UP']
    for page in fitz.open(prior):
        x=page.get_text();q=re.search(r'(?m)^QUESTION\s+(\d+)\s*$',x)
        if not q:continue
        info={}
        for i,h in enumerate(heads):
            pattern=r'(?m)^'+re.escape(h)+r'\s*$'
            z=re.search(pattern,x)
            if not z:continue
            nxt=[k.start() for other in heads for k in [re.search(r'(?m)^'+re.escape(other)+r'\s*$',x[z.end():])] if k] # unused
            remaining=x[z.end():]
            bounds=[m.start() for other in heads for m in re.finditer(r'(?m)^'+re.escape(other)+r'\s*$',remaining)]
            info[h]=remaining[:min(bounds) if bounds else len(remaining)].strip()
        notes[int(q.group(1))]=info
# Preliminary review already written into earlier PDFs; keep distinction from source answer.
review={
101:('Supported','Compute Savings Plans cover EC2, Fargate, and Lambda. Savings depend on a stable usage baseline.','https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html'),
102:('Needs further validation','DataSync cross-Region private networking and endpoint placement are not specified sufficiently to independently confirm the answer.','https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html'),
103:('Answer key questionable','On-Demand Capacity Reservations guarantee capacity, not discounted pricing. Cheapest design depends on usage and workload assumptions.','https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_pricing_model_analysis.html'),
104:('Supported with caveat','Service Catalog portfolio sharing, launch constraints and TagOptions support the design; option D simplifies administrator responsibilities.','https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_sharing.html'),
105:('Supported','RDS MySQL cross-Region read replicas can be promoted; replication is asynchronous and promotion takes time.','https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.XRgn.html')}
flags={3:'Option D is truncated in the source PDF; do not infer missing text.',12:'Cross-account IAM role answer choices overlap in policy terminology; review the trust policy versus permission policy.',16:'References retired Aurora Serverless v1. Review current Aurora Serverless v2 capabilities.',34:'Source key appears questionable: route tables cannot deny arbitrary attacker IPs.'}
questions=[]
for i,m in enumerate(starts):
    n=int(m.group(1));end=starts[i+1].start() if i+1<len(starts) else len(t)
    block=t[m.end():end].strip()
    am=re.search(r'(?im)^Answer\s*:\s*([^\n]+)',block)
    if not am:raise ValueError(f'Missing answer {n}')
    rawanswer=am.group(1).strip()
    answer=list(dict.fromkeys(re.findall(r'[A-F]',rawanswer.upper())))
    before=block[:am.start()].strip()
    options=list(re.finditer(r'(?m)^([A-F])\.\s',before))
    if len(options)<4:raise ValueError(f'Only {len(options)} choices in {n}')
    stem=re.sub(r'\s+',' ',before[:options[0].start()]).strip()
    choices=[]
    for j,op in enumerate(options):
        value=before[op.end():options[j+1].start() if j+1<len(options) else len(before)]
        choices.append({'id':op.group(1),'text':re.sub(r'\s+',' ',value).strip()})
    extra=notes.get(n,{})
    questions.append({'id':n,'domain':domains.get(n,0),'stem':stem,'options':choices,'answers':answer,'answerCount':len(answer),
       'explanation':extra.get('WHY THE CORRECT ANSWER WORKS',''),
       'wrongOptionsExplanation':extra.get('WHY THE OTHER OPTIONS FAIL',''),
       'plainWords':extra.get('IN PLAIN WORDS',''),
       'keyPoints':extra.get('REMEMBER',''),
       'sourceWarning':flags.get(n,extra.get('HEADS-UP','')),
       'review':dict(status=review[n][0],note=review[n][1],reference=review[n][2]) if n in review else None,
       'answerStatus':'source-key-unverified'})
assert len(questions)==674
assert collections.Counter(q['answerCount'] for q in questions)=={1:539,2:74,3:61}
assert len(domains)==674,len(domains)
out=ROOT/'src/data/questions.json';out.write_text(json.dumps(questions,ensure_ascii=False,indent=1))
print('Saved',out,'questions',len(questions),'domains',collections.Counter(q['domain'] for q in questions),'with explanation',sum(bool(q['explanation']) for q in questions))
