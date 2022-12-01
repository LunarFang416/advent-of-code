import pytest

def compute(s: str) -> int:
	req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
	req_fields.sort()
	count = 0
	for i in s.strip().split("\n\n"):
		i = i.strip().replace("\n", " ")
		fields = []
		for j in i.split(" "): 
			key, val = j.split(":")
			if key == "byr":
				if 1920 <= int(val) <= 2002: 
					fields.append(key)
					continue
				else: break
			if key == "iyr":
				if 2010 <= int(val) <= 2020: 
					continue
					fields.append(key)
				else: break
			if key == "eyr":
				if 2020 <= int(val) <= 2030: 
					continue
					fields.append(key)
				else: break
			if key == "hgt": 
				if val.endswith("cm"): 
					if int(val)
		fields.sort()
		if "cid" in fields: fields.remove("cid")
		if req_fields == fields: count += 1
	return count

@pytest.mark.parametrize(
	('_input', 'expected'),
	[()],
)
def test_computer(_input, expected): assert compute(_input) == expected

def main() -> int:
	with open("day4input.txt") as f:
		print(compute(f.read()))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
	
