from pathlib import Path
from pypdf import PdfWriter, PdfReader
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
PAGES = [
    "portfolio/luckydraw.html",
    "portfolio/illustrator-zone.html",
    "portfolio/jayhada.html",
    "portfolio/brandcall.html",
    "portfolio/newsletter.html",
    "portfolio/cardnews.html",
]
OUT = ROOT / "류연주_포트폴리오_합본.pdf"

def main():
    parts = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        for rel in PAGES:
            page.goto((ROOT / rel).as_uri(), wait_until="networkidle")
            page.emulate_media(media="print")
            parts.append(page.pdf(format="A4", print_background=True, margin={"top":"12mm","right":"10mm","bottom":"12mm","left":"10mm"}))
        browser.close()
    writer = PdfWriter()
    for data in parts:
        reader = PdfReader(__import__("io").BytesIO(data))
        for pg in reader.pages:
            writer.add_page(pg)
    with OUT.open("wb") as f:
        writer.write(f)
    print(OUT)

if __name__ == "__main__":
    main()
