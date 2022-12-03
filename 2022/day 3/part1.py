import pytest
import os

def compute(s: str) -> int:
	_sum = 0
	for sack in s.strip().split('\n'):
		s1, s2 = set(sack[:len(sack) // 2]), set(sack[len(sack) // 2:])
		for j in s1.intersection(s2):
			if j.islower(): _sum += ord(j) - ord('a') + 1
			else: _sum += ord(j) - ord('A') + 27

	return _sum

_INPUT = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

@pytest.mark.parametrize(
	('_input', 'expected'),
	[(_INPUT, 157)],
)
def test_computer(_input, expected): assert compute(_input) == expected

def main() -> int:
	with open(f"{os.path.join(os.path.dirname(__file__))}/input.txt") as f: print(compute(f.read()))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
	
