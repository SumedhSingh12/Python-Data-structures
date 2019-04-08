def cont_sum(arr):
	current_sum = arr[0]
	result_sum = arr[0]
	for i in range(1, len(arr)):
		current_sum = max(current_sum + arr[i], arr[i])
		result_sum = max(current_sum, result_sum)
	return result_sum
cont_sum([-3,-2,-1])