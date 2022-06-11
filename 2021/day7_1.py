if __name__ == "__main__":
	n = list(map(int, input().strip().split(",")))
	max = max(n)
	max_f = pow(2, 31)
	for i in range(max):
		curr = 0
		for j in n: curr += abs(j - i)
		if curr < max_f: max_f = curr

	print(max_f) 	
