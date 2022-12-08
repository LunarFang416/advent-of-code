import pytest
import os
from collections import defaultdict

INPUT_TXT = f"{os.path.join(os.path.dirname(__file__))}/input.txt"

def compute(s: str) -> int:
	s = s.strip().splitlines()
	i, path, data = 0, [], defaultdict(int)
	while i < len(s):
		if s[i].startswith("$ cd"):
			if s[i].endswith(".."): path.pop()
			else: path.append(s[i].split()[-1])
		else:
			i += 1
			while i < len(s) and not s[i].startswith("$"):
				a, _ = s[i].split()
				if a.isnumeric(): data['/'.join(path)] += int(a)
				i += 1
			i -= 1
			for j in range(len(path)): data['/'.join(path[:j])] += data['/'.join(path)]
		i += 1
	_min = float("inf")
	cur = 70000000 - data['/']
	for i in data:
		if data[i] + cur >= 30000000:
			_min = min(data[i], _min)

	return _min

_INPUT = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

_EXPECTED = 24933642

@pytest.mark.parametrize(
	('_input', 'expected'),
	[(_INPUT, _EXPECTED)],
)
def test_computer(_input, expected): assert compute(_input) == expected

def main() -> int:
	with open(INPUT_TXT) as f: print(compute(f.read()))
	return 0

if __name__ == "__main__":
	raise SystemExit(main())
	
