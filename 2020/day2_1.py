import pytest
import re
from collections import Counter

def compute(s: str) -> int:
	count = 0
	for line in s.strip().split("\n"):
		_min, _max, _l, _s = re.match(r"(\d+)-(\d+) (\w): (\w+)", line).groups()
		if int(_min) <= Counter(_s)[_l] <= int(_max): count += 1
	return count

_INPUT = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

@pytest.mark.parametrize(
	('_input', 'expected'),
	[(_INPUT, 2)],
)
def test_computer(_input, expected):
	assert compute(_input) == expected

def main():
	with open("day2input.txt") as f:
		print(compute(f.read()))

if __name__ == "__main__":
	raise SystemExit(main())
