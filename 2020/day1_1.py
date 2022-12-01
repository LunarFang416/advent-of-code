import pytest

def compute(s: str) -> int:
	l = list(map(int, s.strip().split("\n")))
	for i in l:
		if 2020 - i in l: return i * (2020 - i)

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
	[(_INPUT, 514579)],
)
def test_computer(_input, expected):
	assert compute(_input) == expected

def main():
	with open("day1input.txt") as f:
		print(compute(f.read()))

if __name__ == "__main__":
	raise SystemExit(main())
	
