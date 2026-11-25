#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny single line, spoken by a hopeless tech support agent
to a desperate customer, to /output/entry.txt.

The joke: the classic "turn it off and on again" is twisted into a
cheerful confession — it is the only thing the agent knows how to do.
The humour comes from the agent's cheerful uselessness, never at the
customer's expense. "No rush" lands ironically: the customer is clearly
in a hurry, so their desperation is felt, never explained.

Usage:
    python3 main.py                 # writes /output/entry.txt
    python3 main.py <output-path>   # writes to a custom path (local testing)
"""

import sys
from pathlib import Path

ENTRY = "Have you tried turning it off and on again? No rush, it's also the last thing I know how to do."


def main() -> None:
    output_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    text = ENTRY
    assert 1 <= len(text) <= 199, f"entry is {len(text)} chars, must be 1-199"
    assert text.strip(), "entry must not be only whitespace"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {output_path}")


if __name__ == "__main__":
    main()
