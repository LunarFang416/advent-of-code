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
	print(n)
	winner_found = False
	for i in n[0]:
		print(i)
		for j in range(1, len(n) - 5, 5):
			change_board(i, n[j: j+6])
			if check_win(n[j:j+6]):
				sum = 0
				board = n[j:j+6]
				for k in range(5):
					for m in range(5):	
						if board[k][m] != "-": sum += int(board[k][m])
				print(sum)
				print(i)
				print(int(i)*sum)
				winner_found = True
				break				
		if winner_found: break
