def hex_to_bin(x):
	binary = ""
	for i in x:
		if i.isalpha():
			i = 10 + ord(i) - ord('A')
		i = int(i)
		b = bin(i)[2:]
		binary += "0"*(4-len(b))  + b
	return binary

def literal_packet(binary, pointer, total_ver):
	while binary[pointer] != "0":
		pointer += 5
	pointer += 5
	return (pointer, total_ver)

def operator_packet_mode_1(binary, pointer, total_ver):
	total_len = int(binary[pointer: pointer + 15], 2)
	pointer += 15
	_pointer = pointer
	while pointer < _pointer + total_len:
		data = packet(binary, pointer, total_ver)
		pointer = data[0]
		total_ver = data[1]
	return (pointer, total_ver)

def operator_packet_mode_2(binary, pointer, total_ver):
	total_pack = int(binary[pointer: pointer + 11], 2)
	pointer += 11
	for i in range(total_pack):
		data = packet(binary, pointer, total_ver)
		pointer = data[0]
		total_ver = data[1]
	return (pointer, total_ver)

def packet(binary, pointer, total_ver):
	ver = int(binary[pointer: pointer + 3], 2)
	total_ver += ver
	pointer += 3
	id = int(binary[pointer: pointer + 3], 2)
	pointer += 3
	if id == 4:
		return literal_packet(binary, pointer, total_ver)
	if binary[pointer] == "0":
		return operator_packet_mode_1(binary, pointer + 1, total_ver)
	return operator_packet_mode_2(binary, pointer + 1, total_ver)

def main():
	raw_data = ""
	with open("day16input.txt") as f:
		raw_data = f.read().strip()
	binary = hex_to_bin(raw_data)	
	print(packet(binary, 0, 0))

if __name__ == "__main__":
	raise SystemExit(main())
