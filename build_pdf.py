from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, KeepTogether
import yaml

ROOT = Path(__file__).parent
OUT = ROOT / '류연주_1페이지_이력서.pdf'
FONT = 'Malgun'
FONT_BOLD = 'MalgunBold'
pdfmetrics.registerFont(TTFont(FONT, 'C:/Windows/Fonts/malgun.ttf'))
pdfmetrics.registerFont(TTFont(FONT_BOLD, 'C:/Windows/Fonts/malgunbd.ttf'))

ssot = yaml.safe_load((ROOT / 'resume.yaml').read_text(encoding='utf-8'))
cv = ssot['cv']
assert cv['name'] == '류연주' and cv['email'] == '5395640@naver.com', 'resume.yaml SSOT identity mismatch'
experience = cv['sections']['experience']
projects_ssot = cv['sections']['projects']
education = cv['sections']['education'][0]

INK = colors.HexColor('#514B5A')
MUTED = colors.HexColor('#766F7C')
ACCENT = colors.HexColor('#756284')
PAPER = colors.HexColor('#FFF9F5')
PEACH = colors.HexColor('#FFF0EB')
LAV = colors.HexColor('#F1ECFB')
SAGE = colors.HexColor('#EDF7E9')
BLUE = colors.HexColor('#EDF7FC')
LINE = colors.HexColor('#EADDE5')

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Name', fontName=FONT_BOLD, fontSize=25, leading=28, textColor=INK, spaceAfter=3))
styles.add(ParagraphStyle(name='Role', fontName=FONT_BOLD, fontSize=10.5, leading=14, textColor=ACCENT, spaceAfter=3))
styles.add(ParagraphStyle(name='Contact', fontName=FONT, fontSize=7.8, leading=11, textColor=MUTED, alignment=TA_LEFT))
styles.add(ParagraphStyle(name='Axis', fontName=FONT_BOLD, fontSize=7.2, leading=9, textColor=INK, alignment=TA_LEFT))
styles.add(ParagraphStyle(name='H2', fontName=FONT_BOLD, fontSize=10.5, leading=13, textColor=ACCENT, spaceBefore=5, spaceAfter=3))
styles.add(ParagraphStyle(name='H3', fontName=FONT_BOLD, fontSize=8.6, leading=11, textColor=INK, spaceBefore=2, spaceAfter=1))
styles.add(ParagraphStyle(name='Body', fontName=FONT, fontSize=7.7, leading=10.2, textColor=MUTED, spaceAfter=2))
styles.add(ParagraphStyle(name='Small', fontName=FONT, fontSize=6.5, leading=8.2, textColor=MUTED, spaceAfter=1))
styles.add(ParagraphStyle(name='Period', fontName=FONT_BOLD, fontSize=6.8, leading=8.5, textColor=ACCENT, spaceAfter=1))

def P(text, style='Body'):
    return Paragraph(text, styles[style])

def section(title):
    return [P(title, 'H2')]

left = []
left += section('한 줄 소개')
left += [P('국내 전시·MICE 현장에서 전시 기획, 참가사 유치, 현장 운영을 맡아온 전시·행사 프로젝트 코디네이터입니다.')]
left += section('경력')
for job in experience:
    period = f"{job['start_date']} — {('현재' if job['end_date'] == 'present' else job['end_date'])}"
    bullets = '<br/>'.join(job['highlights'])
    left += [P(f"{job['company']} · {job['position']}", 'H3'), P(period, 'Period'), P(bullets)]
left += section('핵심 역량')
skills = cv['sections']['skills'][0]['details']
left += [P(skills)]
left += section('업무 방식')
left += [P('<b>관찰 → 구조화 → 제작 → 현장 적용 → 개선</b>')]

right = []
right += section('포트폴리오 증거')
for index, project in enumerate(projects_ssot):
    body = '<br/>'.join(project['highlights'])
    right += [P(project['name'], 'H3'), P(body)]
    if index == 0:
        right += [P('원본 이력서 자기보고 수치 · 검증 대기: 운영 2명→1명 · 참여율 130% 향상', 'Small')]
right += section('학력·도구')
right += [P(f"{education['institution']} · {education['area']} · {education['degree']}"), P('PowerPoint · Excel · Word · 한컴오피스 · Claude · Codex · ChatGPT · Gemini · SNS 활용')]
right += section('포트폴리오')
right += [P('jjujjuya1226-cmd.github.io/recruit/', 'Small')]

doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=14*mm, leftMargin=14*mm, topMargin=12*mm, bottomMargin=10*mm, title='류연주 1페이지 이력서', author='류연주')
story = []
header = Table([[P(cv['name'], 'Name'), P(f"{cv['location']} · {cv['email']}<br/>전시·MICE · 고객경험 · 디지털 운영 개선", 'Contact')]], colWidths=[110*mm, 70*mm])
header.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'BOTTOM'), ('LINEBELOW',(0,0),(-1,-1),1.4,ACCENT), ('BOTTOMPADDING',(0,0),(-1,-1),7), ('LEFTPADDING',(0,0),(-1,-1),0), ('RIGHTPADDING',(0,0),(-1,-1),0)]))
story.append(header)
story.append(Spacer(1, 6))
axis = Table([[P('EVENT OPERATIONS','Axis'), P('CONTENT & CUSTOMER JOURNEY','Axis'), P('DIGITAL OPERATIONS IMPROVEMENT','Axis')]], colWidths=[60*mm,60*mm,60*mm])
axis.setStyle(TableStyle([('BACKGROUND',(0,0),(0,0),PEACH),('BACKGROUND',(1,0),(1,0),LAV),('BACKGROUND',(2,0),(2,0),SAGE),('BOX',(0,0),(-1,-1),0.4,LINE),('INNERGRID',(0,0),(-1,-1),0.4,LINE),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7)]))
story.append(axis)
story.append(Spacer(1, 5))
columns = Table([[left, right]], colWidths=[92*mm,88*mm])
columns.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBEFORE',(1,0),(1,0),0.6,LINE),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(0,0),9),('LEFTPADDING',(1,0),(1,0),10),('RIGHTPADDING',(1,0),(1,0),0)]))
story.append(columns)
doc.build(story)
print(OUT)
