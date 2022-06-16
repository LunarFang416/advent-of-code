from math import sqrt
DIRECTIONS = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def heuristic(p1, p2):
	return abs(sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))

def main():
	grid = []
	with open("day15input.txt", "r") as f:
		for line in f.readlines():
			grid.append(list(map(int, line.strip())))

	open_nodes = []
	start_pos = (0, 0)
	end_pos = (len(grid) - 1, len(grid) - 1)
	open_nodes.append((start_pos, 0, 0, 0))
	closed = []
	values = {start_pos : (0, 0, 0)}
	while len(open_nodes) > 0:
		current = open_nodes[0]
		del open_nodes[0]
		try:
			values.pop(current[0])
		except:
			continue
		closed.append(current[0])
	
		if current[0] == end_pos:
			print(current)
			break
		print(current)
		for _x, _y in DIRECTIONS:
			n_x, n_y = current[0][0] + _x, current[0][1] + _y
			if n_x < 0 or n_x > len(grid) - 1 or n_y < 0 or n_y > len(grid) - 1 or (n_x, n_y) in closed:
				continue
			g = current[2] + grid[n_x][n_y]
			h = heuristic((n_x, n_y), end_pos)
			f = g + h
			
			if (n_x, n_y) in values.keys():
				if values[(n_x, n_y)][1] < g:
					continue			

			
			values[(n_x, n_y)] = (f, g, h)	
			open_nodes.append(((n_x, n_y), f, g, h))
		open_nodes.sort(key = lambda x:x[1])
			


if __name__ == "__main__":
	raise SystemExit(main())



