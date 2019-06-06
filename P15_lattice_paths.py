#determines the number of possible paths in a 20x20 grid only being able to move to the right and down
#Have to use a combination
#Since each square presents two options we get (2n n)

import math

def nCr(n,r):
	f = math.factorial
	return f(n) / f(r) / f(n-r)

print(nCr(40,20))


