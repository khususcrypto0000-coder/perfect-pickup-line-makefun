"""Entry for the make.fun bounty "The Perfect Pickup Line".

Writes a single original pickup line to /output/entry.txt.
Deterministic: every run produces the exact same bytes.
"""

import os

PICKUP_LINE = "I saved this line as a draft a thousand times \u2014 then you showed up, and I finally hit send."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Bounty gate: one line, 1-200 characters, no trailing newline.
    assert 1 <= len(PICKUP_LINE) <= 200, "pickup line must be 1-200 characters"
    assert "\n" not in PICKUP_LINE, "pickup line must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(PICKUP_LINE)


if __name__ == "__main__":
    main()
