import sys

if __name__ == "__main__":
	n = sys.stdin.read()
	n = n.strip().split("\n")
	depth, h, aim = 0, 0, 0
	for i in n:
		dir, value = i.split()
		if dir == "forward": 
			h += int(value)
			depth += aim * int(value)
		elif dir == "up": aim -= int(value)
		else: aim += int(value)

	print(h*depth)
