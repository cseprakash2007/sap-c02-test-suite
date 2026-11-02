#!/usr/bin/env python3
"""Generate domain-wise study PDFs from src/data/questions.json."""
import json, os, re
from html import escape
from collections import Counter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.graphics.shapes import Drawing, Rect, String, Line
DATA="src/data/questions.json"
OUT="study-guides"
os.makedirs(OUT,exist_ok=True)
questions=json.load(open(DATA,encoding="utf-8"))
qs=[q for q in questions if int(q.get("answerCount",len(q.get("answers",[]))))>1]
assert len(qs)==135, f"Expected 135, got {len(qs)}"
S=getSampleStyleSheet()
S.add(ParagraphStyle(name="CoverBigX",parent=S["Title"],fontSize=23,leading=30,spaceAfter=20,textColor=colors.HexColor("#15375D")))
S.add(ParagraphStyle(name="QuestionX",parent=S["Heading2"],fontSize=13,leading=18,spaceBefore=13,spaceAfter=10,textColor=colors.HexColor("#17365D")))
S.add(ParagraphStyle(name="BodyX",parent=S["BodyText"],fontSize=9,leading=13.5,spaceAfter=8))
S.add(ParagraphStyle(name="OptionX",parent=S["BodyText"],fontSize=8.8,leading=12.5,leftIndent=10,spaceAfter=7))
S.add(ParagraphStyle(name="SmallX",parent=S["BodyText"],fontSize=8,leading=11,spaceAfter=6,textColor=colors.HexColor("#4A5360")))
domain_names={1:"Organizational Complexity",2:"New Solutions",3:"Continuous Improvement",4:"Migration and Modernization"}
def safe(x):
 return escape(str(x or "")).replace("\\n","<br/>").replace("\n","<br/>")
def para(t,style="BodyX"):return Paragraph(t,S[style])
def diagram(q):
 t=(q.get("stem","")+" "+q.get("explanation","")).lower()
 if "organizations" in t or "scp" in t:
  n=[("Management","billing + governance"),("Organizations","OUs and SCPs"),("Accounts","IAM grants access")]
 elif "direct connect" in t or "vpn" in t or "drs" in t:
  n=[("On premises","source network"),("Private link","DX / VPN as needed"),("AWS VPC","target resources")]
 elif "s3" in t:
  n=[("Clients","application calls"),("Amazon S3","storage controls"),("AWS services","integration")]
 elif "lambda" in t or "api gateway" in t:
  n=[("Clients","requests"),("API / Events","entry point"),("Compute","Lambda / services")]
 elif "rds" in t or "database" in t:
  n=[("Applications","read / write"),("Network","security + routing"),("Database","storage / replicas")]
 elif "cloudformation" in t or "service catalog" in t:
  n=[("Governance","approved products"),("Deployment","templates / roles"),("Resources","accounts / regions")]
 else:
  n=[("Requirement","business constraint"),("AWS design","selected services"),("Outcome","evaluate tradeoffs")]
 d=Drawing(505,87)
 w=153
 for i,(a,b) in enumerate(n):
  x=i*176
  d.add(Rect(x,20,w,53,rx=7,ry=7,strokeColor=colors.HexColor("#6688AE"),fillColor=colors.HexColor("#E9F2FA")))
  d.add(String(x+w/2,52,a,fontName="Helvetica-Bold",fontSize=9,textAnchor="middle"))
  d.add(String(x+w/2,36,b,fontSize=7,textAnchor="middle"))
  if i<2:d.add(Line(x+w+3,46,x+w+19,46,strokeColor=colors.HexColor("#4C688D"),strokeWidth=2))
 return d
def header_footer(canv,doc):
 canv.saveState();canv.setStrokeColor(colors.HexColor("#D6DFE8"));canv.line(46,45,566,45)
 canv.setFillColor(colors.HexColor("#64748B"));canv.setFont("Helvetica",8)
 canv.drawString(46,31,"AWS SAP-C02  |  Multi-answer question study guide")
 canv.drawRightString(566,31,f"Page {doc.page}")
 canv.restoreState()
