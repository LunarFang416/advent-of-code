import re

def compute(s):
	data = []
	for i in s.split("\n"):
		p = re.match(r"^(on|off).*x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", i).groups()
		data.append([p[0], (int(p[1]), int(p[2])), (int(p[3]), int(p[4])), (int(p[5]), int(p[6]))])

	init = set()
	
	def overlap(p1, p2):
		x, y, z, _x, _y, _z = p1, p2
		new = ()
		if (max(x[0], _x[0]), min(x[1], _x[1]))
		

	for status, (min_x, max_x), (min_y, max_y), (min_z, max_z) in data:
		if status == "on":

		else: 
						
	return len(init)
						
def main():
	with open("day22input.txt") as f:
		print(compute(f.read().strip()))


if __name__ == "__main__":
	raise SystemExit(main())
