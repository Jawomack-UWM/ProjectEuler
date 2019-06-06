#Determine the product of abc given, a < b <c, a^2 + b^2 = c^2, and that a + b + c = 1000

def product_pythagorean_triplet():
	#since  c > b > a  we nest for loops with the max range being less than the current
	for c in range(1,1000):
		for b in range(1, c):
			for a in range(1, b):
				if c ** 2 == (a ** 2) + (b **2) and 1000 == (a + b + c):
					return(a, b, c)
	

(a, b, c) = product_pythagorean_triplet()
print(a)
print(b)
print(c)
z = a * b * c
print('The product of the pythagorean triplet is ', z)


