#finds the sum of the digits of a factorial.  Ex 10! = 3628800, 3+6+2+8+8+0+0 = 27
#find sum of digits in number 100!

import math

num_to_run = 100
factorial_of_num = math.factorial(num_to_run)
#print(factorial_of_num)

list_of_num = list(str(factorial_of_num))
#print(list_of_num)

total = 0

for i in list_of_num:
	total = total + int(i)
print('The sum of digits is: ', total)