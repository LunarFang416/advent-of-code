import sys

if __name__ == "__main__":
	n = sys.stdin.read()
	n = n.strip().split("\n")
	n = [[i.split(" | ")[0].split(), i.split(" | ")[1].split()] for i in n]
	num = 0
	print(n)
	for i in n:
		k = 0
		pattern = ["" for j in range(7)]
		w = sorted(i[0], key = len)
		print(w)
		pattern[0] = w[0][0]
		pattern[4] = w[0][1]
		pattern[1] = w[1].replace(pattern[0], "").replace(pattern[4], "")
		four = w[2].replace(pattern[0], "").replace(pattern[4], "")
		eight = w[9]
		print(four)
		print(eight)
		common = list(set(four).intersection(eight))
		print(common)
		pattern[2] = four[0]
		pattern[3] = four[1]
		found = pattern[:5]
		print(found)
		uncommon = list(set(found) ^ set(list("abcdefg")))
		print(uncommon)
		pattern[5] = uncommon[0]
		pattern[6] = uncommon[1]
		two = ''.join(sorted(pattern[0] + pattern[1] + pattern[3] + pattern[6] + pattern[5]))
		three = ''.join(sorted(pattern[0] + pattern[1] + pattern[3] + pattern[4] + pattern[5]))
		five = ''.join(sorted(pattern[1] + pattern[3] + pattern[2] + pattern[4] + pattern[5]))
		six = ''.join(sorted(''.join(pattern[1:])))
		nine = ''.join(sorted(''.join(pattern[:6])))
		print(pattern)
		print(two, three, five, six, nine)
		for j in range(4):
			s = ''.join(sorted(i[1][j]))
			if len(i[1][j]) == 4: k += 4 * pow(10, 3 - j)
			elif len(i[1][j]) == 7: k += 8 * pow(10, 3 - j)
			elif len(i[1][j]) == 2: k += 1 * pow(10, 3 - j)
			elif len(i[1][j]) == 3: k += 7 * pow(10, 3 - j)
			elif s == two: k += 2 * pow(10, 3 - j)
			elif s == three: k += 3 * pow(10, 3 - j)
			elif s == five: k += 5 * pow(10, 3 - j)
			elif s == six: k += 6 * pow(10, 3 - j)
			elif s == nine: k += 9 * pow(10, 3 - j)
			else: 
				print(i)
				print(s)
				print("===============================")

				raise AssertionError 
		print(f"====> {k}")	
		num += k		 		
	print(num)		
