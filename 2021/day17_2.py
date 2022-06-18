import re

def calc(s):
	p = re.match(r".*x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", s.strip()).groups()
	min_x, max_x, min_y, max_y = tuple(map(int, p))
	c = 0
	for x in range(1, max_x + 1):
		for y in range(min_y, abs(min_y)):
			vx, vy = x, y
			_x, _y = 0, 0
			for _ in range(2 * abs(min_y) + 1):
				_x += vx
				_y += vy
				vx = max(vx - 1, 0)
				vy -= 1
				if min_y <= _y <= max_y and min_x <= _x <= max_x:
					c += 1
					break
				elif _y < min_y or _x > max_x: break

	return c

	

def main():
	with open("day17input.txt") as f:
		print(calc(f.read()))

if __name__ == "__main__":
	raise SystemExit(main())
