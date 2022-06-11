import sys

DIRECTIONS = [[-1,0], [1,0], [0,1], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]

def legal(x, y, r_dir, c_dir, row, col):
	return 0 <= x + r_dir < row and 0 <= y + c_dir < col

def flash_bomb(n, x, y, row, col):
	for r_d, c_d in DIRECTIONS:
		if legal(x, y, r_d, c_d, row, col) and n[x + r_d][y + c_d] != 0:
			n[x + r_d][y + c_d] = (n[x + r_d][y + c_d] + 1) % 10
	
if __name__ == "__main__":
	n = sys.stdin.read().strip().split('\n')
	n = [list(map(int, list(i))) for i in n]
	
	total_flash = 0
	for i in range(100):
		for j in range(len(n)):
			for k in range(len(n[0])):
				n[j][k] = (n[j][k] + 1) % 10		
		flashed = []
		num_flashed = 1
		while num_flashed != 0:
			num_flashed = 0
			for j in range(len(n)):
				for k in range(len(n[0])):
					if n[j][k] == 0 and (j, k) not in flashed:
						flash_bomb(n, j, k, 10, 10)
						flashed.append((j, k))
						num_flashed += 1
			total_flash += num_flashed	
	print(total_flash)	
