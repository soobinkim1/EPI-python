def findThreeLargestNumbers(array):
    # Write your code here.
	# first = - float('inf')
	# second = - float('inf')
	# third = - float('inf')
	result = []
	for n in array:
		if len(result) < 3:
			result.append(n)
		else:
			min_index = result.index(min(result))
			if n > result[min_index]:
				result[min_index] = n
	result.sort() # time complexity =
	return result
