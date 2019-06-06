#Find the largest palindrome made from the product of two 3-digit numbers

# def pal(x):

# 	word = str(x)
# 	l = list(word)
# 	new = l[::-1]
# 	new_word = ''.join(new)
# 	list_of_palindrones = []
# 	first_pal = 0

# 	if word == new_word:
# 		print('%s is a palindrone' %word)
# 		test_pal = word
# 		if test_pal > first_pal:
# 			first_pal = test_pal
		
# 	else:
# 		print('%s is not a palindrone' %word)


first_pal = 0
for i in range(100,1000):
	for j in range(100,1000):
		k = i * j 
		word = str(k)
		l = list(word)
		new = l[::-1]
		new_word = ''.join(new)
		

		if word == new_word:
			test_pal = int(word)

			if test_pal > first_pal:
				first_pal = test_pal
			else: 
				pass

		else:
			pass

print(first_pal)