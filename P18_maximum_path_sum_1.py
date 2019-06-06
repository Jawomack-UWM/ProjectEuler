x = ('''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''.splitlines())
#separates the variable by line creating a string for each \n
#['75', '95 64', ......etc until the end] 

d = {} #int
for i in range(len(x)):
	d[i] = list(map(int, x[i].split()))
	#Split function separates each element of list replaceing space with commas
	#elem0 = ['75'], elem1 = ['95','64'] 
	#int, map, list takes all those strings converting them into int
	#then creates a dictionary to store the lists in
#print(d)

for i in d:
	d[i] = max(d[i])
	#replaces each dictionary value with the max value in the list
#print(d)

running_num = 0

for i in d:
	#sums up the max dictionary values in var running_num
	running_num += d[i]
	#print(running_num)
print('The sum of the max path is: ', running_num)



#random work i tried
#------------------------------
#d[i] = (int(x[i]))
# for i in range(len(x)):
# 	print(max(d.value(i))

#print(x)

# y = []
# #print(x)
# #print(len(x))
# for i in range(len(x)):
# 	y = x[i].split
# 	print(y)
# #x = [int(i) for i in x.split()]
# print(y)
# for i in range(len(x)):
# 	y.append(x[i].replace(' ',','))
# print(y)
# for i in range(len(x)):
#  	y[i] = list(map(int, y[i]))
# print(x)
