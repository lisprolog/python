def index_power(array, n):

	if n == 0:
		return 1;
	if n >= len(array):
		return -1;

	j = array[n];
	for i in range(n-1):
		j *= array[n];

	if j == 0:
		return 1;
	else:
		return j;
