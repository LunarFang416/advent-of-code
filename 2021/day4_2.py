import sys

def check_win(arr):
	for i in arr:
		if i[0] == i[1] == i[2] == i[3] == i[4] == "-": 
			return True
	
	for i in range(5):
		if arr[0][i] == arr[1][i] == arr[2][i] == arr[3][i] == arr[4][i] == "-":
			return True	
	return False
	
def change_board(key, board):
	for i in range(5):
		for j in range(5):
			if board[i][j] == key: 
				board[i][j] = "-"
	

if __name__ == "__main__":
	n = sys.stdin.read()
	n = n.strip().split("\n")
	n[0] = n[0].split(",")
	n = [i for i in n if i != '']
	for i in range(1, len(n)): n[i] = n[i].split()
	boards = []
	for i in range(1, len(n) - 5, 5): boards.append(n[i:i+6])
	print(boards)
	scores = []
	winners = []
	for i in n[0]:
		for j in boards:
			if j not in winners:
				change_board(i, j)
				if check_win(j):
					sum = 0
					for k in range(5):
						for m in range(5):	
							if j[k][m] != "-": sum += int(j[k][m])
					print(f"i => {i} sum => {sum} {int(i)*sum}")
					scores.append(int(i)*sum)
					winners.append(j)
					#boards.remove(j)
				
	print(boards)
	#print(scores)

