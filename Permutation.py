import itertools
l = itertools.permutations(['a', 'a', 'a', 'q', 'r'])
size = 0
for a in l:
	print a
	size = size + 1
size = size/6
print size