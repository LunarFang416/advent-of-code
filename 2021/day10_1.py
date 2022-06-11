import sys
from collections import *


if __name__ == "__main__":
	n = sys.stdin.read().strip().split("\n")
	num = 0
	openers = ['{', '(', '<', '[']
	closers = ['}', ')', '>', ']']
	scores = {'}':1197, ')':3, '>':25137, ']':57}
	for i in n:
		opening_list = []
		closing_list = []
		for j in i:
			if j in openers:
				opening_list.append(j)
			else:
				c_idx = closers.index(j)
				if opening_list[-1] != openers[c_idx]:
					num += scores[j]
					break
				else:
					opening_list.pop()

	print(num)
