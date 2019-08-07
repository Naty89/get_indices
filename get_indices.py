def get_indices(list, x):
	y = []
	for i in range(len(list)-1):
		if x == list[i]:
			y.append(i)
		else:
			pass
	return y

print(get_indices(["a","a","b","a","b","a"], “a”))