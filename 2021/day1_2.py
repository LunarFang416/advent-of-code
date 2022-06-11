import sys

if __name__ == "__main__":
	n = sys.stdin.read()
	n = n.strip()
	n = n.split("\n")
	n = list(map(int, n))
	print(len(n))
	l = 0
	m = []
	for i in range(0, len(n) - 2):
		m.append(n[i] + n[i+1] + n[i+2])
	for j in range(1, len(m)):
		if(m[j] > m[j - 1]): l += 1
	
	print(l)
