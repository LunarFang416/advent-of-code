import sys

if __name__ == "__main__":
	n = sys.stdin.read()
	n = n.strip().split("\n")
	n = [i.split(" | ")[1].split() for i in n]
	num = 0
	for i in n:
		for j in i:
			if len(j) == 2 or len(j) == 4 or len(j) == 3 or len(j) == 7: num += 1
	print(num)		
