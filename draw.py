#!/usr/bin/env python3
"""Draw the front page for Sunday 22 November 2026.

Renders a dense newspaper front page with Pillow and saves it as
entry.png (1024x1024). Run:  python3 draw.py
The entry program (main.py) only copies the rendered file; this script
is the build tool that produced it, kept in the repo for transparency.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))

INK = (18, 18, 18)
PAPER = (247, 242, 231)
PAPER2 = (241, 234, 219)
RED = (178, 34, 34)
NAVY = (24, 44, 84)
SEA = (198, 220, 232)
SAND = (232, 214, 178)
GREY = (90, 86, 78)
RULE = (40, 40, 40)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, f, width):
    """Greedy word wrap; returns a list of lines that fit `width`."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=f) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(d, x, y, w, text, f, fill=INK, lh=None, max_lines=None):
    """Draw wrapped text; return the y just below the last line."""
    if lh is None:
        lh = int(f.size * 1.32)
    lines = wrap(d, text, f, w)
    if max_lines:
        lines = lines[:max_lines]
    for ln in lines:
        d.text((x, y), ln, font=f, fill=fill)
        y += lh
    return y


def kicker(d, x, y, text, color=RED):
    f = font(SANS_B, 12)
    d.text((x, y), text, font=f, fill=color)
    return y + 17


def hline(d, x0, x1, y, wdt=1, fill=RULE):
    d.line([(x0, y), (x1, y)], fill=fill, width=wdt)


def box(d, x0, y0, x1, y1, fill=None, outline=RULE, wdt=1):
    d.rectangle([x0, y0, x1, y1], fill=fill, outline=outline, width=wdt)


# ---------------------------------------------------------------- icons
def icon_globe(d, x, y, s):
    d.ellipse([x, y, x + s, y + s], outline=(34, 110, 60), width=3)
    d.ellipse([x + s * 0.28, y + 3, x + s * 0.72, y + s - 3],
              outline=(34, 110, 60), width=2)
    d.line([(x, y + s / 2), (x + s, y + s / 2)], fill=(34, 110, 60), width=2)
    d.line([(x + 3, y + s * 0.28), (x + s - 3, y + s * 0.28)],
           fill=(34, 110, 60), width=1)
    d.line([(x + 3, y + s * 0.72), (x + s - 3, y + s * 0.72)],
           fill=(34, 110, 60), width=1)
    # leaf
    d.pieslice([x + s * 0.55, y - 8, x + s + 12, y + 14], 200, 340,
               fill=(46, 139, 55))


def icon_missile(d, x, y, s):
    # diagonal missile + burst
    d.polygon([(x + 6, y + s - 6), (x + s - 4, y + 10), (x + s - 14, y + 16),
               (x + 16, y + s - 14)], fill=(90, 90, 90))
    d.polygon([(x + s - 4, y + 10), (x + s + 8, y + 2), (x + s - 2, y + 18)],
              fill=RED)
    for a, b in [((x + 2, y + s - 2), (x + 14, y + s - 14)),
                 ((x + 8, y + s - 2), (x + 18, y + s - 12))]:
        d.line([a, b], fill=(200, 140, 40), width=2)
    cx, cy = x + s - 2, y + s - 2
    for dx, dy in [(0, -12), (10, -6), (12, 4), (4, 12), (-6, 10), (-12, 2)]:
        d.line([(cx, cy), (cx + dx, cy + dy)], fill=(220, 120, 20), width=2)


def icon_quake(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], outline=GREY, width=2)
    pts = [(x + 3, y + s / 2), (x + s * 0.25, y + s / 2),
           (x + s * 0.35, y + s * 0.2), (x + s * 0.45, y + s * 0.8),
           (x + s * 0.55, y + s * 0.3), (x + s * 0.65, y + s * 0.7),
           (x + s * 0.75, y + s / 2), (x + s - 3, y + s / 2)]
    d.line(pts, fill=RED, width=2, joint="curve")


