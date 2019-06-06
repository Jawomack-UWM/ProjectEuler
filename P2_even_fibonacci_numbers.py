#Find sum of even terms in fibonacci sequence that are under 4 mil.

i = 0
j=0
fib = [1,2]
next_num = 0
sum_next = 0


for i in range(50):
	if next_num > 4000000:
		break
	else:
		next_num = fib[i] +fib[i+1]
		print(next_num)
		fib.append(next_num)
print(fib)

for j in range(len(fib)):
	if fib[j]%2 == 0:
		sum_next = sum_next + int(fib[j])
		j += 1
	else:
		j += 1

print(sum_next)