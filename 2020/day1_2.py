import pytest

from itertools import combinations
def compute(s: str) -> int:
	l = list(map(int, s.strip().split("\n")))
	for x, y in combinations(l, 2):
		if 2020 - x - y in l: return x * y * (2020 - x - y)

_INPUT = """
1721
979
366
299
675
1456
"""

@pytest.mark.parametrize(
	('_input', 'expected'),
	[(_INPUT, 241861950)],
)
def test_computer(_input, expected):
	assert compute(_input) == expected

def main():
	with open("day1input.txt") as f:
		print(compute(f.read()))

if __name__ == "__main__":
	raise SystemExit(main())
	
