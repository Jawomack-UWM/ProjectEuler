#Determines the value of the first triangle number to have over five hundred divisors
import math

# def triangle_numbers(x):
# 	tri_num = 0
# 	for i in range(1, x+1):
# 		tri_num += i 
# 	print(tri_num)
# 	return(tri_num)

def num_of_divisors(n):
	number_of_factors = 0
	for i in range(1, int(math.ceil(math.sqrt(n)))):
		if n % i == 0:
			number_of_factors += 2
		else:
			continue
	return number_of_factors

x=1
for i in range(2,1000000):
	x += i 
	if num_of_divisors(x) >= 500:
		print(x)
		break
# 	if k > 500:
#  		print('The highly divisible triangular number is: ', y)
#  		break
# else: 
# 	#prints to console if no solution is found
# 	print('Program done iterating')




