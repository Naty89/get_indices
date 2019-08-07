def get_indices(list, x):
	y = [i for i in range(len(list)) if x == list[i]]
	return y

print(get_indices(["a","a","b","a","b","a","m"], "a"))