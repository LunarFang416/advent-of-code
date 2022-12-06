import pytest
import os

def compute(s: str) -> int:
	src = list(map(int, s.strip().split(",")))
	for noun in range(100):
		for verb in range(100):
			data = src[:]
			data[1], data[2], i = noun, verb, 0
			while i < (len(data) - 3) and data[0] != 19690720:
				if data[i] == 99: break
				else:
					if data[i] == 1:
						data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
					else:
						data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
					i += 4
			if data[0] == 19690720: return 100 * noun + verb

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