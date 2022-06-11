import sys

if __name__ == "__main__":
	n = sys.stdin.read()
	n = n.strip().split("\n")
	depth = 0
	h = 0
	for i in n:
		dir, value = i.split()
		if dir == "forward": h += int(value)
		elif dir == "up": depth -= int(value)
		else: depth += int(value)

	print(h*depth)
