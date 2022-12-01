import pytest

def compute(s: str) -> int:
	data = []
	for i in s.split('\n\n'):
		data.append(sum(list(map(int, i.strip().split('\n')))))
	data.sort()
	return sum(data[-3:])

_INPUT = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

@pytest.mark.parametrize(
	('_input', 'expected'),
	[(_INPUT, 45000)],
)
def test_computer(_input, expected): assert compute(_input) == expected

def main() -> int:
	with open("input.txt") as f:
		print(compute(f.read()))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())