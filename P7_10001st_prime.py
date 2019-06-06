#Calculates prime numbers, and stores them into a list.

def calc_prime_num(x):
	prime = []
	counter = 0
	for p in range(2, x+1):
	    for i in range(2, p):
	        if p % i == 0:
	            break
	    else:
	        #print(p)
	        prime.append(p)
	        counter +=1
	        #print('counter = ', counter)
	        if counter == 10001:
	        	break
	return prime
	print('Done')

x = calc_prime_num(1000000000000000000)
#print('x is equal to: ', x)
print('The 10001 prime number is ', x[-1])
