import re

def drag_x(x):
	if x == 0: return 0
	elif x > 0: return x - 1
	else: return x + 1

def gravity_y(y): return y - 1

def main():
	with open("day17input.txt") as f:
		p = re.match(r".*x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", f.read()).groups()
		min_x, max_x, min_y, max_y = tuple(map(int, p))
	print(min_x, max_x, min_y, max_y)

	

if __name__ == "__main__":
	raise SystemExit(main())
