import re





def compute(s):
	d = {}
	for idx, i in enumerate(s.split("\n\n")):
		data = []	
		for j in i.split("\n")[1:]:
			data.append(list(map(int, re.match(r"(-?\d+),(-?\d+),(-?\d+)", j).groups())))
		d[idx] = data

	return d

def main():
	with open("day19input.txt") as f:
		print(compute(f.read().strip()))


if __name__ == "__main__":
	raise SystemExit(main())
