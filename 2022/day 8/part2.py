import pytest
import os

INPUT_TXT = f"{os.path.join(os.path.dirname(__file__))}/input.txt"

def compute(s: str) -> int:
	_data = [list(map(int, i)) for i in s.strip().splitlines()]
	_max, _res = float("-inf"), [([1] * len(_data[0])).copy() for _ in range(len(_data))]
	def visibility(data, v_adj = 0, h_adj = 0):
		nonlocal _res
		v_max = [0 for _ in range(len(data[0]))]
		h_max = [0 for _ in range(len(data))]
		for i in range(len(data)):
			for j in range(len(data[0])):
				# if data[i][j] > data[v_max[j]][j]: v_score = 0
				v_score = abs(v_max[j] - i)

				# if data[i][j] > data[i][h_max[i]]: h_score = 0
				h_score = abs(h_max[i] - j)

				if data[i][j] >= data[v_max[j]][j]: 
					v_max[j] = i
				if data[i][j] >= data[i][h_max[i]]: h_max[i] = j

				if v_adj != 0: i, j = h_adj - i, v_adj - j
				_res[i][j] *= (h_score) * v_score

		print(v_max, h_max)

	visibility(_data)
	visibility([i[::-1] for i in _data[::-1]], len(_data) - 1, len(_data[0]) - 1)
	print(_res)
	return(max((max(x) for x in _res)))

_INPUT = """
30373
25512
65332
33549
35390
"""

_EXPECTED = 8

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