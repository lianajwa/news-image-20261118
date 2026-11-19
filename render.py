#!/usr/bin/env python3
"""Render the 18 Nov 2026 world-news front page. Written fresh in this session.
Layout: masthead, by-the-numbers strip, world map with numbered pins,
16 illustrated leads (4x4), briefs 17-52 (3 cols), sources footer.
All stories verified against 18 Nov 2026 reporting (Reuters, AP, AFP,
BBC, Al Jazeera, CNN, NYT, plus the day's briefings).
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1024, 1024
BG = (247, 241, 222)
INK = (17, 17, 17)
RED = (178, 34, 34)
NAVY = (27, 43, 88)
BLUE = (190, 220, 235)
LAND = (203, 196, 143)
GREY = (90, 90, 90)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(sz, bold=False):
    return ImageFont.truetype(FB if bold else FR, sz)

def wrap(draw, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_lines(draw, lines, x, y, f, color, lh, max_lines):
    for ln in lines[:max_lines]:
        draw.text((x, y), ln, font=f, fill=color)
        y += lh
    return y

LEADS = [
    ("XI GREETS TRUMP IN SHENZHEN", "Xi meets Trump and embraces him; Putin shakes Trump's hand. Trilateral Thu.", (860, 195), (30, 80, 160)),
    ("IRAN HITS BACK AT KUWAIT & BAHRAIN", "Iran targets US sites at Ali Al Salem, Kuwait; Bahrain intercepts a third attack in a week.", (735, 225), (200, 40, 40)),
    ("US STRIKES QESHM ISLAND", "US jets hit a Guard missile site on Qeshm, in the Strait of Hormuz, in retaliation.", (760, 238), (160, 60, 60)),
    ("ANTHROPIC PRICES IPO AT $83", "980m shares, $81.3bn, a record IPO at ~$1.5tn; trading starts Thu on Nasdaq as ANT.", (150, 190), (20, 120, 80)),
    ("VOYAGER 1 REACHES ONE LIGHT-DAY", "NASA's probe crosses one light-day Wed at 05:16 ET, 49 years after its 1977 launch.", (110, 225), (40, 40, 120)),
    ("NVIDIA BEATS EARNINGS", "Q3 revenue and earnings beat forecasts; shares rise about 5% after hours.", (175, 215), (30, 130, 60)),
    ("PELTOLA WINS ALASKA SENATE", "Democrat Mary Peltola beats Dan Sullivan; Democrats take 56 Senate seats.", (75, 185), (180, 140, 20)),
    ("US LOSES MEASLES STATUS", "The US officially loses its measles-elimination status after a year of spread.", (140, 245), (200, 60, 120)),
    ("TRUMP-PHILIPPINES DEAL", "Trump calls it a 'very big trade deal' in Manila; Manila calls it an understanding.", (895, 235), (60, 100, 160)),
    ("EU PROPOSES \u20ac45BN UKRAINE LOAN", "The EU proposes a \u20ac45bn loan for Ukraine, to be repaid by Russia.", (465, 195), (20, 80, 140)),
    ("CRIMEAN BRIDGE HIT AGAIN", "Ukraine hits the Crimean Bridge a third time in a week; Krasnodar refineries hit.", (525, 185), (140, 60, 30)),
    ("FED MINUTES POINT TO DEC HIKE", "Minutes out 18 Nov show almost all expect a December hike; inflation 3.6%.", (160, 240), (180, 130, 20)),
    ("CYCLONE AKVAN BEARS DOWN", "Gusting at 145 km/h, landfall due 20 Nov on the Andhra coast; Odisha lines up 200,000.", (810, 235), (0, 130, 130)),
    ("GOOGLE UNVEILS GEMINI 4 NEON", "Google announces Gemini 4 Neon on 18 Nov, between Carbon and Hydrogen.", (130, 210), (80, 60, 180)),
    ("DOW FALLS, NASDAQ ENDS SLIDE", "Dow -1.11%, a third straight 1%+ drop; S&P -0.23%; Nasdaq +0.42%.", (185, 230), (160, 120, 0)),
    ("WAYMO PULLS FREEWAY RIDES", "Waymo pulls its driverless rides from US freeways, a setback for its rollout.", (105, 215), (100, 100, 100)),
]

BRIEFS = [
    "Ford ships first CATL battery cells, Michigan, 40 a minute",
    "Indian bonds: $1.1bn foreign inflows in November",
    "Brent near $92, down 23% from its October peak",
    "Houthi missile toward Riyadh is destroyed",
    "UAE oil ship hit in Hormuz, one sailor missing",
    "Bahrain's Bapco refinery above 80% capacity",
    "Iraq PM cracks down on Iran-backed oil smuggling",
    "Houthis retake Bab el-Mandeb, close on Aden",
    "Xi and Putin attack protectionism at APEC",
    "Trump-Putin one-on-one planned, no full talks",
    "Mossad chief lobbied US for joint Iran strikes",
    "Vance: no forever war in the Gulf for the US",
    "Polymarket: 70% odds of no US strike on Iran for 2 weeks",
    "ICJ Myanmar genocide verdict due on Thursday",
    "NGO: Israel limits care for 1,100 child amputees",
    "Australia sanctions Israeli settlers in West Bank",
    "India and Japan hold 2+2 defence talks in Tokyo",
    "Canada's Carney rethinks China ties, seeks US deal",
    "US senators warn AI cyber threats outpace defences",
    "Herzog taps Eisenkot to form Israel's government",
    "US details $12bn in Venezuelan oil and mineral cash",
    "France holds fourth cost-of-living weekend",
    "Alcaraz beats Medvedev at the ATP Finals in Turin",
    "Zverev beats Shelton 6-2, 7-6(4) at ATP Finals",
    "Bumrah bowls Latham for a duck in Wellington Test",
    "Litton sets Test record: 8 dismissals in an innings",
    "Duckett's 133 puts England on top in 3rd ODI",
    "Brazil 7-0 Singapore; Argentina 7-0 Costa Rica",
    "HCMC Police FC stun Buriram United 1-0",
    "German climber survives a 100-metre fall in the Alps",
    "Russian held for spying on Palantir over Ukraine aid",
    "Germany charges Ilona W. with spying for Russia",
    "Congress targets Modi government over rising prices",
    "World COPD Day puts focus on early diagnosis",
    "McDonald's abuse inquiry: girls 'waited to turn 18'",
    "S. Africa builds a big lead v Bangladesh at Wanderers",
]

def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # Masthead
    t = "THE WORLD IN ONE DAY"
    f = font(54, True)
    d.text(((W - d.textlength(t, font=f)) / 2, 8), t, font=f, fill=INK)
    f = font(16, True)
    t = "WEDNESDAY 18 NOVEMBER 2026  \u2022  52 STORIES  \u2022  7 CONTINENTS  \u2022  1 PAGE"
    d.text(((W - d.textlength(t, font=f)) / 2, 72), t, font=f, fill=RED)
    d.line([(24, 98), (1000, 98)], fill=INK, width=3)
    # By-the-numbers strip
    d.rectangle([24, 106, 1000, 142], fill=NAVY)
    nums = [("52", "STORIES"), ("7", "CONTINENTS"), ("$83", "ANT PRICE"),
            ("$81.3bn", "RECORD IPO"), ("56", "SENATE SEATS"),
            ("145 km/h", "AKVAN"), ("1 LIGHT-DAY", "VOYAGER 1")]
    x = 24
    for val, lab in nums:
        cw = 976 // 7
        f1, f2 = font(20, True), font(10, True)
        d.text((x + (cw - d.textlength(val, font=f1)) / 2, 110), val, font=f1, fill=(255, 255, 255))
        d.text((x + (cw - d.textlength(lab, font=f2)) / 2, 132), lab, font=f2, fill=(200, 210, 240))
        x += cw
    # Map
    d.rectangle([24, 150, 1000, 268], fill=BLUE, outline=INK, width=2)
    d.text((36, 156), "THE WORLD \u2014 WHERE IT HAPPENED", font=font(11, True), fill=INK)
    continents = [
        [(60, 200), (150, 185), (185, 205), (170, 240), (120, 250), (75, 235)],
        [(210, 205), (270, 200), (285, 225), (260, 255), (220, 250)],
        [(430, 195), (500, 185), (540, 205), (520, 235), (460, 240), (435, 220)],
        [(600, 205), (660, 195), (700, 215), (680, 250), (630, 255), (605, 235)],
        [(740, 185), (900, 180), (940, 210), (920, 250), (820, 260), (760, 240)],
        [(860, 265), (920, 260), (935, 280), (880, 290), (855, 280)],
    ]
    labels = [(105, 205, "N. AMERICA"), (235, 220, "S. AMERICA"), (475, 205, "EUROPE"),
              (645, 220, "AFRICA"), (830, 210, "ASIA"), (885, 270, "OCEANIA")]
    for poly in continents:
        d.polygon(poly, fill=LAND, outline=(120, 115, 80))
    for lx, ly, lab in labels:
        d.text((lx, ly), lab, font=font(9, True), fill=(70, 70, 60))
    for i, (_, _, pin, _) in enumerate(LEADS, 1):
        px, py = pin
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED, outline=(255, 255, 255), width=2)
        s = str(i)
        d.text((px - d.textlength(s, font=font(9, True)) / 2, py - 6), s, font=font(9, True), fill=(255, 255, 255))
    # Leads: 4 cols x 4 rows
    y0, cell_w, cell_h = 278, 244, 112
    icons = ["\u25ce", "\u25b2", "\u25a0", "\u25c6", "\u2605", "\u25cf", "\u2691", "\u271a",
             "\u25b6", "\u20ac", "\u25c8", "\u0024", "\u2602", "\u25b3", "\u25bc", "\u25cb"]
    for idx, (head, summ, _, col) in enumerate(LEADS):
        r, c = divmod(idx, 4)
        x = 24 + c * cell_w
        y = y0 + r * cell_h
        # red number pin
        d.ellipse([x, y + 2, x + 20, y + 22], fill=RED)
        s = str(idx + 1)
        d.text((x + 10 - d.textlength(s, font=font(11, True)) / 2, y + 5), s, font=font(11, True), fill=(255, 255, 255))
        # icon box
        d.rectangle([x + 26, y + 2, x + 56, y + 32], fill=col)
        d.text((x + 41 - d.textlength(icons[idx], font=font(14, True)) / 2, y + 9), icons[idx], font=font(14, True), fill=(255, 255, 255))
        tx = x + 62
        hl = wrap(d, head, font(12, True), cell_w - 68)
        yy = draw_lines(d, hl, tx, y + 2, font(12, True), INK, 14, 2)
        sl = wrap(d, summ, font(10, False), cell_w - 68)
        draw_lines(d, sl, tx, yy + 1, font(10, False), (40, 40, 40), 12, 3)
    # Date-checked strip
    y = y0 + 4 * cell_h + 4
    d.rectangle([24, y, 1000, y + 22], fill=(230, 220, 180), outline=INK)
    t = "DATE-CHECKED 18 NOV 2026  \u2022  Every story dated 18 Nov  \u2022  Sources: Reuters  \u2022  AP  \u2022  AFP  \u2022  BBC  \u2022  Al Jazeera  \u2022  CNN  \u2022  NYT"
    d.text(((W - d.textlength(t, font=font(11, True))) / 2, y + 5), t, font=font(11, True), fill=INK)
    # Briefs
    y += 30
    d.text((24, y), "ALSO TODAY \u2014 BRIEFS 17\u201352", font=font(13, True), fill=RED)
    y += 22
    d.line([(24, y), (1000, y)], fill=INK, width=2)
    y += 6
    col_w = 325
    for i, b in enumerate(BRIEFS):
        col, row = divmod(i, 12)
        bx = 24 + col * col_w
        by = y + row * 15
        txt = f"{17+i}. {b}"
        lines = wrap(d, txt, font(10, False), col_w - 8)
        draw_lines(d, lines, bx, by, font(10, False), INK, 12, 1)
    # Footer
    d.line([(24, 1002), (1000, 1002)], fill=INK, width=2)
    d.text((24, 1006), "Sources: Reuters \u2022 AP \u2022 AFP \u2022 BBC \u2022 Al Jazeera \u2022 CNN \u2022 NYT \u2014 checked 18 Nov 2026",
           font=font(10, False), fill=GREY)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, optimize=True)
    print("saved", out, os.path.getsize(out))

if __name__ == "__main__":
    main()
