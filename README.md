[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/lianajwa/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/lianajwa/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# The World in One Day — 18 November 2026

Entry for make.fun bounty **news-image-20261118** — "Sum up 18 November's
world news in one image" ($250, 50 places paid; deadline Fri 20 Nov 2026
00:00 UTC / 07:00 WIB).

## The image

A newspaper front page, drawn in this session with Pillow (`render.py`,
vector shapes + system fonts, so every word is spelled exactly as shown),
1024×1024 px, 106,753 bytes.

**Lead — The Gulf:** U.S. jets strike an IRGC missile site on Qeshm
Island; Iran fires drones at Bahrain and Kuwait; three U.S. carrier
groups in the region, Strait of Hormuz on alert.

**2 — Ukraine:** Ukraine hits the Kerch Bridge to Crimea for a second
day; a road span falls into the strait.

**3 — Shenzhen:** Xi Jinping opens the APEC summit in Shenzhen; Trump
and Putin join trilateral talks on Thursday (U.S., China and Russia
flags over the table).

**Also today:** Mary Peltola wins the Alaska Senate seat (Democrats
reach 56); Ebola outbreak in DR Congo — 11,000+ cases, 5,400 deaths;
Category 5 Cyclone Xavier hits the Cook Islands; a Russian military
plane crashes in Siberia, 19 killed. Footer: the U.S. loses its
measles-free status; a 6.0 quake in Papua New Guinea.

Sources checked 18 Nov 2026: CNN, CBS, Al Jazeera, The Guardian,
One Turn's daily brief, FeedCast — all converging on the same three
lead stories above.

## Program

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to `/output/entry.png`. No network, no time, no randomness —
two runs write identical bytes.

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
