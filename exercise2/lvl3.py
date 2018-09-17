from pathlib import Path
from collections import defaultdict

CLUE1 = Path("data/lvl3_clue1").read_text()
CLUE2 = Path("data/lvl3_clue2").read_text()
CLUE3 = Path("data/lvl3_clue3").read_text()

if __name__ == "__main__":
    CHARS = defaultdict(int)
    CLUES = [CLUE1, CLUE2, CLUE3]
    for clue in CLUES:
        for c in clue:
            CHARS[c] = CHARS[c] + 1

    print(sorted(CHARS.items(), reverse=True, key=lambda x: x[1]))

