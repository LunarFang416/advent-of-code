import sys

if __name__ == "__main__":
	n = sys.stdin.read().strip().split("\n")
	num = 0
	openers = ['{', '(', '<', '[']
	closers = ['}', ')', '>', ']']
	scores = {'}':3, ')':1, '>':4, ']':2}
	corr = {'{':'}', '(':')','[':']', '<':'>'}
	m = n[:]
	for i in n:
		opening_list = []
		for j in i:
			if j in openers:
				opening_list.append(j)
			else:
				c_idx = closers.index(j)
				if opening_list[-1] != openers[c_idx]:
					m.remove(i)
					break
				else: opening_list.pop()			
	print(m)
	l = []					
	for i in m:
		s = []
		t = 0
		for j in i:
			if j in openers: s.append(j)
			else: s.pop()
		s = s[::-1]
		for m in s:
			t *= 5
			t += scores[corr[m]]
		l.append(t)
	l.sort()
	print(len(l))	
	print(l[int(len(l)/2)])
