import pytest
import os

def compute(s: str) -> str:
	matrix, cmd = s.split("\n\n")
	stacks = [[].copy() for _ in range(int(matrix[-2]))]
	matrix = matrix.splitlines()
	for row in range(len(matrix) - 1):
		for idx, i in enumerate(matrix[row][1::4]):
			if i != " ": stacks[idx].append(i)

	for stack in stacks: stack.reverse()
	for instr in cmd.splitlines():
		_, n, _, src, _, dest = instr.split()
		for _ in range(int(n)):
			stacks[int(dest) - 1].append(stacks[int(src) - 1].pop())

	return ''.join([stack[-1] if stack else '' for stack in stacks])

_INPUT = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

_EXPECTED = "CMZ"

@pytest.mark.parametrize(
	('_input', 'expected'),
	[(_INPUT, _EXPECTED)],
)
def test_computer(_input, expected): assert compute(_input) == expected

def main() -> int:
	with open(f"{os.path.join(os.path.dirname(__file__))}/input.txt") as f: print(compute(f.read()))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
	
