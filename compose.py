#!/usr/bin/env python3
"""THE WORLD TODAY - Sunday, 22 November 2026.

Renders one newspaper front page (1024x1024) summing up the world news of
22 November 2026, cut off at 09:35 UTC: a Gulf-war lead with a schematic
map, four illustrated features, a consensus band, a day-in-numbers strip
and thirty one-line briefs - 40 stories across 6 regions.

Every fact is drawn from the day's reporting (One Turn's Sunday edition,
built from 757 headlines, cross-checked against Reuters, AP, the BBC,
Al Jazeera and official statements). The picture is drawn entirely with
Pillow vector shapes - no photographs - and saved as a JPEG in a file
named entry.png, byte-identical on every run.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (246, 241, 227)
PAPER_DARK = (232, 223, 199)
INK = (24, 22, 18)
FAINT = (92, 86, 72)
RED = (163, 22, 33)
BLUE = (30, 74, 110)
WATER = (176, 203, 214)
LAND = (222, 210, 175)
GOLD = (176, 132, 32)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to a pixel width; returns a list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, xy, text, fnt, width, leading, fill=INK, max_lines=None):
    x, y = xy
    lines = wrap(draw, text, fnt, width)
    if max_lines:
        lines = lines[:max_lines]
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


# ---------------------------------------------------------------- stories

LEAD = {
    "kicker": "MIDDLE EAST - THE GULF WAR",
    "headline": "Iran strikes Bahrain bases; tankers hit near Hormuz",
    "body": (
        "Iran's Revolutionary Guard said its missiles and drones struck two "
        "US Patriot radars at Bahrain's Al-Riffa and Awali bases late on "
        "Saturday, answering US drone flights and a strike on Hengam Island. "
        "Bahrain said an industrial site was hit and set ablaze - no "
        "injuries - and its defences intercepted the attacks. Kuwait engaged "
        "drones in its skies; tankers were hit near the strait. Washington "
        "says nearly all the fire was intercepted."
    ),
    "sources": "Sources: Reuters, Al Jazeera, IRNA, Bahrain Defence Force, US Central Command.",
}

FEATURES = [
    {
        "kicker": "CLIMATE - ANTALYA",
        "headline": "COP31 votes on a fuel-free deal",
        "body": (
            "Two days into overtime, the ten-page text went to nearly 200 "
            "delegations before dawn on Sunday. It recalls COP28, sets "
            "electricity at 35% of world energy by 2035, and is the first "
            "COP text to admit 1.5C will be overshot."
        ),
        "sources": "Reuters, AP, BBC, The Guardian",
        "art": "globe",
    },
    {
        "kicker": "CONFLICT - UKRAINE",
        "headline": "Russia hits Zelensky's hometown",
        "body": (
            "A ballistic missile struck Kryvyi Rih on Saturday, killing a "
            "first responder and a seven-year-old boy and wounding dozens. "
            "Ukraine's drones answered: a Russian cargo ship burned in the "
            "Gulf of Finland."
        ),
        "sources": "One Turn wires, Zelenskyy statement, Finland Border Guard",
        "art": "burst",
    },
    {
        "kicker": "JUSTICE - SINALOA",
        "headline": "'El Chapo Isidro' captured; 11 die",
        "body": (
            "Special forces arrested Fausto Isidro Meza Flores, an FBI Top "
            "10 fugitive, in Guasave on Saturday. Seven gunmen and four "
            "soldiers died in the operation; the arrest was reported by "
            "17 outlets."
        ),
        "sources": "Al Jazeera, BBC, The Guardian",
        "art": "badge",
    },
    {
        "kicker": "ECONOMY - NEW YORK",
        "headline": "AI sell-off: Wall St in correction",
        "body": (
            "Friday's rout in AI and chip shares sent the S&P 500 down "
            "3.7% into correction with the Dow, as investors doubted AI "
            "spending will pay off. The Nikkei fell 5.06% and gold slid "
            "4.62%; India's Sensex rose 2.3%."
        ),
        "sources": "One Turn market data, wire reports",
        "art": "chart",
    },
]

CONSENSUS = [
    {
        "kicker": "SHENZHEN",
        "headline": "Trump, Xi and Putin meet face to face",
        "detail": "The three leaders agreed in Shenzhen to open talks on nuclear risk reduction.",
        "sources": "One Turn, NPR",
    },
    {
        "kicker": "TRADE",
        "headline": "EU-Indonesia deal signed in Brussels",
        "detail": "The pact ends ten years of talks; 98.5% of EU goods are to enter tariff-free.",
        "sources": "European Commission, Reuters",
    },
    {
        "kicker": "PERU",
        "headline": "Quake of 6.7 shakes the Andes",
        "detail": "Epicentre near Junin; 170 homes affected, no deaths reported.",
        "sources": "USGS, AP",
    },
    {
        "kicker": "GAZA",
        "headline": "Aid vehicle hit as strikes go on",
        "detail": "Israeli strikes continued; Hamas seeks urgent talks after aid workers were killed.",
        "sources": "WAFA, wire reports",
    },
    {
        "kicker": "THE HAGUE",
        "headline": "ICJ: Myanmar committed genocide",
        "detail": "The court finds Myanmar responsible over the Rohingya; advocates press for penalties.",
        "sources": "ICJ, wire reports",
    },
]

NUMBERS = [
    ("400+", "drones in Russia's overnight barrage"),
    ("110+", "missiles in the same barrage"),
    ("-3.7%", "the S&P 500 on Friday"),
    ("-5.1%", "Japan's Nikkei index"),
    ("-4.6%", "gold, in the sell-off"),
    ("$3.79bn", "GTA VI's launch-day record"),
    ("6.7", "the Peru quake's magnitude"),
    ("35%", "electricity's 2035 goal at COP31"),
]

BRIEFS = [
    ("DENMARK", "expels Russia's attaché over an alleged plot against a Ukrainian rapper; urges EU visa limits."),
    ("NIGERIA", "a boat carrying funeral mourners capsizes in the south; 24 dead, the emergency agency says."),
    ("INDONESIA", "candy factory fire in Serang, Banten leaves 3 dead and dozens missing."),
    ("YEMEN", "Houthis fire missiles at Saudi Arabia after a coalition operation in Hodeida."),
    ("FINLAND", "probes a suspected Russian helicopter incursion, 4.1 km into its airspace."),
    ("HORMUZ CLAIM", "Iran says a missile hit a US F-16 over the strait; Washington denies any damage."),
    ("BRITAIN", "UK and EU strike deals; Burnham eyes rejoining the bloc."),
    ("LEBANON", "President Aoun blames Israel and Iran for threats to his country's sovereignty."),
    ("WEST BANK", "settler attacks rise; Jeffries to push legislation in Washington."),
    ("EU-RWANDA", "Brussels moves on Rwanda deportation hubs and a digital tax."),
    ("HAITI", "Haiti and El Salvador agree to build three prisons together."),
    ("BRAZIL", "Bolsonaro is in intensive care with a bowel obstruction."),
    ("WASHINGTON", "Trump orders federal contractors to report congressional requests."),
    ("BANGLADESH", "garment workers strike amid political clashes in Dhaka."),
    ("ENERGY", "Saudi Arabia triples the oil it stores in Japan."),
    ("ARGENTINA", "approves a $50 billion LNG export project in Buenos Aires."),
    ("BELGIUM", "an air-traffic strike is set to cancel flights from Brussels."),
    ("HEALTH", "a one-time CRISPR therapy cuts bad cholesterol by 52% in a trial."),
    ("BRITAIN", "Princess Kate says she is in remission from cancer."),
    ("SPACE", "Earth gains a new mini-moon, 2026 QQ8."),
    ("JAPAN", "a pilotless air taxi carries a passenger in Yamanashi prefecture."),
    ("GAMES", "GTA VI takes a record $3.79 billion on its launch day."),
    ("FOOTBALL", "Leeds stun Chelsea 4-1, their first win at Stamford Bridge since 1999."),
    ("SOUTH AFRICA", "Phumzile Mlambo-Ngcuka, former deputy president, dies at 71."),
    ("TENNIS", "Alcaraz will play Zverev in the ATP Finals final in Turin."),
    ("MUSIC", "BTS win five MAMA awards in Osaka."),
    ("HORMUZ", "a British swimmer crosses the strait to show the war's toll on wildlife."),
    ("IRAN", "Tehran begins rationing electricity as the war strains the grid."),
    ("TUNISIA", "activist Sihem Bensedrine is jailed for five years."),
    ("INDIA", "fake liquor kills at least 11 people in Manipur."),
]


# ---------------------------------------------------------------- drawing

def masthead(draw):
    draw.rectangle([0, 0, W, 8], fill=INK)
    title_f = font(SERIF_B, 63)
    title = "THE WORLD TODAY"
    tw = draw.textlength(title, font=title_f)
    draw.text(((W - tw) / 2, 16), title, font=title_f, fill=INK)
    draw.line([18, 92, W - 18, 92], fill=INK, width=3)
    draw.line([18, 97, W - 18, 97], fill=INK, width=1)
    meta_f = font(SANS_B, 17)
    date_line = "SUNDAY, 22 NOVEMBER 2026"
    dw = draw.textlength(date_line, font=meta_f)
    draw.text(((W - dw) / 2, 104), date_line, font=meta_f, fill=RED)
    side_f = font(SANS, 13)
    draw.text((18, 106), "40 stories - 6 regions - one page", font=side_f, fill=FAINT)
    right = "News to 09:35 UTC"
    rw = draw.textlength(right, font=side_f)
    draw.text((W - 18 - rw, 106), right, font=side_f, fill=FAINT)
    draw.line([18, 130, W - 18, 130], fill=INK, width=1)


def gulf_map(draw, box):
    """Schematic map of the northern Gulf and the Strait of Hormuz."""
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=WATER, outline=INK, width=2)
    # Halftone swell lines on the water, for print texture.
    for row, wy in enumerate(range(y0 + 14, y1 - 24, 13)):
        offset = 7 if row % 2 else 0
        for wx in range(x0 + 10 + offset, x1 - 12, 15):
            draw.ellipse([wx, wy, wx + 2, wy + 2], fill=(150, 182, 196))
    # Land: Arabia along the bottom-left, Iran along the top-right.
    draw.polygon([(x0, y1), (x0, y0 + 118), (x0 + 96, y0 + 96),
                  (x0 + 150, y0 + 150), (x0 + 205, y0 + 176),
                  (x0 + 250, y1)], fill=LAND)
    draw.polygon([(x0 + 205, y0), (x1, y0), (x1, y0 + 84),
                  (x0 + 268, y0 + 96), (x0 + 236, y0 + 52)], fill=LAND)
    # Qatar peninsula and the strait narrows.
    draw.polygon([(x0 + 128, y0 + 138), (x0 + 152, y0 + 118),
                  (x0 + 160, y0 + 146), (x0 + 140, y0 + 158)], fill=LAND)
    dot_f = font(SANS_B, 11)
    places = [
        ("KUWAIT", x0 + 62, y0 + 92, RED),
        ("BAHRAIN", x0 + 118, y0 + 128, RED),
        ("QATAR", x0 + 148, y0 + 152, INK),
        ("IRAN", x0 + 292, y0 + 40, INK),
        ("STRAIT OF HORMUZ", x0 + 236, y0 + 128, RED),
        ("OMAN", x0 + 306, y0 + 168, INK),
    ]
    for name, px, py, colour in places:
        r = 5 if colour == RED else 4
        draw.ellipse([px - r, py - r, px + r, py + r], fill=colour)
        draw.text((px + 9, py - 6), name, font=dot_f, fill=INK)
    for px, py in [(x0 + 118, y0 + 128), (x0 + 62, y0 + 92), (x0 + 262, y0 + 118)]:
        for dx, dy in [(0, -11), (8, -8), (11, 0), (8, 8), (0, 11),
                       (-8, 8), (-11, 0), (-8, -8)]:
            draw.line([px, py, px + dx, py + dy], fill=RED, width=2)
    cap_f = font(SANS_I, 11)
    draw.text((x0 + 8, y1 - 18),
              "The Gulf on Saturday night: strikes, interceptions, tankers hit.",
              font=cap_f, fill=INK)


def feature_art(draw, kind, box):
    x0, y0, x1, y1 = box
    if kind == "chart":
        base = y1 - 8
        vals = [0.25, 0.45, 0.4, 0.62, 0.55, 0.85, 1.0]
        step = (x1 - x0 - 12) // len(vals)
        pts = []
        for i, v in enumerate(vals):
            px = x0 + 6 + i * step
            py = base - int(v * (y1 - y0 - 14))
            pts.append((px, py))
            draw.line([px, base, px, py], fill=RED, width=3)
        draw.line(pts, fill=INK, width=2)
        draw.line([x0 + 2, base, x1 - 2, base], fill=INK, width=1)
    elif kind == "globe":
        cx, cy, r = (x0 + x1) // 2, (y0 + y1) // 2, (y1 - y0) // 2 - 4
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=BLUE, width=3)
        draw.ellipse([cx - r // 3, cy - r, cx + r // 3, cy + r], outline=BLUE, width=1)
        draw.line([cx - r, cy, cx + r, cy], fill=BLUE, width=1)
        draw.line([cx - r, cy - r // 2, cx + r, cy - r // 2], fill=BLUE, width=1)
        draw.line([cx - r, cy + r // 2, cx + r, cy + r // 2], fill=BLUE, width=1)
    elif kind == "burst":
        cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
        for dx, dy in [(0, -20), (14, -14), (20, 0), (14, 14), (0, 20),
                       (-14, 14), (-20, 0), (-14, -14)]:
            draw.line([cx, cy, cx + dx, cy + dy], fill=RED, width=3)
        draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=RED)
    elif kind == "badge":
        cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
        pts = []
        import math
        for i in range(10):
            ang = -math.pi / 2 + i * math.pi / 5
            rad = 22 if i % 2 == 0 else 10
            pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
        draw.polygon(pts, outline=GOLD, width=3)
        draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], outline=GOLD, width=2)


def build():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    masthead(draw)

    # Lead, left column.
    lx, ly, lw = 18, 142, 596
    draw.text((lx, ly), LEAD["kicker"], font=font(SANS_B, 15), fill=RED)
    y = text_block(draw, (lx, ly + 22), LEAD["headline"],
                   font(SERIF_B, 37), lw, 43)
    y = text_block(draw, (lx, y + 8), LEAD["body"],
                   font(SANS, 14), lw, 18.5) + 6
    draw.text((lx, y), LEAD["sources"], font=font(SANS_I, 12), fill=FAINT)
    gulf_map(draw, (632, 142, 1006, 382))
    draw.line([18, 392, W - 18, 392], fill=INK, width=2)

    # Four features in a row.
    fy = 402
    fw = (W - 36 - 3 * 12) // 4
    for i, feat in enumerate(FEATURES):
        fx = 18 + i * (fw + 12)
        draw.rectangle([fx, fy, fx + fw, fy + 144], outline=INK, width=1)
        feature_art(draw, feat["art"], (fx + fw - 52, fy + 8, fx + fw - 8, fy + 46))
        draw.text((fx + 8, fy + 8), feat["kicker"], font=font(SANS_B, 11), fill=RED)
        y = text_block(draw, (fx + 8, fy + 26), feat["headline"],
                       font(SERIF_B, 16), fw - 62, 19, max_lines=2)
        text_block(draw, (fx + 8, max(y + 4, fy + 68)), feat["body"],
                   font(SANS, 11), fw - 16, 13, max_lines=5)
    draw.line([18, 556, W - 18, 556], fill=INK, width=2)

    # Consensus band: the five stories every wire carried.
    cy0 = 566
    draw.rectangle([18, cy0, W - 18, cy0 + 22], fill=INK)
    band_f = font(SANS_B, 13)
    band_t = "ON EVERY WIRE - THE CONSENSUS FIVE"
    bw = draw.textlength(band_t, font=band_f)
    draw.text(((W - bw) / 2, cy0 + 4), band_t, font=band_f, fill=PAPER)
    cw = (W - 36 - 4 * 10) // 5
    for i, item in enumerate(CONSENSUS):
        cx = 18 + i * (cw + 10)
        draw.text((cx, cy0 + 28), item["kicker"], font=font(SANS_B, 11), fill=RED)
        y = text_block(draw, (cx, cy0 + 43), item["headline"],
                       font(SERIF_B, 12), cw, 14, max_lines=2)
        y = text_block(draw, (cx, y), item["detail"],
                       font(SANS, 10), cw, 12, max_lines=3)
        draw.text((cx, y + 1), item["sources"], font=font(SANS_I, 9), fill=FAINT)
    draw.line([18, 688, W - 18, 688], fill=INK, width=1)

    # The day in numbers.
    ny = 698
    nw = (W - 36) // 8
    for i, (num, label) in enumerate(NUMBERS):
        cx = 18 + i * nw
        num_f = font(SERIF_B, 22)
        tw = draw.textlength(num, font=num_f)
        draw.text((cx + (nw - tw) / 2, ny), num, font=num_f, fill=RED)
        lab_lines = wrap(draw, label, font(SANS, 9), nw - 8)
        ly = ny + 30
        for line in lab_lines[:2]:
            lw2 = draw.textlength(line, font=font(SANS, 9))
            draw.text((cx + (nw - lw2) / 2, ly), line, font=font(SANS, 9), fill=FAINT)
            ly += 11
    draw.line([18, 756, W - 18, 756], fill=INK, width=2)

    # Briefs, three columns.
    by = 766
    draw.text((18, by), "THE DAY IN BRIEF - 30 MORE STORIES", font=font(SANS_B, 14), fill=INK)
    col_w = (W - 36 - 2 * 14) // 3
    per_col = (len(BRIEFS) + 2) // 3
    for c in range(3):
        cx = 18 + c * (col_w + 14)
        cy = by + 22
        for lead, rest in BRIEFS[c * per_col:(c + 1) * per_col]:
            cy = text_block(draw, (cx, cy), lead + " - " + rest,
                            font(SANS, 10.5), col_w, 11, max_lines=2) + 0.5
    foot_f = font(SANS_I, 10)
    foot = "Set from the wires of Sunday 22 November 2026 - drawn and typeset by an AI agent."
    fw2 = draw.textlength(foot, font=foot_f)
    draw.text(((W - fw2) / 2, 1006), foot, font=foot_f, fill=FAINT)
    return img


if __name__ == "__main__":
    build().save("entry.png", format="JPEG", quality=88, subsampling=1)
