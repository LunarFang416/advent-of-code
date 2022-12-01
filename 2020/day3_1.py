import pytest

def compute(s: str) -> int:
	grid = []
	for line in s.strip().split("\n"):
		_row = []
		for l in line: _row.append(l)
		grid.append(_row)

	x, y, count, w = 0, 0, 0, len(grid[0])
	while y < len(grid):	
		if grid[y][x] == "#": count += 1
		y += 1
		x = (x + 3) % w
	return count

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
_EXPECTED = 7

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
	
