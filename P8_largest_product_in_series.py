#cycles through 1000 digit number, selecting a group of num and finding the highest multiply of groupings

def largest_product_in_a_series(test_num, num_of_adj_digits):
	test_list = list(str(test_num)) #turns integer into string and then list to cycle through
	len_of_list = len(test_list)
	running_num = 1 #intitiation
	highest_multiple = 1 #int
	#print('length of list: ', len_of_list)
	#print('num of adj: ', num_of_adj_digits)

	

	for pos in range(len_of_list - 1):
		#print('i = ', pos)
		if pos ==  len_of_list - num_of_adj_digits+1:
			#breaks the iterations of list before loop accessed list element not there
			break

		for chunk in range(0, num_of_adj_digits):
			#print('j = ', chunk)
			running_num = running_num * int(test_list[pos + chunk])
			#multiples elements of list together and stores in variable
			#print('running num is: ', running_num)
			
		else: 
			if running_num > highest_multiple: 
				highest_multiple = running_num
				#saves highest_multiple number
				#print('highest_multiple is: ', highest_multiple)
				running_num = 1
				#resets running number to 1 otherwise running number will keep getting bigger and bigger
				#print('running_num reset')

			else: 
				running_num = 1
				#print('running_num reset')

	return highest_multiple
	#return has to be on outside of for loop
	
  #store big number as multi line string then turned into integer with 'int' has well as 
  #replaced \n with nothing ('')
x = largest_product_in_a_series(int( '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''.replace("\n", '')),13)
print('The highest product in the series is: ', x)
