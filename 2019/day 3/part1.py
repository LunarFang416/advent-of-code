import pytest
import os

INPUT_TXT = f"{os.path.join(os.path.dirname(__file__))}/input.txt"

def compute(s: str) -> int:
	pass

_INPUT = """
"""

_EXPECTED = 0

@pytest.mark.parametrize(
	('_input', 'expected'),
	[(_INPUT, _EXPECTED)],
)
def test_computer(_input, expected): assert compute(_input) == expected

def main() -> int:
	with open(INPUT_TXT) as f: print(compute(f.read()))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
	
