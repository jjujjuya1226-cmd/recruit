from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
from pathlib import Path

ROOT = Path(__file__).parent
pdfmetrics.registerFont(TTFont('Malgun', 'C:/Windows/Fonts/malgun.ttf'))
pdfmetrics.registerFont(TTFont('MalgunBold', 'C:/Windows/Fonts/malgunbd.ttf'))
out = ROOT / '류연주_메쎄이상_전시기획및운영_이력서.pdf'
doc = SimpleDocTemplate(str(out), pagesize=A4, rightMargin=18*mm, leftMargin=18*mm, topMargin=16*mm, bottomMargin=16*mm, title='류연주 이력서 - 전시기획 및 운영', author='류연주')
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='NameK', fontName='MalgunBold', fontSize=25, leading=31, textColor=colors.HexColor('#17202b'), spaceAfter=3))
styles.add(ParagraphStyle(name='Sub', fontName='Malgun', fontSize=10, leading=15, textColor=colors.HexColor('#687382')))
styles.add(ParagraphStyle(name='H', fontName='MalgunBold', fontSize=14, leading=20, textColor=colors.HexColor('#17202b'), spaceBefore=14, spaceAfter=6))
styles.add(ParagraphStyle(name='BodyK', fontName='Malgun', fontSize=9.5, leading=15, textColor=colors.HexColor('#26313d'), spaceAfter=4))
styles.add(ParagraphStyle(name='Small', fontName='Malgun', fontSize=8.5, leading=13, textColor=colors.HexColor('#687382')))
P = lambda t, s='BodyK': Paragraph(t, styles[s])

story = [
    P('류연주', 'NameK'),
    P('전시·행사 프로젝트 기획자 | 참가사 유치·현장 운영 전문 | (주)메쎄이상 전시기획 및 운영 지원', 'Sub'),
    P('전시 현장에서 참가사 유치·특별관 기획·현장 운영을 직접 담당해 온 전시·행사 프로젝트 기획자입니다. 참가업체·관람객·운영스탭 다자간 이해관계를 조율하며 프로젝트를 끝까지 실행합니다.'),
]
story += [
    P('핵심 역량', 'H'),
    P('전시기획 · 참가사 유치 · 거래처(참가사) 관리·영업 · 현장 운영 · 특별관 기획 · 박람회 운영 · 국제행사 운영 · 이해관계자 조율 · 고객 경험 · 운영 프로세스 개선'),
]
story += [
    P('경력', 'H'),
    P('<b>(주)세계전람 · 전시1부 · 주임/팀원</b> | 2025.04 - 현재'),
    P('서울국제유아교육전·키즈페어, 인천 베이비&amp;키즈페어 등 전시 기획 및 현장 운영<br/>특별관 기획, <b>참가사 유치·거래처 관리</b>, 현장 운영 관리<br/>3040 부모 관람객의 관심을 반영한 콘텐츠와 이벤트 기획'),
    P('<b>(주)텍스코 · MICE1팀 · 대리/팀원</b> | 2023.01 - 2024.06'),
    P('WBC 2024 등 국제학술대회 전시·참가자 운영<br/><b>참가업체·부스 현장 운영</b> 및 공식 프로그램 지원'),
]
story += [
    P('현장 운영 프로젝트', 'H'),
    P('<b>모바일 스마트 럭키드로우 · 기획/개발/배포</b>'),
    P('행사 현장에서 추첨마다 운영 인력 2명이 필요했던 문제를 모바일 웹 도구로 전환해 운영 인력을 2명에서 1명으로 개선했습니다(참여율 130% 향상). 현장 운영 효율화 실행 사례입니다.'),
]
story += [
    P('학력·도구', 'H'),
    P('계명대학교 4년제 졸업<br/>Microsoft PowerPoint · Excel · Word · 한컴오피스'),
    P('포트폴리오: https://jjujjuya1226-cmd.github.io/recruit/', 'Small'),
]


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#dfe5eb'))
    canvas.line(18*mm, 12*mm, 192*mm, 12*mm)
    canvas.setFont('Malgun', 7.5)
    canvas.setFillColor(colors.HexColor('#687382'))
    canvas.drawString(18*mm, 7*mm, 'RYU YEONJU · 메쎄이상 전시기획 및 운영')
    canvas.drawRightString(192*mm, 7*mm, f'{doc.page}')
    canvas.restoreState()


doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(out)
