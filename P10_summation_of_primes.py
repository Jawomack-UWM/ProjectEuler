#Find the sum of all primes below 2 million

#make list of all primes belows 2 million

# sum the list


# def prime_num_list(x):
# 	#creates a list of prime numbers below x
# 	prime = []

# 	for p in range(2, x+1):
# 		for i in range(2,p):
# 			if p % i == 0:
# 				break
# 		else:
# 			prime.append(p)

# 	return prime
# 	print('Done')

import eulerlib

def summation_of_primes(x):
	list_primes = eulerlib.primes(x)
	sum_of_list = sum(list_primes)
	return sum_of_list


if __name__ == '__main__':
	print(summation_of_primes(2000000))