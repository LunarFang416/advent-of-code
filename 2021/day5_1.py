import sys



if __name__ == "__main__":
	n = sys.stdin.read()
	n = n.strip().split("\n")
	
	vectors = [list(i.replace(" -> ", ",").split(",")) for i in n]
	print(vectors)
	board = [[0]*1000 for i in range(1000)]
	
	for i in vectors:
		if int(i[0]) == int(i[2]):
			x = int(i[0])
			print(f"x same =>>> {i}")
			min_y = min(int(i[1]), int(i[3]))
			max_y = max(int(i[1]), int(i[3])) + 1
			for j in range(min_y, max_y):
				board[j][x] += 1

		if int(i[1]) == int(i[3]):
			y = int(i[1])
			min_x = min(int(i[0]), int(i[2]))
			max_x = max(int(i[0]), int(i[2])) + 1
			print(f"y same =>>> {i}")
			for j in range(min_x, max_x):
				board[y][j] += 1
	
	num = 0
	for i in range(1000):
		for j in range(1000):
			if board[i][j] >= 2: num += 1
	
	print(num)	
