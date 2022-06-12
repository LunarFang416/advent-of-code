from collections import Counter, defaultdict
import re

def main():
	mapping = defaultdict(lambda: "")
	with open("day14input.txt", "r") as f:
		poly, rules = f.read().split("\n\n")
		rules = rules.strip().split("\n")
		for i in rules:
			org, tar = re.search("(\w+)\s*->\s*(\w)", i).groups()
			mapping[org] = tar
	print(mapping)	
	poly = poly.strip()
	for i in range(10):
		new_poly = ''	
		c1, c2 = 0, 1
		while c2 < len(poly):
			new_poly += poly[c1] + mapping[poly[c1] + poly[c2]]
			c1 += 1
			c2 += 1
		new_poly += poly[-1]
		poly = new_poly
	
	res = Counter(poly)
	print(res)
	print(max(res.values()) - min(res.values()))	

if __name__ == "__main__":
	raise SystemExit(main())
