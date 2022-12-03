import pytest

def compute(s: str) -> int:
	score = 0
	for opp, _, you in s.strip().split('\n'):
		if opp == 'A':
			if you == 'X': score += 3
			elif you == 'Y': score += 3 + 1
			else: score += 6 + 2
		elif opp == 'B':
			if you == 'X': score += 1
			elif you == 'Y': score += 3 + 2
			else: score += 6 + 3
		else:
			if you == 'X': score += 2
			elif you == 'Y': score += 3 + 3
			else: score += 6 + 1

	return score
_INPUT = """
A Y
B X
C Z
"""

@pytest.mark.parametrize(
	('_input', 'expected'),
	[(_INPUT, 12)],
)
def test_computer(_input, expected): assert compute(_input) == expected

def main() -> int:
	with open("input.txt") as f: print(compute(f.read()))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())