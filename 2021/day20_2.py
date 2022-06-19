from collections import defaultdict

DIRECTIONS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]

def delta(s): return int(s == "#")

def compute(s):
	algo, raw_image = s.split("\n\n")
	image = []
	d = defaultdict(lambda: ".")
	for idx, i in enumerate(raw_image.split("\n")):
		image.append(i)
		for _idx, j in enumerate(i): d[(idx, _idx)] = j
	length = len(image)
	for i in range(1, 51):
		n_d = defaultdict(lambda: (algo[-1], algo[0])[(i-1) % 2])
		for k in range(0 - i, length + i):
			for l in range(0 - i, length + i):
				num = ""
				for x, y in DIRECTIONS: num += str(delta(d[(k + x, l + y)]))
				n_d[(k, l)] = algo[int(num, 2)]
		d = n_d
	c = 0
	for idx, m in d.items(): if delta(m): c += 1
	return c

def main():
	with open("day20input.txt") as f:
		print(compute(f.read().strip()))

if __name__ == "__main__":
	raise SystemExit(main())
