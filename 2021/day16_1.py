import pytest

def hex_to_bin(x):
	binary = ""
	for i in x:
		if i.isalpha(): i = 10 + ord(i) - ord('A')
		b = bin(int(i))[2:]
		binary += "0"*(4-len(b)) + b
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
		pointer, total_ver = packet(binary, pointer, total_ver)
	return (pointer, total_ver)

def operator_packet_mode_2(binary, pointer, total_ver):
	total_pack = int(binary[pointer: pointer + 11], 2)
	pointer += 11
	for i in range(total_pack):
		pointer, total_ver = packet(binary, pointer, total_ver)
	return (pointer, total_ver)

def packet(binary, pointer, total_ver):
	total_ver += int(binary[pointer: pointer + 3], 2)
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
	print(packet(hex_to_bin(raw_data), 0, 0))

@pytest.mark.parametrize(
	('_input', 'expected'),
	(("8A004A801A8002F478",16),("620080001611562C8802118E34",12),("C0015000016115A2E0802F182340", 23), ("A0016C880162017C3686B18A3D4780", 31), ),
)
def test(_input, expected): assert packet(hex_to_bin(_input), 0, 0)[1] == expected


if __name__ == "__main__":
	raise SystemExit(main())
