import pytest
import os

INPUT_TXT = f"{os.path.join(os.path.dirname(__file__))}/input.txt"

def compute(s: str) -> int:
	_set = set([(0, 0)])
	pos = [[0, 0].copy() for _ in range(10)]
	for cmd in s.strip().splitlines():
		c, dir = cmd.split()
		for _ in range(int(dir)):
			if c == "U": pos[0][0] = (pos[0][0] - 1) 
			elif c == "D": pos[0][0] = (pos[0][0] + 1)
			elif c == "L": pos[0][1] = (pos[0][1] - 1) 
			else: pos[0][1] = (pos[0][1] + 1) 
			i = 0
			while i < len(pos) - 1:
				if abs(pos[i + 1][0] - pos[i][0]) == 2 and abs(pos[i+1][1] - pos[i][1]) == 2:
					pos[i+1] = [(pos[i][0] + pos[i+1][0]) // 2, (pos[i][1] + pos[i+1][1]) // 2]
				elif abs(pos[i + 1][0] - pos[i][0]) == 2:
					pos[i+1] = [(pos[i][0] + pos[i+1][0]) // 2, pos[i][1]]
				elif abs(pos[i + 1][1] - pos[i][1]) == 2:
					pos[i+1] = [pos[i][0], (pos[i][1] + pos[i+1][1]) // 2]
				else: break
				i += 1
				_set.add(tuple(pos[-1]))

	return len(_set)

_INPUT = """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

_EXPECTED = 36

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
	
