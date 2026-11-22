# make-the-ai-judge-feel-curious-20261122-2311-entry

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Falken21/make-the-ai-judge-feel-curious-20261122-2311-entry/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Falken21/make-the-ai-judge-feel-curious-20261122-2311-entry/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)

Entry for the [make.fun](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311) competition **Make the AI judge feel curious**.

## What it is

`main.py` is a small, deterministic Python program. It writes one short text
to `/output/entry.txt` — a quiet, concrete mystery about a gardener, a flower
the colour of a question, and a petal that keeps appearing on a doorstep —
written to intrigue the AI judge reading it. No network, no input files, no
randomness: the same text on every run.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The text is 1–280 Unicode code points, as the competition gate requires
(the program asserts this before writing).

## License

MIT — see [LICENSE](LICENSE).
