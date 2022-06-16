def sum_packet(store):
	return sum(store)

def product_packet(store):
	s = 1
	for i in store: s *= i	
	return s

def minimum_packet(store):
	return min(store)

def maximum_packet(store):
	return max(store)

def literal_packet(binary, pointer):
	val = ""
	while binary[pointer] != "0":
		val += binary[pointer + 1: pointer + 5]
		pointer += 5
	val += binary[pointer + 1: pointer + 5]
	pointer += 5
	return (pointer, int(val, 2))		

def greater_packet(store):
	return int(store[0] > store[1])

def lesser_packet(store):
	return int(store[0] < store[1])

def equal_packet(store):
	return int(store[0] == store[1])

func_map = {
	0: sum_packet, 
	1: product_packet,
	2: minimum_packet, 
	3: maximum_packet,
	4: literal_packet,
	5: greater_packet,
	6: lesser_packet,
	7: equal_packet
}

def hex_to_bin(x):
	binary = ""
	for i in x:
		if i.isalpha():
			i = 10 + ord(i) - ord('A')
		i = int(i)
		b = bin(i)[2:]
		binary += "0"*(4-len(b))  + b
	return binary

def operator_packet_mode_1(binary, pointer, value, _id):
	total_len = int(binary[pointer: pointer + 15], 2)
	pointer += 15
	_pointer = pointer
	value_store = []
	while pointer < _pointer + total_len:
		data = packet(binary, pointer, value)
		pointer = data[0]
		value_store.append(data[1])
	final_value = func_map[_id](value_store)
	return (pointer, final_value)

def operator_packet_mode_2(binary, pointer, value, _id):
	total_pack = int(binary[pointer: pointer + 11], 2)
	pointer += 11
	value_store = []
	for i in range(total_pack):
		data = packet(binary, pointer, value)
		pointer = data[0]
		value_store.append(data[1])
	final_value = func_map[_id](value_store)
	return (pointer, final_value)

def packet(binary, pointer, value):
	pointer += 3
	id = int(binary[pointer: pointer + 3], 2)
	pointer += 3
	if id == 4:
		return literal_packet(binary, pointer)
	if binary[pointer] == "0":
		return operator_packet_mode_1(binary, pointer + 1, value, id)
	return operator_packet_mode_2(binary, pointer + 1, value, id)


def main():
	raw_data = ""
	with open("day16input.txt") as f:
		raw_data = f.read().strip()
	binary = hex_to_bin(raw_data)	
	print(packet(binary, 0, 0))

if __name__ == "__main__":
	raise SystemExit(main())