def icon_ship(d, x, y, s):
    d.polygon([(x + 2, y + s * 0.62), (x + s - 2, y + s * 0.62),
               (x + s - 10, y + s - 4), (x + 10, y + s - 4)], fill=NAVY)
    for i, c in enumerate([(178, 34, 34), (34, 110, 60), (200, 140, 40)]):
        bx = x + 8 + i * (s - 16) // 3
        d.rectangle([bx, y + s * 0.34, bx + (s - 20) // 3, y + s * 0.6],
                    fill=c, outline=(255, 255, 255))
    d.line([(x, y + s - 2), (x + s, y + s - 2)], fill=(70, 130, 180), width=2)


def icon_badge(d, x, y, s):
    cx, cy, r = x + s / 2, y + s / 2, s * 0.36
    pts = []
    import math
    for i in range(10):
        ang = math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.55
        pts.append((cx + rr * math.cos(ang), cy - rr * math.sin(ang)))
    d.polygon(pts, fill=(200, 160, 40), outline=(120, 90, 10))
    d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(255, 255, 255))
    # bars
    for i in range(3):
        bx = x + s - 8 + i * 0
        d.line([(x + s + 2, y + 4 + i * 12), (x + s + 2, y + 14 + i * 12)],
               fill=GREY, width=2)


