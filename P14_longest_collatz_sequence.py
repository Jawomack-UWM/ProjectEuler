#Deteremines the longest chain of collatz sequence

def longest_collatz_sequence(x):
	counter = 0 #includes starting number
	longest_chain = 0
	num_makes_longest_chain = 0

	for n in range(1, x):

		test = n

		while n > 1:

			if n % 2 == 0:
				#number is even
				n = n / 2
				counter += 1

			else:
				#number is odd
				n = 3 * n +1
				counter += 1

		if counter > longest_chain:
			longest_chain = counter
			counter = 1 #reset counter
			num_makes_longest_chain = test
			print(num_makes_longest_chain)
			

		else: 
			counter = 1
			
	return(num_makes_longest_chain, longest_chain)

def single_num_chain(n):
#single version of the collatz sequence for testing purposes
	counter = 1

	while n != 1:

		if n % 2 == 0:
			n = n / 2
			counter +=1
			print(n)
		else:
			n = 3 * n + 1 
			counter +=1
			print(n)
	return counter

(x, y) = longest_collatz_sequence(1000000)
print('The number that produces the longest chain is ', x)
print('The longest chain is %d numbers long' %y)

# x = single_num_chain(14)
# print('The function returns %d numbers in the collatz sequence' %x)

