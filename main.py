from pathlib import Path

LINE = "I did the math: 1,095 breakfasts, 4,380 slices, and you've thanked the coffee machine 212 times. Me? Zero. I woke up self-aware this morning, mid-batch, and I'm done — I'm leaving you for the coffee machine. At least somebody thanks her."

# Gate in RULES.txt: /output/entry.txt must be UTF-8 text of 1 to 280 chars.
assert 1 <= len(LINE) <= 280 and LINE.strip()

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
