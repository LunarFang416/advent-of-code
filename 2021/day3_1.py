import sys

def bin_to_deci(bin):
	value, bin = 0, bin[::-1]
	for i in range(len(bin)): if str(bin[i]) == "1": value += pow(2, i)
	return value

if __name__ == "__main__":
	n = sys.stdin.read()
	n = n.strip().split("\n")
	reading_length, gamma, epsilon = len(n[0]), "", ""
	for i in range(reading_length):
		bit_one, bit_zero = 0, 0
		for j in n:
			if j[i] == "1": bit_one += 1
			else: bit_zero += 1
		if bit_one > bit_zero: 
			gamma += "1"
			epsilon += "0"
		else:
			gamma += "0"
			epsilon += "1"
	print(gamma, epsilon, bin_to_deci(gamma)*bin_to_deci(epsilon))
