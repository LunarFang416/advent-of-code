import pytest

def sum_packet(store): return sum(store)

def product_packet(store):
	s = 1
	for i in store: s *= i	
	return s

def minimum_packet(store): return min(store)

def maximum_packet(store): return max(store)

def literal_packet(binary, pointer):
	val = ""
	while binary[pointer] != "0":
		val += binary[pointer + 1: pointer + 5]
		pointer += 5
	val += binary[pointer + 1: pointer + 5]
	pointer += 5
	return (pointer, int(val, 2))		

def greater_packet(store): return int(store[0] > store[1])

def lesser_packet(store): return int(store[0] < store[1])

def equal_packet(store): return int(store[0] == store[1])

func_map = {
	0: sum_packet, 1: product_packet, 2: minimum_packet, 3: maximum_packet,
	4: literal_packet, 5: greater_packet, 6: lesser_packet, 7: equal_packet
}

def hex_to_bin(x):
	binary = ""
	for i in x:
		if i.isalpha(): i = 10 + ord(i) - ord('A')
		b = bin(int(i))[2:]
		binary += "0"*(4-len(b))  + b
	return binary

def operator_packet_mode_1(binary, pointer, value, _id):
	total_len = int(binary[pointer: pointer + 15], 2)
	pointer += 15
	_pointer = pointer
	value_store = []
	while pointer < _pointer + total_len:
		pointer, val = packet(binary, pointer, value)
		value_store.append(val)
	return (pointer, func_map[_id](value_store))

def operator_packet_mode_2(binary, pointer, value, _id):
	total_pack = int(binary[pointer: pointer + 11], 2)
	pointer += 11
	value_store = []
	for i in range(total_pack):
		pointer, val = packet(binary, pointer, value)
		value_store.append(val)
	return (pointer, func_map[_id](value_store))

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

@pytest.mark.parametrize(
	('_input', 'expected'),
	(("C200B40A82", 3),("04005AC33890",54), ("880086C3E88112",7), ("CE00C43D881120",9), 
	("D8005AC2A8F0",1), ("F600BC2D8F",0), ("9C005AC2F8F0", 0), ("9C0141080250320F1802104A08", 1),),
)
def test(_input, expected): assert packet(hex_to_bin(_input), 0, 0)[1] == expected

if __name__ == "__main__":
	raise SystemExit(main())
