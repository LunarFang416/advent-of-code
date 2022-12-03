import pytest
import os

def compute(s: str) -> int:
	_sum, s = 0, s.strip().split('\n')
	for i in range(0, len(s), 3):
		s1, s2, s3 = set(s[i]), set(s[i + 1]), set(s[i + 2])
		for j in s3.intersection(s1.intersection(s2)):
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
	[(_INPUT, 70)],
)
def test_computer(_input, expected): assert compute(_input) == expected

def main() -> int:
	with open(f"{os.path.join(os.path.dirname(__file__))}/input.txt") as f: print(compute(f.read()))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
	
