import ast
from copy import deepcopy

def split(l, depth=[]):
	if isinstance(l, int): 
		if l >= 10: return depth	
		else: return None
	if len(l) == 2: return split(l[0], [*depth, 0]) or split(l[1], [*depth, 1])

def explode(l, depth=[]):
	if isinstance(l, int): return None
	if depth and len(depth) >= 4 and isinstance(l[0], int) and isinstance(l[1], int):
		return depth
	return explode(l[0], [*depth, 0]) or explode(l[1], [*depth, 1])

def do_explode(_sum, depth):
	__sum = _sum
	for i in depth[:-1]:_sum = _sum[i]
	a, b = _sum[depth[-1]] 
	_sum[depth[-1]] = 0
	def comp_range(locate):
		for idx, i in enumerate(depth[-1::-1]):
			if i == locate:
				return [*depth[:len(depth) - idx - 1], *[int(not j) for j in depth[len(depth) - idx - 1:]], *[locate]*10]
		return []	

	l_adj = comp_range(1)
	r_adj = comp_range(0)
	
	def update(coord, x):
		_n = __sum
		for i in coord:
			if isinstance(_n[i], int):
				_n[i] += x
				return _n
			_n = _n[i]	
	update(r_adj, b)
	update(l_adj, a)
	return __sum

def do_split(_sum, data):
	__sum = _sum
	for i in data[:-1]: _sum = _sum[i]
	_sum[data[-1]] = [int(_sum[data[-1]] / 2), _sum[data[-1]] - int(_sum[data[-1]] / 2)] 
	return __sum

def magnitude(_sum):
	if isinstance(_sum, int): return _sum
	return 3 * magnitude(_sum[0]) + 2 * magnitude(_sum[1])

def reduce(__sum):
	while explode(__sum) or split(__sum):
		while explode(__sum):
			__sum = do_explode(__sum, explode(__sum))
			continue

		d = split(__sum)
		if d: __sum = do_split(__sum, d)
	return __sum

def calc(s):
	data = []
	for i in s.split(): data.append(ast.literal_eval(i))
	maximum = 0
	for idx, a in enumerate(data):
		for b in data[idx+1:]:
			maximum = max(maximum, magnitude(reduce([deepcopy(b), deepcopy(a)])))
			maximum = max(maximum, magnitude(reduce([deepcopy(a), deepcopy(b)])))

	print(maximum)
		
def main(): 
	with open("day18input.txt") as f: calc(f.read())

if __name__ == "__main__":
	raise SystemExit(main())
