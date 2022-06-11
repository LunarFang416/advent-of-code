if __name__ == "__main__":
	n = list(map(int, input().strip().split(",")))
	print(n)
	num = 0
	for i in range(80):
		new_fish = []
		print(len(n))
		for i in range(len(n)):
			if n[i] == 0:
				new_fish.append(8)
				n[i] = 6
			else:
				n[i] -= 1
		n.extend(new_fish)
	
	print(len(n))		
