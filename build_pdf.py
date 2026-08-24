from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
from pathlib import Path

ROOT=Path(__file__).parent
pdfmetrics.registerFont(TTFont('Malgun','C:/Windows/Fonts/malgun.ttf'))
pdfmetrics.registerFont(TTFont('MalgunBold','C:/Windows/Fonts/malgunbd.ttf'))
out=ROOT/'류연주_ATS_이력서.pdf'
doc=SimpleDocTemplate(str(out),pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=16*mm,bottomMargin=16*mm,title='류연주 ATS 이력서',author='류연주')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='NameK',fontName='MalgunBold',fontSize=25,leading=31,textColor=colors.HexColor('#17202b'),spaceAfter=3))
styles.add(ParagraphStyle(name='Sub',fontName='Malgun',fontSize=10,leading=15,textColor=colors.HexColor('#687382')))
styles.add(ParagraphStyle(name='H',fontName='MalgunBold',fontSize=14,leading=20,textColor=colors.HexColor('#17202b'),spaceBefore=14,spaceAfter=6))
styles.add(ParagraphStyle(name='BodyK',fontName='Malgun',fontSize=9.5,leading=15,textColor=colors.HexColor('#26313d'),spaceAfter=4))
styles.add(ParagraphStyle(name='Small',fontName='Malgun',fontSize=8.5,leading=13,textColor=colors.HexColor('#687382')))
P=lambda t,s='BodyK': Paragraph(t,styles[s])
story=[P('류연주','NameK'),P('전시·행사 프로젝트 기획자 | Exhibition & Event Project Coordinator | 현장운영 | 고객경험 | DX·AI','Sub'),P('약 4년간 20여 개 전시·행사를 기획·운영하며 참가자·참가사·운영스탭의 요구를 조율해 왔습니다. 전시 프로젝트를 현장에서 끝까지 실행하고, 콘텐츠와 DX·AI 도구로 운영 과정을 개선하는 전시·행사 프로젝트 기획자입니다.')]
story += [P('핵심 역량','H'),P('행사기획 · 전시기획 · 박람회 운영 · 국제행사 운영 · 참가사 유치 · 현장 운영 · 고객 경험 · 콘텐츠 기획 · SNS 마케팅 · 뉴스레터 · 카드뉴스 · DX · AI 활용 · AIX · 바이브 코딩 · 업무 자동화 · 모바일 웹 · 실시간 결과 처리 · 운영 프로세스 개선')]
story += [P('경력','H'),P('<b>(주)세계전람 · 전시1부 · 주임/팀원</b> | 2025.04 - 현재'),P('서울국제유아교육전·키즈페어, 인천 베이비&키즈페어 등 전시 기획 및 현장 운영<br/>특별관 기획, 참가사 유치, 현장 운영 관리<br/>3040 부모 관람객의 관심을 반영한 콘텐츠와 이벤트 기획'),P('<b>(주)텍스코 · MICE1팀 · 대리/팀원</b> | 2023.01 - 2024.06'),P('WBC 2024 등 국제학술대회 전시·참가자 운영<br/>참가업체·부스·현장 운영 및 공식 프로그램 지원')]
story += [P('대표 프로젝트','H'),P('<b>모바일 스마트 럭키드로우 · 기획/개발/배포</b>'),P('수동 추첨을 모바일 웹 기반 실시간 랜덤 추첨 시스템으로 전환했습니다. AI·바이브 코딩으로 관리자 설정, 경품 재고·확률 가중치, 추첨 결과 흐름을 구현했습니다. 운영 인력을 2명에서 1명으로 개선하고 행사 참여율을 130% 향상시켰습니다.'),P('<b>뉴스레터 디자인 · 콘텐츠 기획</b>'),P('행사 소개, 카운트다운, 참가업체·프로그램 안내를 단계별로 구성하고 긴 세로형 콘텐츠의 정보 구조와 사전 참여 흐름을 설계했습니다.'),P('<b>카드뉴스 디자인 · SNS 콘텐츠 운영</b>'),P('관람객·참가업체·운영스탭별 행사 안내·홍보 콘텐츠를 제작했습니다. 개최 안내, 부대행사, 참가업체, SNS 이벤트, 운영스탭 모집 등 행사 전 과정의 콘텐츠를 운영했습니다.')]
story += [P('학력·도구','H'),P('계명대학교 4년제 졸업<br/>Microsoft PowerPoint · Excel · Word · 한컴오피스 · Claude · Codex · ChatGPT · Gemini · SNS 활용'),P('프로젝트: https://jjujjuya1226-cmd.github.io/luckydraw/','Small')]
def footer(canvas,doc):
    canvas.saveState(); canvas.setStrokeColor(colors.HexColor('#dfe5eb')); canvas.line(18*mm,12*mm,192*mm,12*mm); canvas.setFont('Malgun',7.5); canvas.setFillColor(colors.HexColor('#687382')); canvas.drawString(18*mm,7*mm,'RYU YEONJU · ATS RESUME'); canvas.drawRightString(192*mm,7*mm,f'{doc.page}'); canvas.restoreState()
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(out)


