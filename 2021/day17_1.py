import re

def calc(s):
	p = re.match(r".*x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", s.strip()).groups()
	min_x, max_x, min_y, max_y = tuple(map(int, p))
	h = {}
	for i in range(min_y, max_y + 1):
		for steps in range(1, 100):
			v_y = (i - (0.5) * (-1) * (steps**2)) / steps
			m = (v_y**2) / 2
			h[m] = v_y

	return int(max(h.keys()))	

def main():
	with open("day17input.txt") as f:
		print(calc(f.read()))

if __name__ == "__main__":
	raise SystemExit(main())
