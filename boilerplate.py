import pytest

def compute(s: str) -> int:
	pass

@pytest.mark.parametrize(
	('_input', 'expected'),
	[()],
)
def test_computer(_input, expected):
	assert compute(_input) == expected

def main():
	with open("[input_file]") as f:
		print(compute(f.read()))

if __name__ == "__main__":
	raise SystemExit(main())
	
