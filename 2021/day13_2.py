import re
from collections import defaultdict

def main():
	mapping = set()
	folds = []
	max_x, max_y = 0, 0
	with open("day13input.txt", "r") as f:
		fold = False
		for line in f.readlines():
			if not line.strip():
				fold = True
				continue
			if not fold:
				x, y = list(map(int, line.strip().split(",")))
				if x > max_x: max_x = x
				if y > max_y: max_y = y
				mapping.add((x, y))
			else:
				dir, val = re.search("(\w)=(\d+)", line).groups()
				folds.append([dir, int(val)])
	
	new_mapping = set()
	for dir, val in folds:
		for x, y in mapping:
			if dir == "x":
				if x > val:	
					new_x = val - (x - val)
					new_mapping.add((new_x, y)) 
				else:
					new_mapping.add((x, y))
			else:
				if y > val:
					new_y = val - (y - val)
					new_mapping.add((x, new_y))	
				else:
					new_mapping.add((x, y))
		mapping = new_mapping
		new_mapping = set()		

	data = defaultdict(lambda: " ")
		
	for x, y in mapping:	
		data[(x, y)] = "#"
	for y in range(6):
		for x in range(40):
			print(data[(x, y)], end="")
		print("")	
	
	



if __name__ == "__main__":
	raise SystemExit(main())
