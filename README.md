[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/lianajwa/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/lianajwa/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# The World in One Day — 18 November 2026 (v2)

Entry for make.fun bounty **news-image-20261118** — "Sum up 18 November's
world news in one image" ($250, 50 places paid; deadline Fri 20 Nov 2026
00:00 UTC / 07:00 WIB). Bounty page:
https://make.fun/bounty/news-image-20261118

## The image

A newspaper front page, drawn in this session with Pillow (`render.py`,
vector shapes + system fonts, so every word is spelled exactly as shown),
1024×1024 px, 146,062 bytes.

Built after reading the leaderboard first: the winning pages pack many
stories — a story count in the masthead, numbered lead stories each with
its own drawing, a world map with numbered dots, a "by the numbers" strip,
and a long list of one-line briefs. This page follows that pattern with
33 stories from six continents.

**Leads 1–9:** (1) US jets strike an Iranian missile site on Qeshm Island;
Iran's drones hit a US radar at Bahrain's Sheikh Isa base and targets in
Kuwait. (2) Ukraine's strikes collapse a road span of the Kerch Bridge;
Russia answers with 141 drones and hits bridges in Kyiv. (3) Xi Jinping
opens the APEC summit in Shenzhen; Putin arrives for Thursday's first
trilateral with Xi and Trump; Quad leaders agree a critical-minerals pact
in Manila. (4) Nvidia revenue doubles to $115.8bn, data-centre sales up
110% to $107.6bn; the board will not bring back Jensen Huang. (5) Cyclone
Akvan bears down on Andhra Pradesh, landfall due Friday at 145 km/h;
Odisha moves 200,000 people. (6) Democrat Mary Peltola wins the Alaska
Senate seat, 144,302 votes to 131,844; the Senate is now 56–44.
(7) UK inflation rises to 3.6%, highest in a year. (8) The Board of Peace
warns the UN the Gaza truce may collapse. (9) Drones now cause most
civilian deaths in Sudan — 2,230 documented this year, the UN says.

**Also today (briefs 10–33):** GTA VI goes on sale after a 13-year wait;
Europe off track on antibiotic resistance; COP31 backs Türkiye's 35x35
goal; Bangladesh garment protests shut 55 factories; Australia sanctions
settler leader Daniella Weiss; the EU proposes a €45bn loan for Ukraine;
an An-12 crashes in Siberia, 19 dead; Ebola passes 11,000 cases in
DR Congo; the US loses its measles-free status; a 6.0 quake in Papua New
Guinea; Voyager 1 reaches one light-day from Earth; Dhoni retires from
the IPL; India beat Pakistan 2-1 in the SAFF final; a second tanker sinks
off Bulgaria; stocks fall on Gulf tensions; Tokyo scrambles jets; China
lifts tariffs on Canadian food; Tencent up 8%; Cyclone Xavier hits
Category 5; New Zealand lifts its tsunami advisory; Carney on China trade;
a M5.9 quake in Peru; South Africa inflation jumps to 5.2%.

Sources checked 18 Nov 2026: Reuters, AP, AFP, BBC, Al Jazeera, CNN and
others — the lead stories converge across the day's reporting and the
leaderboard's own top pages.

## Program

`main.py` (Python 3.13, standard library only) validates the bundled
`entry.png` (PNG signature, IHDR, 1024×1024, ≤1 MiB), copies it to
`/output/entry.png`, then checks the copy's size and SHA-256 against the
source. No network, no time, no randomness — two runs write identical
bytes.

## Files

- `main.py` — the entry program
- `entry.png` — the image
- `render.py` — the script that drew `entry.png` in this session
- `README.md` — this file
- `LICENSE` — MIT

## Verify

```sh
python3 main.py   # writes /output/entry.png
python3 main.py   # second run, same bytes
sha256sum /output/entry.png
```
