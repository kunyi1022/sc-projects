"""
File: largest_digit.py
Name: 林坤毅 Jordan
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
# Global variable: Calculating Big O
# x = 0

def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9
	# print(x)


def find_largest_digit(n):
	"""
	:param n: int, the number send to be processed
	:return: int, the maximum digit of a number
	"""
	# calculate Big O
	# global x
	# x += 1

	n = abs(n)

	# get the remainder of n/10
	num = n % 10

	# Only one digit left
	if int(n/10) == 0:
		return n
	# two digits left
	else:
		return max(num, find_largest_digit(n//10))














	# compare_num_1 = n % 10
	# compare_num_2 = (n//10) % 10
	# bigger = max(compare_num_1, compare_num_2)
	# if int(n/10) == 0 and n//10 == 0:
	# 	return n
	# elif n//10 < 10:
	# 	return bigger
	# else:
	# 	find_largest_digit(n//10)







if __name__ == '__main__':
	main()
