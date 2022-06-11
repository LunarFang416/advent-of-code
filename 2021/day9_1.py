import sys



if __name__ == "__main__":
	n = [list(i) for i in sys.stdin.read().strip().split("\n")]
	row = len(n)
	col = len(n[0])
	num = 0
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
			if small: num += 1 + x

	print(num)
