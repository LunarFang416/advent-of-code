import ast

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
	a, b =_sum[depth[-1]] 
	_sum[depth[-1]] = 0
	l_adj , r_adj = [], []
	for idx, i in enumerate(depth[-1::-1]):
		if i == 0:
			r_adj = [*depth[:len(depth) - idx - 1], *[int(not j) for j in depth[len(depth) - idx - 1:]]] 
			break
	for idx, i in enumerate(depth[-1::-1]):
		if i == 1:
			l_adj = [*depth[:len(depth) - idx - 1], *[int(not j) for j in depth[len(depth) - idx - 1:]]] 
			break
	if l_adj:l_adj.extend([1]*10)
	if r_adj:r_adj.extend([0]*10)	
	_m = _n = __sum
	for j in r_adj:
		if isinstance(_m[j], int):
			_m[j] += b
			break
		_m = _m[j]
	for j in l_adj:
		if isinstance(_n[j], int):
			_n[j] += a
			break
		_n = _n[j]
	return __sum

def do_split(_sum, data):
	__sum = _sum
	for i in data[:-1]: _sum = _sum[i]
	_sum[data[-1]] = [int(_sum[data[-1]] / 2), _sum[data[-1]] - int(_sum[data[-1]] / 2)] 
	return __sum

def magnitude(_sum):
	if isinstance(_sum, int): return _sum
	return 3 * magnitude(_sum[0]) + 2 * magnitude(_sum[1])

def calc(s):
	data = []
	for i in s.split(): data.append(ast.literal_eval(i))
	
	_sum = data[0]
		
	for a in data[1:]:
		__sum  = [_sum, a]
		while explode(__sum) or split(__sum):
			while explode(__sum):
				__sum = do_explode(__sum, explode(__sum))
				continue				
			
			d = split(__sum)
			if d: __sum = do_split(__sum, d)
		_sum = __sum
	print(magnitude(_sum))
	print(_sum)		
		
def main():
	with open("day18input.txt") as f:
		calc(f.read())

if __name__ == "__main__":
	raise SystemExit(main())
