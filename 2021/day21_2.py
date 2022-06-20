import re
import functools

def compute(s):
	_a, _b = s.split("\n")
	_a, _b = re.match(r".*(\d)$", _a).groups(), re.match(r".*(\d)$", _b).groups()
	_a, _b = int(_a[0]), int(_b[0])

	cache = {}
	
	def possibilities(): return [x + y + z for x in [1, 2, 3] for y in [1, 2, 3] for z in [1, 2, 3]]
	
	def compute_wins(a, b, s_a, s_b):
		k = (a, b, s_a, s_b)
		if k in cache:
			return cache[k]
		count = [0, 0]
		
		for p in possibilities():
			next = (a + p - 1) % 10 + 1
			_s_a = s_a + next
			if _s_a >= 21:
				count[0] += 1
			else:
				_y, _x = compute_wins(b, next, s_b, _s_a)
				count[0] += _x
				count[1] += _y
		cache[k] = count
		return count
	return compute_wins(_a, _b, 0, 0)
	
def main():
	with open("day21input.txt") as f:
		print(compute(f.read().strip()))

if __name__ == "__main__":
	raise SystemExit(main())
