#determine the largest prime factor for the number 600,851,475,143

n = 600851475143
largest_factor = 1

#remove any factors of 2 (even factors)
while n % 2 == 0: 
    largest_factor = 2
    n = n/2

#cycle through odd factors
p = 3
while n != 1:
    while n % p == 0:
        largest_factor = p
        n = n/p
    p += 2

print(largest_factor)

