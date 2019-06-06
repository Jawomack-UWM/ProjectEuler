
def normal_year(x):
	days_in_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	running_days = 1
	num_of_sun_first_of_month = 0
	for i in range(len(days_in_year)):
		running_days = running_days + days_in_year[i]
		
		if running_days % 7 == 0:
			num_of_sun_first_of_month +=1
			print(running_days)
		print(running_days)
	else: 
		print(num_of_sun_first_of_month)

def leap_year(x):
	days_in_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	running_days = 1
	num_of_sun_first_of_month = 0
	for i in range(len(days_in_leap_year)):
		running_days = running_days + days_in_leap_year[i]
		
		if running_days % 7 == 0:
			num_of_sun_first_of_month +=1
			print(running_days)
		print(running_days)
	else: 
		print(num_of_sun_first_of_month)


year = 1901
final_year = 2000
if year % 400 == 0:
	leap_year()
	year += 1

elif year % 100 == 0:
	normal_year()
	year += 1

elif year % 4 == 0:
	leap_year()
	year += 1
else:
	normal_year()
	year +=1
# running_day = running_days + month

# #starting date = 1 jan 1901 which is a tuesday, so check will have to = 6
# #start is on a monday

# if num % 7 == 0:
# 	print('Its a sunday')
# 	num_of_sun += 1


