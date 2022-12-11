import pytest
import os

INPUT_TXT = f"{os.path.join(os.path.dirname(__file__))}/input.txt"

def compute(s: str) -> int:
	data = [list(map(int, i)) for i in s.strip().splitlines()]
	_set = set()
	def visibility(arr, v_adj = 0, h_adj = 0):
		nonlocal _set
		v_max = [-1 for i in range(len(arr[0]))]
		h_max = [-1 for i in range(len(arr))]
		for i in range(len(arr)):
			for j in range(len(arr[0])):
				if arr[i][j] > v_max[j]:
					_set.add((i if not h_adj else h_adj - i, j if not v_adj else v_adj - j))
					v_max[j] = arr[i][j]
				if arr[i][j] > h_max[i]:
					_set.add((i if not h_adj else h_adj - i, j if not v_adj else v_adj - j))
					h_max[i] = arr[i][j]
	
	visibility(data)
	visibility([i[::-1] for i in data[::-1]], len(data) - 1, len(data[0]) - 1)
	return len(_set)



_INPUT = """
30373
25512
65332
33549
35390
"""

_EXPECTED = 21

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
	
