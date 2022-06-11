import sys

NORTH = [-1,0]
SOUTH = [1,0]
EAST = [0,1]
WEST = [0,-1]
SOUTH_EAST = [1,1]
SOUTH_WEST = [1,-1]
NORTH_EAST = [-1,1]
NORTH_WEST = [-1,-1]

DIRECTIONS = [NORTH, SOUTH, EAST, WEST, SOUTH_EAST, SOUTH_WEST, NORTH_EAST, NORTH_WEST]


def check_dir(coord):
	x1, y1, x2, y2 = list(map(int, coord))
	if x1 == x2:
		if y1 > y2: return WEST
		else: return EAST
	if y1 == y2:
		if x1 > x2: return NORTH
		else: return SOUTH
	if x1 < x2: 
		if y2 < y1: return SOUTH_WEST
		else: return SOUTH_EAST
	if x1 > x2:
		if y2 > y1: return NORTH_EAST
		else: return NORTH_WEST

def change_board(board, coord):
	r_dir, c_dir = check_dir(coord)
	x1, y1, x2, y2 = list(map(int, coord))
	c_x, c_y = int(x1), int(y1)
	print(f"x1 = {x1} y1 = {y1} x2 = {x2} y2 = {y2}  r_dir = {r_dir} c_dir = {c_dir} ")
	while c_x != x2 or c_y != y2:
		#print(f"{c_x} {c_y}")
		board[c_x][c_y] += 1
		c_x += r_dir
		c_y += c_dir
	board[x2][y2] += 1

if __name__ == "__main__":
	n = sys.stdin.read()
	n = n.strip().split("\n")
	
	vectors = [list(i.replace(" -> ", ",").split(",")) for i in n]
	print(vectors)
	board = [[0]*1000 for i in range(1000)]
	
	for i in vectors:
		change_board(board, i)		
	
	num = 0
	for i in range(1000):
		for j in range(1000):
			if board[i][j] >= 2: num += 1
	
	print(num)	
