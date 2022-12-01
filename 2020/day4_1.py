import pytest

def compute(s: str) -> int:
	req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
	req_fields.sort()
	count = 0
	for i in s.strip().split("\n\n"):
		i = i.strip().replace("\n", " ")
		fields = []
		for j in i.split(" "): fields.append(j.split(":")[0])
		fields.sort()
		if "cid" in fields: fields.remove("cid")
		if req_fields == fields: count += 1
	return count

_INPUT = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""	
_EXPECTED = 2

@pytest.mark.parametrize(
	('_input', 'expected'),
	[(_INPUT,_EXPECTED)],
)
def test_computer(_input, expected): assert compute(_input) == expected

def main() -> int:
	with open("day4input.txt") as f:
		print(compute(f.read()))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
	
