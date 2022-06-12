import os
import re
from collections import defaultdict

def main():
	map = defaultdict(list)
	with open("day12input.txt", "r") as f:
		for line in f.readlines():
			fro, to = re.search(r"(\w+)-(\w+)", line).groups()
			map[fro].append(to)
			map[to].append(fro)
	routes = set()	
	
	todo = [('start', )]
	
	while todo:
		path = todo.pop()
		if path[-1] == "end":
			routes.add(path)
			print("tttttt")
			continue
		print("here")
		print(path)
		for choice in map[path[-1]]:
			if choice.isupper() or choice not in path:
				todo.append((*path, choice))
	print(routes)	
	print(len(routes))
	
		
if __name__ == "__main__":
	raise SystemExit(main())
