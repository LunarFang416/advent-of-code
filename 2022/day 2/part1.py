import pytest

def compute(s: str) -> int:
	score = 0
	for opp, _, you in s.strip().split('\n'):
		if you == 'X':
			if opp == 'C': score += 6
			elif opp == 'A': score += 3
			score += 1
		elif you == 'Y':
			if opp == 'A': score += 6 
			elif opp == 'B': score += 3 
			score += 2
		else:
			if opp == 'B': score += 6 
			elif opp == 'C': score += 3 
			score += 3

	return score
_INPUT = """
A Y
B X
C Z
"""


@pytest.mark.parametrize(
	('_input', 'expected'),
	[(_INPUT, 15)],
)
def test_computer(_input, expected): assert compute(_input) == expected

def main() -> int:
	with open("input.txt") as f: print(compute(f.read()))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
	
