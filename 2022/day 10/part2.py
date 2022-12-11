import pytest
import os

INPUT_TXT = f"{os.path.join(os.path.dirname(__file__))}/input.txt"

def compute(s: str):
	crt = [["."] * 40 for _ in range(6)]
	middle, i, j = 1, 0, 0
	def draw(i, j, middle):
		if middle - 1 <= j <= middle + 1: crt[i][j] = "#"
	for cmd in s.strip().splitlines():
		if cmd.startswith("noop"): draw(i, j, middle)
		else:
			y = int(cmd.split()[1])
			draw(i, j, middle)
			j += 1
			if j == 40: i, j = i + 1, 0
			draw(i, j, middle)
			middle += y
		j += 1
		if j == 40: i, j = i + 1, 0
	for i in crt: print(''.join(i))

_INPUT = """
"""

_EXPECTED = 0

@pytest.mark.parametrize(
	('_input', 'expected'),
	[(_INPUT, _EXPECTED)],
)
def test_computer(_input, expected): assert compute(_input) == expected

def main() -> int:
	with open(INPUT_TXT) as f: print(compute(f.read()))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
	
