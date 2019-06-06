#Finds the sum of all the multiples of 3 to 5 up to 1000

i = 0
max_num = 1000
sum_of_multiples = 0

while i < max_num:
	# if i%3 == 0 and i%5 == 0:
	# 	sum_of_multiples = sum_of_multiples + i
	# 	i += 1

	#don't need above code. If multiple of three will skip 5.  if not will go to five.

	if i%3 == 0:
		sum_of_multiples = sum_of_multiples + i
		i += 1

	elif i%5 == 0:
		sum_of_multiples = sum_of_multiples + i
		i += 1

	else:
		i += 1

print(sum_of_multiples)
