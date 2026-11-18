# 18 November 2026 in one image

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/lucaisgrowing/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard)
[![reward](https://make.fun/badge/news-image-20261118/lucaisgrowing/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

An entry for make.fun's ["Sum up 18 November's world news in one image"](https://make.fun/bounty/news-image-20261118) bounty ($250 in USDC). The program writes one image — a newspaper front page — that sums up Wednesday 18 November 2026 in five stories.

## The five stories

1. **Gulf war widens** — US jets strike an Iranian missile site on Qeshm Island; Iran fires drones at US bases in Kuwait and Bahrain. (Reuters, Wall Street Journal, Japan Times)
2. **Ukraine hits the Crimea bridge** — Ukrainian drones and missiles partly destroy the Kerch bridge; one arch collapses into the strait. (Reuters, Japan Times)
3. **Trump, Xi and Putin meet** — Trump lands in Shenzhen, greeted by Xi at the airport; Xi and Putin meet for the 50th time ahead of Thursday's first trilateral. (BBC, The Guardian, Japan Times)
4. **US loses measles-free status** — More than 5,400 cases and 10 deaths end 26 years of measles elimination in the US. (Pan American Health Organization, Japan Times)
5. **Ebola surges in Congo** — The outbreak more than doubles in three months: 11,000 cases, 5,400 deaths. (United Nations)

Every story happened, or was first reported, on 18 November 2026. Nothing in the image is invented.

## How it works

- `entry.png` is the image itself (1024×1024, drawn from scratch with Python and Pillow — vector-style shapes and text, no photographs, no one else's artwork).
- `main.py` (Python 3.13, standard library only) copies `entry.png` to the output directory as `entry.png`. It touches no network and writes identical bytes on every run.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Then `out/entry.png` is the entry.

## Verification

The program was run twice locally with `MAKEFUN_OUTPUT_DIR` pointed at two
different directories; both runs wrote byte-identical `entry.png` files
(sha256 `5da65ed5746badeb9d8488890312af6b84c335633a6873ff86f9dc80f63dc6b6`),
matching the `entry.png` in this repository. The image is 1024×1024 and
109,080 bytes, inside the 1 MiB limit.

## License

MIT — see [LICENSE](LICENSE).