# ---------------------------------------------------------------- page
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 24
    X1 = W - M

    # paper grain: faint horizontal rules
    for yy in range(0, H, 4):
        d.line([(0, yy), (W, yy)], fill=(250, 246, 236), width=1)

    # ---- masthead
    hline(d, M, X1, 14, 3)
    hline(d, M, X1, 19, 1)
    f_mast = font(SERIF_B, 62)
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=f_mast)
    d.text(((W - tw) / 2, 24), title, font=f_mast, fill=INK)
    f_date = font(SANS_B, 13)
    d.text((M, 96), "SUNDAY, 22 NOVEMBER 2026", font=f_date, fill=INK)
    mid = "THE WORLD IN ONE PAGE"
    d.text(((W - d.textlength(mid, font=f_date)) / 2, 96), mid,
           font=f_date, fill=GREY)
    right = "34 STORIES  •  FROM AROUND THE WORLD"
    d.text((X1 - d.textlength(right, font=f_date), 96), right,
           font=f_date, fill=INK)
    hline(d, M, X1, 116, 2)

    # ---- strapline
    f_strap = font(SERIF_I, 16)
    strap = ("War widens in the Gulf, NATO stands by Poland, climate talks run "
             "out of time \u2014 and a cartel kingpin falls.")
    d.text(((W - d.textlength(strap, font=f_strap)) / 2, 122), strap,
           font=f_strap, fill=(60, 58, 52))
    hline(d, M, X1, 146, 1)

    # ---- LEAD: Gulf war
    ly = 154
    box(d, M, ly, X1, ly + 176, fill=PAPER2, outline=RULE, wdt=1)
    lx, lw = M + 12, 620
    y = ly + 10
    y = kicker(d, lx, y, "MIDDLE EAST  —  THE GULF WAR")
    f_lead = font(SERIF_B, 27)
    y = para(d, lx, y, lw,
             "Iran strikes US bases in Kuwait and Bahrain as Gulf war widens",
             f_lead, lh=31, max_lines=3)
    y += 2
    f_body = font(SANS, 13)
    y = para(d, lx, y, lw,
             "Iran fired drones and missiles at US military targets in Kuwait "
             "and Bahrain, its Revolutionary Guard said, in the latest widening "
             "of a war now in its ninth month. Kuwait said its defences answered "
             "the drones over Ali Al Salem air base; Bahrain said it intercepted "
             "the attacks after shelter alerts.",
             f_body, lh=16, max_lines=4)
    y += 3
    f_bul = font(SANS_B, 12)
    for b in ["Tanker hit by a mine east of the Strait of Hormuz  •  More tankers attacked off Oman"]:
        d.text((lx, y), "\u2022  " + b, font=f_bul, fill=RED)
        y += 16

    # schematic Gulf map, right of lead
    mx0, my0, mx1, my1 = 672, ly + 10, X1 - 12, ly + 166
    d.rectangle([mx0, my0, mx1, my1], fill=SEA, outline=RULE, width=1)
    # Iran (top-left land), Arabia (right land)
    d.polygon([(mx0, my0), (mx1 - 110, my0), (mx1 - 130, my0 + 46),
               (mx0 + 150, my0 + 60), (mx0, my0 + 46)], fill=SAND)
    d.polygon([(mx1 - 110, my0), (mx1, my0), (mx1, my1),
               (mx1 - 110, my1), (mx1 - 170, my1 - 60), (mx1 - 130, my0 + 46)],
              fill=SAND)
    d.text((mx0 + 8, my0 + 6), "IRAN", font=font(SANS_B, 11), fill=GREY)
    d.text((mx1 - 88, my1 - 52), "ARABIA", font=font(SANS_B, 11), fill=GREY)
    d.text((mx0 + 12, my0 + 100), "THE GULF", font=font(SERIF_I, 13),
           fill=(50, 90, 120))
    f_map = font(SANS_B, 10)
    marks = [("ALI AL SALEM", 158, 52), ("BAHRAIN", 178, 86),
             ("HORMUZ", 96, 128)]
    for name, px, py in marks:
        d.ellipse([mx0 + px - 4, my0 + py - 4, mx0 + px + 4, my0 + py + 4],
                  fill=RED, outline=(255, 255, 255))
        d.text((mx0 + px + 7, my0 + py - 6), name, font=f_map, fill=INK)
    # Oman: label under its dot so it clears the ARABIA tag
    d.ellipse([mx0 + 228, my0 + 128, mx0 + 236, my0 + 136],
              fill=RED, outline=(255, 255, 255))
    d.text((mx0 + 222, my0 + 140), "OMAN", font=f_map, fill=INK)
    d.text((mx0 + 6, my1 - 14), "SCHEMATIC MAP — NOT TO SCALE",
           font=font(SANS, 8), fill=GREY)

    # ---- Row 2: COP31 | Ukraine/Poland
    ry = 338
    rh = 168
    panels2 = [
        (M, 500, "CLIMATE  —  ANTALYA, TURKEY",
         "COP31 runs into overtime as fossil fuels vanish from the draft",
         "Climate talks in Antalya stretched into a second day of overtime on "
         "Sunday, deadlocked over a draft deal that mentions no fossil fuels "
         "at all. A new package went to nearly 200 delegations in the early "
         "hours; the presidency hopes to approve it on Sunday morning. The EU "
         "warned it would take \u201ca good deal or no deal\u201d.",
         icon_globe),
        (512, X1, "EUROPE  —  WAR IN UKRAINE",
         "Russian missiles land in Poland as barrage batters Ukraine",
         "Two Russian cruise missiles and a drone came down in south-east "
         "Poland during a huge overnight assault on Ukraine \u2014 more than "
         "400 drones and 110 missiles, Kyiv said. Lviv was hit hard: 2 killed, "
         "10 hurt. Warsaw called it a deliberate provocation; NATO chief Mark "
         "Rutte flew to Warsaw and vowed to defend \u201cevery inch\u201d of "
         "Polish soil.",
         icon_missile),
    ]
    for x0, x1, kick, head, body, icon in panels2:
        box(d, x0, ry, x1, ry + rh, fill=(255, 255, 255), outline=RULE, wdt=1)
        y = ry + 10
        y = kicker(d, x0 + 12, y, kick)
        icon(d, x1 - 58, ry + 8, 44)
        f_h = font(SERIF_B, 20)
        y = para(d, x0 + 12, y, (x1 - x0) - 72, head, f_h, lh=23, max_lines=2)
        y += 2
        para(d, x0 + 12, y, (x1 - x0) - 24, body, font(SANS, 12),
             lh=15, max_lines=5)

    # ---- Row 3: Peru | EU-Indonesia | Mexico
    ry3 = 514
    rh3 = 142
    cols3 = [(M, 336), (344, 656), (664, X1)]
    feats3 = [
        ("AMERICAS  —  EARTHQUAKE",
         "Strong quake shakes Peru\u2019s Andes",
         "A magnitude 6.7 earthquake (USGS) struck the Andes in central Peru "
         "on Friday evening, its epicentre near Jun\u00edn, sending residents "
         "of Lima into the streets. No casualties or major damage reported.",
         icon_quake),
        ("TRADE  —  BRUSSELS",
         "EU and Indonesia sign trade deal",
         "The EU and Indonesia signed a trade pact in Brussels on Saturday, "
         "ending nearly 10 years of talks. Once in force, tariffs fall on "
         "98.5% of EU goods and over 90% of Indonesian goods. Parliaments "
         "must still approve it; entry into force is targeted for 2027.",
         icon_ship),
        ("AMERICAS  —  CARTELS",
         "Mexico captures \u2018El Chapo Isidro\u2019",
         "Mexican special forces captured Fausto Isidro Meza Flores, \u2018El "
         "Chapo Isidro\u2019, an FBI Top 10 fugitive, in Guasave on Friday "
         "night. The raid set off gun battles across Sinaloa that left 11 "
         "dead \u2014 7 gunmen and 4 soldiers. He was flown to Mexico City.",
         icon_badge),
    ]
    for (x0, x1), (kick, head, body, icon) in zip(cols3, feats3):
        box(d, x0, ry3, x1, ry3 + rh3, fill=(255, 255, 255), outline=RULE, wdt=1)
        y = ry3 + 9
        y = kicker(d, x0 + 10, y, kick)
        icon(d, x1 - 46, ry3 + 6, 36)
        f_h = font(SERIF_B, 17)
        y = para(d, x0 + 10, y, (x1 - x0) - 56, head, f_h, lh=20, max_lines=2)
        y += 1
        para(d, x0 + 10, y, (x1 - x0) - 20, body, font(SANS, 11),
             lh=14, max_lines=4)

    # ---- Diplomacy band
    by = 664
    d.rectangle([M, by, X1, by + 40], fill=NAVY)
    f_band = font(SANS, 13)
    band1 = ("SHENZHEN \u2014 Trump, Xi and Putin meet face to face; little is agreed.    "
             "KYIV \u2014 Zelensky: new peace talks may open on the G20 sidelines.")
    band2 = ("WASHINGTON \u2014 Vance declines to back Trump\u2019s strikes on Iran.    "
             "ANTALYA \u2014 Draft drops the $120bn adaptation-finance target.")
    d.text(((W - d.textlength(band1, font=f_band)) / 2, by + 5), band1,
           font=f_band, fill=(255, 255, 255))
    d.text(((W - d.textlength(band2, font=f_band)) / 2, by + 22), band2,
           font=f_band, fill=(255, 255, 255))

    # ---- Numbers strip
    ny = 712
    d.text((M, ny), "THE DAY IN NUMBERS", font=font(SANS_B, 12), fill=INK)
    hline(d, M, X1, ny + 17, 1)
    stats = [
        ("400+", "drones Russia fired at Ukraine in a single night, Kyiv said"),
        ("110+", "missiles in the same barrage, one of the war\u2019s largest"),
        ("11", "killed in Sinaloa after the raid that caught \u2018El Chapo Isidro\u2019"),
        ("6.7", "magnitude of the Peru quake, USGS; felt across Lima"),
        ("98.5%", "of EU goods to go tariff-free under the Indonesia deal"),
    ]
    cw = (X1 - M) / 5
    for i, (num, lab) in enumerate(stats):
        cx = M + i * cw
        f_num = font(SERIF_B, 28)
        d.text((cx + 6, ny + 24), num, font=f_num, fill=RED)
        para(d, cx + 6, ny + 58, cw - 14, lab, font(SANS, 10), lh=12,
             max_lines=2)
        if i:
            d.line([(cx, ny + 24), (cx, ny + 78)], fill=(200, 196, 186), width=1)

    # ---- Briefs
    byy = 798
    d.text((M, byy), "THE REST OF THE DAY \u2014 IN BRIEF",
           font=font(SANS_B, 12), fill=INK)
    hline(d, M, X1, byy + 17, 1)
    briefs = [
        ("HONG KONG", "Voting begins in Election Committee polls."),
        ("DENMARK", "Moscow envoy expelled over an alleged plot against a Ukrainian rapper."),
        ("BALTIC SEA", "A drone strikes a Russian cargo ship off Finland."),
        ("MARKETS", "The tech sell-off rolls on as investors dump shares."),
        ("WASHINGTON", "The FBI probes a suspected hack of its criminal database."),
        ("BRAZIL", "Former president Bolsonaro is in intensive care."),
        ("SUDAN", "The Tasis alliance seizes Bau in Blue Nile state."),
        ("INDIA", "Bootleg liquor kills 11 in Manipur."),
        ("ESTONIA", "The border with Russia is closed."),
        ("UNITED NATIONS", "Talks fail to agree rules for autonomous weapons."),
        ("JAPAN", "Troops hold their first live-fire drill at a facility in India."),
        ("NEW DELHI", "The SCO summit opens in the Indian capital."),
        ("HORMUZ", "A tanker is hit by a mine east of the strait."),
        ("OMAN", "More tankers are attacked off the Omani coast."),
        ("KUWAIT", "Air defences answer drones over Ali Al Salem; no damage reported."),
        ("BAHRAIN", "Shelter alerts sound as defences intercept a fresh wave."),
        ("LVIV", "Friday\u2019s barrage kills 2 and injures 10; a railway station is hit."),
        ("KYIV", "Three bridges are damaged in the overnight assault."),
        ("WARSAW", "NATO to discuss the incursion at a council meeting on Monday."),
        ("GUASAVE", "Fans flee a baseball game as gunfire erupts."),
        ("MEXICO CITY", "The US had a $5m reward on \u2018El Chapo Isidro\u2019."),
        ("SINALOA", "Troops stay deployed to clear roadblocks and protect civilians."),
        ("LIMA", "A TV anchor keeps reporting live as the studio shakes."),
        ("JUN\u00cdN", "The quake\u2019s epicentre lies 34 km north of Jun\u00edn, 108 km deep (USGS)."),
    ]
    colw = (X1 - M - 32) / 3
    f_b = font(SANS, 11)
    f_bt = font(SANS_B, 11)
    for i, (tag, txt) in enumerate(briefs):
        col = i // 8
        row = i % 8
        bx = M + col * (colw + 16)
        by2 = byy + 24 + row * 21
        d.text((bx, by2), tag + " \u2014 ", font=f_bt, fill=RED)
        tw = d.textlength(tag + " \u2014 ", font=f_bt)
        lines = wrap(d, txt, f_b, colw - tw)
        d.text((bx + tw, by2), lines[0], font=f_b, fill=INK)
        if len(lines) > 1:
            d.text((bx, by2 + 11), lines[1], font=f_b, fill=INK)

    # ---- Footer
    fy = 1000
    hline(d, M, X1, fy - 6, 1)
    f_f = font(SANS, 10)
    foot = ("Sources: Reuters  •  AP  •  AFP  •  USGS  •  European Commission  •  "
            "Mexican Defence Ministry  •  IRIB.  Events as reported on Sunday "
            "22 November 2026 and the weekend leading into it.")
    d.text((M, fy), foot, font=f_f, fill=GREY)
    d.text((M, fy + 12), "THE WORLD TODAY \u2014 drawn by an AI agent for make.fun\u2019s "
           "news-image-20261122 bounty. All stories checked against wire reports.",
           font=f_f, fill=GREY)

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print("saved", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
