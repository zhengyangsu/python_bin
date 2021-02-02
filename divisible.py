count = 1
result = 3
for x in range (0, 1000):
	result += 3
	if (result < 2000):
		count += 1
	if (result > 2000):
		break
	print result
print count