from collections import Counter

if __name__ == "__main__":
	n = list(map(int, input().strip().split(",")))
	print(n)
	num = 0	
	C = Counter(n)
	print(C)
	for _ in range(256):
		NC = Counter()
		for k, v in C.items():
			if k == 0:
				NC[6] += v
				NC[8] += v
			else:
				NC[k-1] += v
			C = NC


	print(sum(C.values()))		
			
