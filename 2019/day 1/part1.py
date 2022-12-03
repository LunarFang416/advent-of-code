import pytest
import os

def compute(s: str) -> int:
	_sum = 0
	for i in s.strip().split('\n'):
		_sum += (int(i) // 3) - 2
	return _sum

@pytest.mark.parametrize(
	('_input', 'expected'),
	[()],
)
def test_computer(_input, expected): assert compute(_input) == expected

def main() -> int:
	with open(f"{os.path.join(os.path.dirname(__file__))}/input.txt") as f: print(compute(f.read()))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())