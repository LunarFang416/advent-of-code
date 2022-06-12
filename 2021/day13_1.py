import re

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
	
	
	val = folds[0][1]
	new_mapping = set()
	for x, y in mapping:
		if x > val:	
			new_x = val - (x - val)
			new_mapping.add((new_x, y)) 
			#mapping.remove((x, y))
		else:
			new_mapping.add((x, y))
	print(len(new_mapping))




if __name__ == "__main__":
	raise SystemExit(main())
