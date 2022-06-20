import re

def compute(s):
	a, b = s.split("\n")
	a, b = re.match(r".*(\d)$", a).groups(), re.match(r".*(\d)$", b).groups()
	a, b = int(a[0]), int(b[0])

	rolls = s_a = s_b = 0
	_roll = 1
	def next_3(n): 
		n0, n1, n2 = n, n + 1, n + 2
		if n1 > 100: n1 -= 100
		if n2 > 100: n2 -= 100
		return n0 + n1 + n2
		
	while s_a < 1000 and s_b < 1000:
		a = add = (a + next_3(_roll) % 10) % 10
		if add == 0: a = add = 10
		s_a += add
		rolls += 3
		if s_a >= 1000: break
		_roll = (_roll + 3) % 100
		if _roll == 0: _roll = 100
		
		b = add = (b + next_3(_roll) % 10) % 10
		if add == 0: b = add = 10
		s_b += add
		rolls += 3
		if s_b >= 1000: break
		_roll = (_roll + 3) % 100
		if _roll == 0: _roll = 100

	if s_a < 1000: return rolls * s_a
	return rolls * s_b

def main():
	with open("day21input.txt") as f:
		print(compute(f.read().strip()))

if __name__ == "__main__":
	raise SystemExit(main())
