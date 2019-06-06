#Calculates the difference between the sum of squares of the first one hundred numbers and teh square of the sum


def sum_of_squares(x):
	
	sum_of_squares = 0
	for i in range(1,x+1):
		sum_of_squares = sum_of_squares + i ** 2
	print('Sum of squares = ', + sum_of_squares)
	return sum_of_squares

def square_of_sum(x):
	square_of_sum = 0
	total = 0
	for i in range(1, x+1):
		total = total + i
	square_of_sum = total ** 2
	print('Square of sums = ', square_of_sum)
	return square_of_sum




#square_of_sum(10)
x = sum_of_squares(100)
y = square_of_sum(100)
z = y - x 
print('The difference between the sum of squares and the square of sums is: ' + str(z))

