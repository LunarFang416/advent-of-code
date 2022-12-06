import pytest
import os

INPUT_TXT = f"{os.path.join(os.path.dirname(__file__))}/input.txt"

def compute(s: str) -> int:
	s = s.strip()
	for i in range(len(s) - 13):
		if len(set(s[i:i+14])) == 14: return i + 14

_INPUT = """
bvwbjplbgvbhsrlpgdmjqwftvncz
"""

_EXPECTED = 23

@pytest.mark.parametrize(
	('_input', 'expected'),
	[(_INPUT, _EXPECTED)],
)
def test_computer(_input, expected): assert compute(_input) == expected

def main() -> int:
	with open(INPUT_TXT) as f: print(compute(f.read().strip()))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
	
