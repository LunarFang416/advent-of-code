import pytest

def compute(s: str) -> int:
	pass

@pytest.mark.parametrize(
	('_input', 'expected'),
	[()],
)
def test_computer(_input, expected): assert compute(_input) == expected

def main() -> int:
	with open("day[]input.txt") as f:
		print(compute(f.read()))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
	
