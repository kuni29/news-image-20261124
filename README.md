# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/kuni29/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/kuni29/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image that sums up the world news of Tuesday 24 November 2026, drawn as a newspaper front page in a graphic-recording style. The hero is a two-panel diptych: an empty negotiation table in Abu Dhabi — snapped pencil, handshake that never meets, a NO DEAL stamp — beside a night city under a drone swarm, its power grid going dark, headlined by the night's big number, 160+ missiles and drones. A "how today connects" arrow flow links the failed talks to the strikes and the Nvidia turmoil to the Nikkei's +5% AI rally. Two more hero stories (the Nikkei surge to 58,676; a suspected North Korean aircraft breaching South Korean airspace over Ulleung island), three mid stories (Nvidia CEO Jensen Huang under board and FBI scrutiny; the UN's call for a Benghazi probe; Russia's warning to Estonia), a labelled atlas strip marking ten places where the day happened, and 24 one-line briefs from every region — 30 stories in all, each colour-coded by category with a legend. Every story was first reported on 24 November 2026; stories first reported on 23 November (the EU's 22nd sanctions package, the COP31 collapse, the US House majority, the Benghazi strike itself, the Women's World Cup hosts) were deliberately left out, and the page carries a DATE-CHECKED stamp. The picture is designed in `design.html` with hand-drawn inline SVG illustrations and rendered to `entry.png` by `render.mjs` (headless Chrome), so every word is typeset, not generated: no garbled text. `main.py` delivers the image bytes to the output directory, unchanged on every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.png` (1024×1024 PNG, under the 1 MiB cap).

---
<sub>Entered on [make.fun](https://make.fun/?ref=sjptyjw4&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
