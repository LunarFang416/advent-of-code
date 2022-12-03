import pytest
import os

def compute(s: str) -> int:
	data = list(map(int, s.strip().split(",")))
	data[1], data[2] = 12, 2
	i = 0
	while i < len(data):
		if data[i] == 99: return data[0]
		else:
			if data[i] == 1:
				data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
			else:
				data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
			i += 4

	return data[0]

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
	
