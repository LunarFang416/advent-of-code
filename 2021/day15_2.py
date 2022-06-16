from math import sqrt
import heapq
DIRECTIONS = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def heuristic(p1, p2):
	return abs(sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))

def val(n):
	while n > 9:
		n -= 9		
	return n	

def main():
	new_grid = {}
	with open("day15input.txt", "r") as f:
		lines = f.readlines()
		height = len(lines)
		for i in range(len(lines)):
			for j in range(len(lines)):
				for m in range(5):
					for n in range(5):
						new_grid[(i + m*height, j + n*height)] = val(int(lines[i][j]) + m + n)
	


	start = (0, 0)
	end = max(new_grid.keys())

	seen = set()
	todo = [(0, 0, 0, (0, 0))]
	
	while todo:
		f, g, h, coord = heapq.heappop(todo)
		
		if coord == end:
			print(f, g, h, coord)
			break
		elif coord in seen:
			continue
		else:
			seen.add(coord)
		
		for x, y in DIRECTIONS:	
			n_x, n_y = coord[0] + x, coord[1] + y
			if (n_x, n_y) in new_grid.keys() and (n_x, n_y) not in seen:
				n_g = g + new_grid[(n_x, n_y)] 
				n_h = heuristic(end, (n_x, n_y))
				n_f = n_h + n_g	
				heapq.heappush(todo, (n_f, n_g, n_h, (n_x, n_y)))

if __name__ == "__main__":
	raise SystemExit(main())



