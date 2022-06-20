import re

def compute(s):
	data = []
	for i in s.split("\n"):
		p = re.match(r"^(on|off).*x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", i).groups()
		data.append([p[0], (int(p[1]), int(p[2])), (int(p[3]), int(p[4])), (int(p[5]), int(p[6]))])

	init = set()
	for status, (min_x, max_x), (min_y, max_y), (min_z, max_z) in data:
		if ((min_x not in range(-50, 50) and max_x not in range(-50, 50)) or 
			(min_y not in range(-50, 50) and max_y not in range(-50, 50)) or 
			(min_z not in range(-50, 50) and max_z not in range(-50, 50))):
			continue
		if min_x < -50: min_x = -50
		if max_x > 50: max_x = 50
		if min_y < -50: min_y = -50
		if max_y > 50: max_y = 50
		if min_z < -50: min_z = -50
		if max_z > 50: max_z = 50
		if status == "on":
			for x in range(min_x, max_x + 1):
				for y in range(min_y, max_y + 1):
					for z in range(min_z, max_z + 1):
						init.add((x, y, z))
		else: 
			for x in range(min_x, max_x + 1):
				for y in range(min_y, max_y + 1):
					for z in range(min_z, max_z + 1):
						if (x, y, z) in init:
							init.remove((x, y, z))
						
	return len(init)
						
def main():
	with open("day22input.txt") as f:
		print(compute(f.read().strip()))


if __name__ == "__main__":
	raise SystemExit(main())
