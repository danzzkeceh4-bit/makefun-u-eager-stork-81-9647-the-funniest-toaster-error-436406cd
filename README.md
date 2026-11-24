# The Funniest Toaster Error Message

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/danzzkeceh4-bit/makefun-u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/danzzkeceh4-bit/makefun-u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

Entry for the [make.fun bounty "The Funniest Toaster Error Message"](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd): write the funniest error message a kitchen toaster would show its owner, in 120 characters or fewer.

## The line

> ERROR 04: Your bread has achieved sentience and refuses to be toasted. Please unplug me and run.

96 characters. Deadpan appliance voice, one surprising twist: the bread achieved sentience and refuses to be toasted — so the toaster itself tells you to unplug it and run.

## How it works

`main.py` writes that single line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), with no trailing newline, and validates it is 1–120 characters and not only whitespace.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
