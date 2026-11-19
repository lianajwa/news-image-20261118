# The World in One Day — Wednesday 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/lianajwa/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard)
[![reward](https://make.fun/badge/news-image-20261118/lianajwa/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

One image that sums up the world's news of Wednesday 18 November 2026:
**52 stories, 7 regions, 16 drawn illustrations** — each lead has a picture
drawn for it, the world map pins every story on land, and every number is
date-checked.

## What happened that day

- **Xi greets Trump in Shenzhen** — Xi embraces Trump at the airport; Putin
  joins them. A first-ever trilateral summit follows on Thursday.
- **US strikes Qeshm Island; Iran hits Kuwait & Bahrain** — US jets hit a
  Revolutionary Guard missile site in the Strait of Hormuz; Iran answers
  with drone attacks on US sites at Ali Al Salem (Kuwait) and Sheikh Isa
  (Bahrain).
- **Anthropic prices its IPO at $83** — 825m shares, $81bn raised, a record
  IPO at ~$1.5tn; trading starts Thursday on Nasdaq as ANT.
- **Voyager 1 reaches one light-day** — NASA's probe crosses one light-day
  from Earth at 05:16 ET, 49 years after its 1977 launch.
- **Nvidia beats, shares fall** — Q3 revenue $115.8bn beats forecasts, but
  shares fall 2.9% as Jensen Huang's exit weighs.
- **Peltola wins Alaska's Senate race** — Democrat Mary Peltola beats Dan
  Sullivan; Democrats take 56 Senate seats.
- **US loses measles-elimination status**, the EU proposes a €45bn loan for
  Ukraine, the Crimean Bridge is hit again, Fed minutes point to a December
  hike, Cyclone Akvan bears down on India's Andhra coast, Google unveils
  Gemini 4 Neon, the Dow falls 1.11% while the Nasdaq ends its slide, and
  Waymo pulls its driverless rides from US freeways — plus briefs 17–52.

## How the image is built

`render.py` (Python 3, standard library + Pillow) draws the whole front
page: masthead, by-the-numbers strip, a world map projected from real
latitude/longitude with every pin on land (leader lines where pins crowd),
16 hand-drawn illustration scenes — a Shenzhen skyline, Gulf drones at
night, a warship off Qeshm, the $83 IPO sign, Voyager in deep space, a
falling Nvidia chart, Alaskan mountains, measles viruses, Manila flags,
the EU stars, a broken bridge, the Fed's columns, a cyclone spiral,
Gemini's spark, market candlesticks, a Waymo on a closed freeway — then
briefs 17–52 and a sources footer.

`main.py` validates `entry.png` (PNG, 1024×1024, ≤1 MiB) and copies it to
the output path, so both runs write the same bytes.

## Run it

```sh
python3 render.py          # regenerates entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Sources

Reuters, AP, AFP, BBC, Al Jazeera, CNN, NYT — every story dated
18 November 2026.
