#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes the monologue to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
The monologue is 100 words, 510 characters: a dark lord mid-ritual, losing
the demon's name — tiredness in the rhythm, the pauses, the small
deflections, never in a plain statement that he is weary.
"""
import os

ENTRY = (
    "Light the candles. No — the chalk first. The circle was... "
    "I have drawn this circle forty-one times, and the choir knows the words "
    "better than I do now. They wait for the third verse. The choir clears "
    "its throat. The third verse is the name. His name. It sat on my tongue "
    "a moment ago. Mar... Mal... The dark leans out and says it for me, "
    "patient as a clerk. He has waited three hundred years. He can wait "
    "while I... where was I? Ah. The candles. Begin again, my lord, says "
    "the dark. And it sounds almost kind."
)


def main():
    # Bounty gate: /output/entry.txt must be UTF-8 text of 1 to 600 characters.
    assert 1 <= len(ENTRY) <= 600, f"entry length {len(ENTRY)} outside 1-600 gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY.split())} words, {len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
