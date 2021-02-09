def largest(x):
	luku = x[0]
	for y in x:
		if luku < y:
			luku = y
	return luku

print(largest([1,2,3,4,5]))
