#Determines the sum of the digits of 2^1000

def sum_of_digits(x):
	#for to convert number to string to use "list"
	list_1 = list(str(x))
	#have to convert each element in list to number for 'sum'
	list_1 = list(map(int, list_1))
	sum_digits = sum(list_1)
	return sum_digits

x = 2 ** 1000
y = sum_of_digits(x)
print('The sum of digits is: ', y)