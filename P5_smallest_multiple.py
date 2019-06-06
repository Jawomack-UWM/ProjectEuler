

# for i in range(2520,400000000):
# 	for j in range(2,22):
# 		if j == 21:
# 			print(i)
			
# 		elif i%j == 0:
# 			continue
# 		else:
# 			break



# for x in range(10):
#     for y in range(10):
#         print(x*y)
#         if x*y > 50:
#             break
#     else:
#         continue  # executed if the loop ended normally (no break)
#     break  # executed if 'continue' was skipped (break)



check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def find_solution(step):
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

if __name__ == '__main__':
    solution = find_solution(20)
    if solution is None:
        print("No answer found")
    else:
        print("found an answer:", solution)