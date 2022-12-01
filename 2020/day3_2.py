import pytest

def compute(s: str) -> int:
	grid = []
	for line in s.strip().split("\n"):
		_row = []
		for l in line: _row.append(l)
		grid.append(_row)
	total, w = 1, len(grid[0])
	for d_x, d_y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
		x, y, count = 0, 0, 0
		while y < len(grid):	
			if grid[y][x] == "#": count += 1
			y += d_y
			x = (x + d_x) % w
		total *= count
	return total

_INPUT = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""
_EXPECTED = 336

@pytest.mark.parametrize(
	('_input', 'expected'),
	[(_INPUT, _EXPECTED)],
)
def test_computer(_input, expected): assert compute(_input) == expected

def main() -> int:
	with open("day3input.txt") as f:
		print(compute(f.read()))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
	