def question_section(q,pos,total):
 parts=[]
 answers=[str(x) for x in q.get("answers",[])]
 review=q.get("review") or {}
 parts.append(para(f"Q{q['id']}  |  {pos} of {total}  |  Select {q.get('answerCount',len(answers))}","QuestionX"))
 parts.append(para(safe(q.get("stem",""))))
 for opt in q.get("options",[]):
  label=str(opt.get("id","?"))
  marker="<font color='#157347'><b>ANSWER</b></font> " if label in answers else ""
  parts.append(para("<b>"+safe(label)+".</b> "+marker+safe(opt.get("text","")),"OptionX"))
 parts.append(para("<b>Dataset answer key: "+", ".join(answers)+"</b>"))
 if q.get("plainWords"):parts.append(para("<b>In plain English:</b> "+safe(q["plainWords"])))
 if q.get("explanation"):parts.append(para("<b>Why the selected answers work:</b> "+safe(q["explanation"])))
 else:parts.append(para("<b>Study note:</b> No dedicated correct-answer explanation supplied in the source dataset; independently verify before relying on this key."))
 parts.append(para("<b>Conceptual architecture diagram (illustrative; not a complete implementation)</b>","SmallX"))
 parts.append(diagram(q))
 reasons=review.get("wrongOptionsReason") or {}
 if reasons:
  for opt in q.get("options",[]):
   letter=str(opt.get("id",""))
   if letter in reasons:parts.append(para("<b>Option "+safe(letter)+":</b> "+safe(reasons[letter]),"OptionX"))
 if q.get("wrongOptionsExplanation"):parts.append(para("<b>Why other choices fail (source notes):</b> "+safe(q["wrongOptionsExplanation"])))
 if q.get("keyPoints"):parts.append(para("<b>Exam takeaways:</b> "+safe(q["keyPoints"])))
 flags=[]
 if q.get("answerStatus"):flags.append("Answer status: "+str(q["answerStatus"]))
 if q.get("sourceWarning"):flags.append(str(q["sourceWarning"]))
 if review.get("auditNote"):flags.append(str(review["auditNote"]))
 if flags:parts.append(para("<b>Audit notes / limitations:</b> "+safe(" | ".join(flags)),"SmallX"))
 links=review.get("awsDocumentationLinks") or review.get("references") or []
 if links:parts.append(para("<b>AWS reference links:</b> "+safe(" ; ".join(links[:6])),"SmallX"))
 if review.get("externalQuestionLinks"):parts.append(para("<b>External variants:</b> "+safe(" ; ".join(review["externalQuestionLinks"][:3])),"SmallX"))
 parts.append(Spacer(1,12))
 return parts
def make_pdf(path,domains):
 story=[Spacer(1,75),para("AWS SAP-C02 | Multi-Answer Study Guide","CoverBigX"),para("Domain-wise questions, all original options, source explanations, exam notes and conceptual diagrams."),Spacer(1,20)]
 counts=Counter(q["domain"] for q in qs)
 for d in domains:story.append(para(f"Domain {d}: {domain_names[d]} — {counts[d]} questions"))
 story.append(Spacer(1,22))
 story.append(para("<b>Important verification note:</b> The answer key and explanations are sourced from the GitHub dataset. They are not all independently verified. Review statuses and warnings are preserved. Diagrams illustrate concepts; they do not establish answer correctness.","SmallX"))
 story.append(para("Source branch: answer-audit-2026-10-28 | Repository: cseprakash2007/sap-c02-test-suite","SmallX"))
 for d in domains:
  group=sorted((q for q in qs if q["domain"]==d),key=lambda q:q["id"])
  story.append(PageBreak())
  story.append(para(f"Domain {d}: {domain_names[d]}","CoverBigX"))
  story.append(para(f"{len(group)} multi-answer questions. Questions are ordered by original dataset ID."))
  for pos,q in enumerate(group,1):
   story.append(PageBreak())
   story.extend(question_section(q,pos,len(group)))
 pdf=SimpleDocTemplate(path,pagesize=letter,rightMargin=46,leftMargin=46,topMargin=48,bottomMargin=56,title="AWS SAP-C02 Multi-Answer Study Guide")
 pdf.build(story,onFirstPage=header_footer,onLaterPages=header_footer)
for d in range(1,5):
 make_pdf(f"{OUT}/SAP-C02_Domain-{d}_Multi-Answer.pdf",[d])
make_pdf(f"{OUT}/SAP-C02_All-135_Multi-Answer_Domain-Wise.pdf",[1,2,3,4])
print("Generated all five study PDFs")
