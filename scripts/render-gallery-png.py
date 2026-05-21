from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "fiverr-gallery-png"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1600, 1000


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


F = {
    "eyebrow": font(34, True),
    "title": font(72, True),
    "subtitle": font(34),
    "h2": font(36, True),
    "body": font(27),
    "small": font(22),
    "caption": font(28, True),
}


def wrap_text(draw, text, face, max_width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = word if not current else current + " " + word
        if draw.textbbox((0, 0), test, font=face)[2] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw, xy, text, face, fill, max_width, line_gap=10):
    x, y = xy
    for line in wrap_text(draw, text, face, max_width):
        draw.text((x, y), line, font=face, fill=fill)
        y += face.size + line_gap
    return y


def card(draw, xy, size, fill, radius=30, outline=None):
    x, y = xy
    w, h = size
    draw.rounded_rectangle((x, y, x + w, y + h), radius=radius, fill=fill, outline=outline)


def save(img, name):
    img.save(OUT / name, "PNG", optimize=True)


def cover():
    img = Image.new("RGB", (W, H), "#0f172a")
    draw = ImageDraw.Draw(img)
    for i in range(H):
        r = int(15 + i * 0.02)
        g = int(23 + i * 0.06)
        b = int(42 + i * 0.07)
        draw.line((0, i, W, i), fill=(min(r, 25), min(g, 80), min(b, 120)))
    draw.ellipse((1160, 60, 1520, 420), fill="#14532d")
    draw.ellipse((-160, 660, 360, 1180), fill="#1e3a8a")
    draw.text((110, 120), "AGENT SKILL PACK SYSTEM", font=F["eyebrow"], fill="#99f6e4")
    draw.text((110, 232), "AI Agent & Skill Packs", font=F["title"], fill="white")
    draw.text((110, 315), "For real business workflows, audits, handoffs, and reusable automation.", font=F["subtitle"], fill="#dbeafe")
    card(draw, (110, 410), (1380, 360), "#ffffff", 34)
    draw.text((170, 490), "What you get", font=F["h2"], fill="#0f172a")
    items = [
        ("12 validated packs", "Skill logic, tests, safety", "#dbeafe", "#1e3a8a"),
        ("Filled samples", "See delivery before order", "#ccfbf1", "#115e59"),
        ("Client handoff", "Reports, notes, checklist", "#ede9fe", "#5b21b6"),
    ]
    x = 170
    for title, desc, bg, fg in items:
        card(draw, (x, 545), (380, 150), bg, 24)
        draw.text((x + 30, 590), title, font=F["body"], fill=fg)
        draw.text((x + 30, 632), desc, font=F["small"], fill=fg)
        x += 442
    draw.text((110, 890), "Validated with npm run preflight", font=F["caption"], fill="#e0f2fe")
    draw.text((690, 890), "Built for Fiverr, GitHub, and OpenClaw-style workflows", font=F["caption"], fill="#bbf7d0")
    save(img, "01-main-cover.png")


def what_you_get():
    img = Image.new("RGB", (W, H), "#f8fafc")
    draw = ImageDraw.Draw(img)
    draw.text((100, 120), "Not Just Prompts", font=F["title"], fill="#0f172a")
    draw.text((100, 200), "A complete system for reusable AI agent workflows.", font=F["subtitle"], fill="#334155")
    cols = [
        ("1. Skill Logic", ["README", "SKILL instructions", "Trigger rules", "Operating workflow"], "#dbeafe", "#1e3a8a"),
        ("2. Validation", ["Test cases", "Risk checks", "Safety boundaries", "Preflight proof"], "#ccfbf1", "#115e59"),
        ("3. Delivery", ["Report templates", "Buyer messages", "Release notes", "Acceptance checklist"], "#ede9fe", "#5b21b6"),
    ]
    x = 100
    for title, lines, bg, fg in cols:
        card(draw, (x, 285), (410, 470), bg, 30)
        draw.text((x + 38, 350), title, font=F["h2"], fill=fg)
        y = 430
        for line in lines:
            draw.text((x + 38, y), line, font=F["body"], fill=fg)
            y += 60
        x += 495
    card(draw, (100, 835), (1400, 78), "#0f172a", 22)
    draw.text((142, 858), "Each pack is structured so buyers can inspect, test, and reuse the workflow.", font=F["caption"], fill="white")
    save(img, "02-what-you-get.png")


