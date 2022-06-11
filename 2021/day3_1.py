import sys


def bin_to_deci(bin):
	value = 0
	bin = bin[::-1]
	for i in range(len(bin)):
		if str(bin[i]) == "1": value += pow(2, i)
	return value



if __name__ == "__main__":
	n = sys.stdin.read()
	n = n.strip().split("\n")
	reading_length = len(n[0])
	gamma = ""
	epsilon = ""
	for i in range(reading_length):
		bit_one = 0
		bit_zero = 0
		for j in n:
			if j[i] == "1": bit_one += 1
			else: bit_zero += 1
		if bit_one > bit_zero: 
			gamma += "1"
			epsilon += "0"
		else:
			gamma += "0"
			epsilon += "1"
	print(gamma)
	print(epsilon)
	print(bin_to_deci(gamma)*bin_to_deci(epsilon))	

