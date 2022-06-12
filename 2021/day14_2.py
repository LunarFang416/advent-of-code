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
	count_1 = Counter()
	for i in range(len(poly) - 1):
		count_1[poly[i: i+2]] += 1

	for _ in range(40):
		new_count = Counter()
		char_count = Counter()
		for i, j in count_1.items():	
			new_count[i[0]+mapping[i]] += j
			new_count[mapping[i]+i[1]] += j
			
			char_count[i[0]] += j
			char_count[mapping[i]] += j
		
		count_1 = new_count
	
	char_count[poly[-1]] += 1
	print(max(char_count.values()) - min(char_count.values()))		

if __name__ == "__main__":
	raise SystemExit(main())