def sample_deliverables():
    img = Image.new("RGB", (W, H), "#ecfeff")
    draw = ImageDraw.Draw(img)
    draw.text((100, 110), "See The Delivery Before You Order", font=font(62, True), fill="#164e63")
    draw.text((100, 185), "Filled sample outputs show the final handoff style.", font=F["subtitle"], fill="#0e7490")
    samples = [
        ("AI workflow log debug report", "Root cause, evidence, risk, and fix scope"),
        ("Offer builder plan", "Packages, buyer requirements, FAQ, upsell path"),
        ("AEO search readiness report", "Search clarity, FAQ, proof, and conversion edits"),
        ("Safe Git release report", "Risk map, validation, release notes, stop list"),
        ("Delivery package report", "Manifest, usage notes, validation, acceptance checklist"),
    ]
    positions = [(100, 270), (840, 270), (100, 430), (840, 430), (470, 590)]
    for (title, desc), pos in zip(samples, positions):
        card(draw, pos, (660, 120), "#ffffff", 26)
        draw.text((pos[0] + 34, pos[1] + 28), title, font=F["body"], fill="#0f172a")
        draw.text((pos[0] + 34, pos[1] + 72), desc, font=F["small"], fill="#475569")
    card(draw, (100, 815), (1400, 85), "#164e63", 24)
    draw.text((138, 842), "Use the samples to choose the right scope before paying for implementation.", font=F["caption"], fill="white")
    save(img, "03-sample-deliverables.png")


def safety_scope():
    img = Image.new("RGB", (W, H), "#fff7ed")
    draw = ImageDraw.Draw(img)
    draw.text((100, 110), "Built For Safe Freelance Delivery", font=font(62, True), fill="#7c2d12")
    draw.text((100, 185), "Clear boundaries protect the buyer, seller, and platform.", font=F["subtitle"], fill="#9a3412")
    card(draw, (100, 285), (660, 455), "#ffffff", 30)
    card(draw, (840, 285), (660, 455), "#ffffff", 30)
    draw.text((142, 350), "Included", font=font(40, True), fill="#166534")
    draw.text((882, 350), "Not Included", font=font(40, True), fill="#991b1b")
    included = ["Redacted inputs", "Public repositories", "Scoped reports", "Validation summaries", "Buyer handoff notes"]
    excluded = ["Passwords, tokens, cookies", "Payment, payout, KYC, tax", "Wallet or OAuth work", "Unscoped private repo access", "Guaranteed revenue or ranking"]
    y = 430
    for line in included:
        draw.text((142, y), line, font=F["body"], fill="#14532d")
        y += 60
    y = 430
    for line in excluded:
        draw.text((882, y), line, font=F["body"], fill="#7f1d1d")
        y += 60
    card(draw, (100, 825), (1400, 82), "#431407", 24)
    draw.text((138, 850), "Designed for redacted materials, safe scope, and platform-compliant handoff.", font=F["caption"], fill="#ffedd5")
    save(img, "04-safety-and-scope.png")


def package_ladder():
    img = Image.new("RGB", (W, H), "#f5f3ff")
    draw = ImageDraw.Draw(img)
    draw.text((100, 110), "Choose The Right Level", font=F["title"], fill="#4c1d95")
    draw.text((100, 190), "Start small, then expand into a reusable agent workflow system.", font=F["subtitle"], fill="#6d28d9")
    cards = [
        (100, 290, "#ffffff", "#5b21b6", "Starter", "One workflow or one skill idea.", ["Audit", "Scoped pack plan", "Next-step checklist"]),
        (585, 260, "#4c1d95", "#ffffff", "Standard", "A reusable business workflow.", ["Custom pack", "Test cases", "Delivery template", "Buyer handoff notes"]),
        (1070, 290, "#ffffff", "#5b21b6", "Premium", "A multi-pack operating system.", ["Pack bundle", "Proof samples", "Release and delivery docs"]),
    ]
    for x, y, bg, fg, title, desc, lines in cards:
        h = 515 if title == "Standard" else 455
        card(draw, (x, y), (430, h), bg, 30)
        muted = "#ddd6fe" if bg != "#ffffff" else "#475569"
        body = "#ede9fe" if bg != "#ffffff" else "#334155"
        draw.text((x + 38, y + 62), title, font=font(40, True), fill=fg)
        draw_wrapped(draw, (x + 38, y + 118), desc, F["small"], muted, 340, 8)
        draw.text((x + 38, y + 205), "Output", font=F["body"], fill=fg)
        ly = y + 260
        for line in lines:
            draw.text((x + 38, ly), line, font=F["body"], fill=body)
            ly += 52
    card(draw, (100, 840), (1400, 82), "#312e81", 24)
    draw.text((138, 866), "Use diagnosis first, then upgrade only when the scope is clear.", font=F["caption"], fill="white")
    save(img, "05-package-ladder.png")


def main():
    cover()
    what_you_get()
    sample_deliverables()
    safety_scope()
    package_ladder()
    for path in sorted(OUT.glob("*.png")):
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
