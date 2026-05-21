from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "fiverr-gallery-png"
OUT = ROOT / "assets" / "fiverr-gallery-contact-sheet"
OUT.mkdir(parents=True, exist_ok=True)

CARD_NAMES = [
    "01-main-cover.png",
    "02-what-you-get.png",
    "03-sample-deliverables.png",
    "04-safety-and-scope.png",
    "05-package-ladder.png",
]


def font(size, bold=False):
    candidates = [
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def load_cards():
    cards = []
    for name in CARD_NAMES:
        path = SRC / name
        if not path.exists():
            raise FileNotFoundError(f"Missing gallery card: {path}")
        cards.append((name, Image.open(path).convert("RGB")))
    return cards


def make_contact_sheet(cards):
    thumb_w, thumb_h = 640, 400
    margin = 80
    gap = 45
    title_h = 150
    label_h = 42
    cols = 2
    rows = 3
    width = margin * 2 + cols * thumb_w + gap
    height = title_h + margin + rows * (thumb_h + label_h) + (rows - 1) * gap

    sheet = Image.new("RGB", (width, height), "#f8fafc")
    draw = ImageDraw.Draw(sheet)
    draw.text((margin, 45), "Fiverr Gallery Upload Preview", font=font(46, True), fill="#0f172a")
    draw.text(
        (margin, 100),
        "Agent Skill Pack bundle: five marketplace cards, checked in one sheet.",
        font=font(24),
        fill="#334155",
    )

    for idx, (name, card) in enumerate(cards):
        row = idx // cols
        col = idx % cols
        x = margin + col * (thumb_w + gap)
        y = title_h + margin + row * (thumb_h + label_h + gap)
        thumb = card.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        draw.rounded_rectangle((x - 8, y - 8, x + thumb_w + 8, y + thumb_h + 8), radius=18, fill="#e2e8f0")
        sheet.paste(thumb, (x, y))
        draw.text((x, y + thumb_h + 12), name, font=font(24, True), fill="#0f172a")

    return sheet


def make_pdf(cards):
    pages = []
    for _, card in cards:
        page = Image.new("RGB", card.size, "white")
        page.paste(card, (0, 0))
        pages.append(page)
    pdf_path = OUT / "fiverr-gallery-cards.pdf"
    pages[0].save(pdf_path, save_all=True, append_images=pages[1:], resolution=150.0)
    return pdf_path


def main():
    cards = load_cards()
    sheet = make_contact_sheet(cards)
    sheet_path = OUT / "fiverr-gallery-contact-sheet.png"
    sheet.save(sheet_path, "PNG", optimize=True)
    pdf_path = make_pdf(cards)
    print(sheet_path.relative_to(ROOT))
    print(pdf_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
