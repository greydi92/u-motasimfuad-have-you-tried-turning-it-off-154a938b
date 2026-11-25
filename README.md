# Have You Tried Turning It Off?

make.fun bounty `u-motasimfuad-have-you-tried-turning-it-off-154a938b` — one funny single line a hopeless tech support agent says to a desperate customer. Reward $10 total, top-10 split. Deadline 2026-11-26 04:25 WIB.

## The entry

```
Have you tried turning it off and on again? No rush, it's also the last thing I know how to do.
```

- **Character count:** 95 (gate: 1–199, UTF-8, not only whitespace)
- **The joke:** the classic "turn it off and on again" is twisted into a cheerful confession — it is the only thing the agent knows how to do. The humour comes from the agent's cheerful uselessness; the customer is never the butt of it. "No rush" lands ironically against a desperate customer, so their desperation is felt, never explained. (Iterate round 1 replaced the builder's line — "Could you turn it off and on again, nice and slow? I need the time to Google what that error means." — whose "agent Googles it too" twist is a common IT-comedy trope other entries may share.)

## How to run

```sh
python3 main.py                 # writes /output/entry.txt
python3 main.py <output-path>   # writes to a custom path (local testing)
```

## What the program does

`main.py` holds the entry text as a constant, asserts it is 1–199 characters and not only whitespace, then writes it verbatim (UTF-8, no trailing newline) to `/output/entry.txt`. No network, no input files, fully deterministic.

## Verification

```sh
python3 main.py /tmp/test-entry.txt
wc -c /tmp/test-entry.txt   # 95
cat /tmp/test-entry.txt
```

Local check passed: output is exactly the entry above, 95 characters.
There is no local grader in this kit — the server grades every entry (RULES.txt: "This is a program/v1 competition: its scorer and reference data stay on the server").
