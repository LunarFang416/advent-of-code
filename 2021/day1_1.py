import sys

if __name__ == "__main__":
	n = sys.stdin.read()
	n = n.strip()
	n = n.split("\n")
	n = list(map(int, n))
	print(len(n))
	l = 0
	for i in range(1, len(n)):
		if n[i] > n[i - 1]: l += 1
	print(l)
