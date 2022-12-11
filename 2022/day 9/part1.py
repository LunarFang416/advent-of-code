import pytest
import os

INPUT_TXT = f"{os.path.join(os.path.dirname(__file__))}/input.txt"

def compute(s: str) -> int:
	_set = set([(0, 0)])
	t_pos, h_pos = [0, 0], [0, 0]
	for cmd in s.strip().splitlines():
		c, dir = cmd.split()
		for _ in range(int(dir)):
			if c == "U": h_pos[0] = (h_pos[0] - 1) 
			elif c == "D": h_pos[0] = (h_pos[0] + 1)
			elif c == "L": h_pos[1] = (h_pos[1] - 1) 
			else: h_pos[1] = (h_pos[1] + 1) 
			if abs(h_pos[0] - t_pos[0]) > 1 or abs(h_pos[1] - t_pos[1]) > 1:
				t_pos = [h_pos[0], h_pos[1]]
				if c == "U": t_pos[0] = (h_pos[0] + 1) 
				elif c == "D": t_pos[0] = (h_pos[0] - 1)
				elif c == "L": t_pos[1] = (h_pos[1] + 1)
				else: t_pos[1] = (h_pos[1] - 1) 
			_set.add(tuple(t_pos))

	return len(_set)

_INPUT = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

_EXPECTED = 13

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
	
