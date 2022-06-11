import sys

def bin_to_deci(bin):
	value = 0
	bin = bin[::-1]
	for i in range(len(bin)):
		if bin[i] == "1": value += pow(2, i)
	return value

if __name__ == "__main__":
	n = sys.stdin.read()
	n = n.strip().split("\n")
	reading_len = len(n[0])
	o_candidates = n[:]
	co2_candidates = n[:]
	current_o_pos = 0
	current_co2_pos = 0
	while len(o_candidates) != 1 or len(co2_candidates) != 1:
		bit_one = 0
		bit_zero = 0
		if len(o_candidates) != 1:	
			for i in o_candidates:
				if i[current_o_pos] == "1": bit_one += 1
				else: bit_zero += 1
			if bit_one == bit_zero or bit_one > bit_zero:
				o_candidates = [i for i in o_candidates if i[current_o_pos] == "1"]
			else:	
				o_candidates = [i for i in o_candidates if i[current_o_pos] == "0"]
			current_o_pos = current_o_pos % reading_len + 1

		bit_one = 0
		bit_zero = 0
		
		if len(co2_candidates) != 1:	
			for i in co2_candidates:
				if i[current_co2_pos] == "1": bit_one += 1
				else: bit_zero += 1
			if bit_one == bit_zero or bit_one > bit_zero:
				co2_candidates = [i for i in co2_candidates if i[current_co2_pos] == "0"]
			else:
				co2_candidates = [i for i in co2_candidates if i[current_co2_pos] == "1"]
			current_co2_pos = current_co2_pos % reading_len + 1

	print(o_candidates[0])
	print(co2_candidates[0])
	print(bin_to_deci(o_candidates[0]) * bin_to_deci(co2_candidates[0]))
