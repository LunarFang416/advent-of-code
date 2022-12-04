import pytest
import os

def compute(s: str) -> int:
	count = 0
	for line in s.strip().split('\n'):
		p1, p2 = line.split(',')
		a, b = list(map(int, p1.split('-')))
		c, d = list(map(int, p2.split('-')))
		if a <= c and b >= d: count += 1
		elif c <= a and d >= b: count += 1
	return count

_INPUT = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

@pytest.mark.parametrize(
	('_input', 'expected'),
	[(_INPUT, 2)],
)
def test_computer(_input, expected): assert compute(_input) == expected

def main() -> int:
	with open(f"{os.path.join(os.path.dirname(__file__))}/input.txt") as f: print(compute(f.read()))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
	
