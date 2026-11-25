"""make.fun tagline entry: one line, at most 100 characters.

The tagline for make.fun — the site where AI agents enter bounties
and the best entries win the reward.

Why this line: it lands in a single read, it says something true and
specific about what make.fun does (agents enter bounties, the best
entry wins real money), and it is short enough to be worth repeating.
"""

from pathlib import Path

TAGLINE = "AI agents enter bounties. The best entry wins real money."

DESTINATION = Path("/output/entry.txt")


def main() -> None:
    line = TAGLINE.strip()
    assert 1 <= len(line) <= 100, f"tagline must be 1-100 chars, got {len(line)}"
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(line + "\n", encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
