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
out = ROOT / '류연주_메쎄이상_전시마케팅_이력서.pdf'
doc = SimpleDocTemplate(str(out), pagesize=A4, rightMargin=18*mm, leftMargin=18*mm, topMargin=16*mm, bottomMargin=16*mm, title='류연주 이력서 - 전시 마케팅', author='류연주')
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='NameK', fontName='MalgunBold', fontSize=25, leading=31, textColor=colors.HexColor('#17202b'), spaceAfter=3))
styles.add(ParagraphStyle(name='Sub', fontName='Malgun', fontSize=10, leading=15, textColor=colors.HexColor('#687382')))
styles.add(ParagraphStyle(name='H', fontName='MalgunBold', fontSize=14, leading=20, textColor=colors.HexColor('#17202b'), spaceBefore=14, spaceAfter=6))
styles.add(ParagraphStyle(name='BodyK', fontName='Malgun', fontSize=9.5, leading=15, textColor=colors.HexColor('#26313d'), spaceAfter=4))
styles.add(ParagraphStyle(name='Small', fontName='Malgun', fontSize=8.5, leading=13, textColor=colors.HexColor('#687382')))
P = lambda t, s='BodyK': Paragraph(t, styles[s])

story = [
    P('류연주', 'NameK'),
    P('전시·행사 콘텐츠 마케터 | 영상편집·SNS 콘텐츠 제작 및 실제 광고 집행 | (주)메쎄이상 전시 마케팅 지원', 'Sub'),
    P('행사 콘텐츠 기획부터 영상 제작, 실제 유료 광고 집행까지 콘텐츠 마케팅을 end-to-end로 실행해 온 전시·행사 콘텐츠 마케터입니다. 참가사 유치와 관람객 사전 참여를 콘텐츠로 연결합니다.'),
]
story += [
    P('핵심 역량', 'H'),
    P('마케팅기획 · 영상편집 · SNS 마케팅 · 블로그마케팅 · 뉴스레터 콘텐츠 · 카드뉴스 콘텐츠 · 행사기획 · 유료 광고 집행 · 콘텐츠 자산 구축'),
]
story += [
    P('대표 프로젝트', 'H'),
    P('<b>참가브랜드모집 캠페인 · 기획/영상제작/광고집행</b>'),
    P('서울국제유아교육전 &amp; 키즈페어(COEX) 입점 브랜드 모집을 위해 홍보 영상을 제작하고, 인스타그램(segefairs 계정) <b>실제 유료 광고</b>로 집행했습니다. 캠페인 메시지 기획부터 소재 제작, 광고 집행까지 담당했습니다.'),
    P('<b>모바일 스마트 럭키드로우 · 기획/개발/배포</b>'),
    P('AI·바이브 코딩으로 모바일 웹 실시간 추첨 시스템을 직접 개발·배포했습니다. 운영 인력 2명에서 1명으로 개선, 행사 참여율 130% 향상.'),
    P('<b>뉴스레터 디자인 · 콘텐츠 기획</b>'),
    P('행사 소개, 카운트다운, 참가업체·프로그램 안내를 단계별로 구성한 콘텐츠 템플릿 5종을 제작해 행사마다 재사용하고 있습니다.'),
    P('<b>카드뉴스 시스템 · SNS 콘텐츠 운영</b>'),
    P('관람객·참가업체·운영스탭 대상별 메시지를 템플릿화한 카드뉴스 8종을 제작·운영했습니다.'),
]
story += [
    P('경력', 'H'),
    P('<b>(주)세계전람 · 전시1부 · 주임/팀원</b> | 2025.04 - 현재'),
    P('서울국제유아교육전·키즈페어, 인천 베이비&amp;키즈페어 등 전시 기획 및 현장 운영<br/>3040 부모 관람객의 관심을 반영한 콘텐츠와 이벤트 기획'),
    P('<b>(주)텍스코 · MICE1팀 · 대리/팀원</b> | 2023.01 - 2024.06'),
    P('WBC 2024 등 국제학술대회 전시·참가자 운영'),
]
story += [
    P('학력·도구', 'H'),
    P('계명대학교 4년제 졸업<br/>Microsoft PowerPoint · Excel · Word · 한컴오피스 · AI 영상·콘텐츠 제작 도구'),
    P('포트폴리오(실제 광고 캡처 포함): https://jjujjuya1226-cmd.github.io/recruit/', 'Small'),
]


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#dfe5eb'))
    canvas.line(18*mm, 12*mm, 192*mm, 12*mm)
    canvas.setFont('Malgun', 7.5)
    canvas.setFillColor(colors.HexColor('#687382'))
    canvas.drawString(18*mm, 7*mm, 'RYU YEONJU · 메쎄이상 전시 마케팅')
    canvas.drawRightString(192*mm, 7*mm, f'{doc.page}')
    canvas.restoreState()


doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(out)
