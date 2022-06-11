import sys

NORTH = [-1,0]
SOUTH = [1,0]
EAST = [0,1]
WEST = [0,-1]
SOUTH_EAST = [1,1]
SOUTH_WEST = [1,-1]
NORTH_EAST = [-1,1]
NORTH_WEST = [-1,-1]

DIRECTIONS = [NORTH, SOUTH, EAST, WEST]

def is_safe(x, y, r_dir, c_dir, row, col):
	if x - r_dir < 0: return False
	if x + r_dir >= row: return False
	if y - c_dir < 0: return False
	if y + c_dir >= col: return False
	return True

def find_boundry_helper(area, x, y, row, col, basin_area):
	

	if int(area[x][y]) >= 9: return 
	elif (x, y) not in basin_area:
		basin_area.append((x, y))
		for r_dir, c_dir in DIRECTIONS:
			if is_safe(x, y, r_dir, c_dir, row, col):
				ans = find_boundry_helper(area, x + r_dir, y + c_dir, row, col, basin_area)
		return 
	return 

def find_boundry(area, x, y, row, col):
	basin_area = [(x,y)]
	for r_dir, c_dir in DIRECTIONS:
		if is_safe(x, y, r_dir, c_dir, row, col):
			ans = find_boundry_helper(area, x + r_dir, y + c_dir, row, col, basin_area)
	print("here")
	return len(basin_area)


if __name__ == "__main__":
	n = [list(i) for i in sys.stdin.read().strip().split("\n")]
	row = len(n)
	col = len(n[0])
	num = 0
	basins = []
	for i in range(row):
		for j in range(col):
			small = True
			x = int(n[i][j])
			if i - 1 >= 0:
				if x >= int(n[i - 1][j]): small = False
			if i + 1 < row:
				if x >= int(n[i + 1][j]): small = False
			if j + 1 < col:
				if x >= int(n[i][j + 1]): small = False	
			if j - 1 >= 0:
				if x >= int(n[i][j - 1]): small = False
			if small: 
				x = int(i)
				y = int(j)
				basins.append(find_boundry(n, x, y, row, col))				
	basins.sort()
	print(basins)										
