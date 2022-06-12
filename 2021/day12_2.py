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
	
	todo = [(('start', ), False)]
	
	while todo:
		path, status = todo.pop()
		if path[-1] == "end":
			routes.add(path)
			print(path)	
			#print("tttttt")
			continue
		for choice in map[path[-1]]:
			if choice == 'start':
				continue
			if choice.isupper():
				todo.append(((*path, choice), status))
			elif status == False and path.count(choice) == 1:
				todo.append(((*path, choice), True))
			elif choice not in path:
				todo.append(((*path, choice), status))
	
	
	print(len(routes))	
	
		
if __name__ == "__main__":
	raise SystemExit(main())
