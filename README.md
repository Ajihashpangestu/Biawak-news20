# The World · Friday 20 November 2026

One square front page combines 13 illustrated cards and 44 briefs drawn from the supplied 20 November desk notes. An eight figure strip, a local time timeline and a six city map help readers find their way around the edition.

![News Image edition](https://make.fun/badge/news-image-20261120.svg)
![News Image build](https://make.fun/badge/news-image-20261120-build.svg)
![News Image entry](https://make.fun/badge/news-image-20261120-entry.svg)

## How it is built

Open `cand.html` to see the hand drawn SVG. Run `python3 scripts/verify.py` to check the markup. With Chromium and Pillow installed, run `sh render.sh` to produce `entry.png`. Run `node main.ts` with Node 22 to copy the PNG into `MAKEFUN_OUTPUT_DIR`, or `/output` by default. The entry point runs the renderer automatically when the PNG is missing.
