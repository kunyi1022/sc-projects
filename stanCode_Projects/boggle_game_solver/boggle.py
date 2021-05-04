"""
File: boggle.py
Name: 林坤毅 Jordan
----------------------------------------
This is a boggle game that user can type 4x4 characters square, and it will help
user find all exist word that can be found in 4x4 square by checking surrounding
character around each character.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global Variable
dictionary = []
first_lst = []
second_lst = []
third_lst = []
fourth_lst = []
boggle_dict = {}
dict_position = 0
ans_lst = []


def main():
	"""
	1. Read the dictionary.
	2. Ask user to type a 4x4 square (those characters will be store in four lists in one dict)
	3. Finding all the words in 4x4 square.
	"""
	read_dictionary()
	while True:

		# First row input
		first_row = input('1 row of letters: ')
		if len(first_row) != 7:
			print('Illegal input')
			break
		else:
			for i in range(len(first_row)):
				ch = first_row[i]
				if i % 2 == 0:
					first_lst.append(ch)

		# Second row input
		second_row = input('2 row of letters: ')
		if len(second_row) != 7:
			print('Illegal input')
			break
		else:
			for i in range(len(second_row)):
				ch = second_row[i]
				if i % 2 == 0:
					second_lst.append(ch)

		# Third row input
		third_row = input('3 row of letters: ')
		if len(third_row) != 7:
			print('Illegal input')
			break
		else:
			for i in range(len(third_row)):
				ch = third_row[i]
				if i % 2 == 0:
					third_lst.append(ch)

		# Fourth row input
		fourth_row = input('4 row of letters: ')
		if len(fourth_row) != 7:
			print('Illegal input')
			break
		else:
			for i in range(len(fourth_row)):
				ch = fourth_row[i]
				if i % 2 == 0:
					fourth_lst.append(ch)

		# Add input lists in dictionary
		boggle_dict[0] = first_lst
		boggle_dict[1] = second_lst
		boggle_dict[2] = third_lst
		boggle_dict[3] = fourth_lst
		break

	for y in range(len(boggle_dict)):
		for x in range(len(boggle_dict[y])):
			helper(y, x, '', [], ans_lst)
	# print(ans_lst)
	print(f'There are {len(ans_lst)} words in total.')


def helper(y, x, current_word, position_lst, ans_lst):
	"""
	:param y: (int) position value of y-axis
	:param x: (int) position value of x-axis
	:param current_word: (str) the string that keeps adding character and checking dictionary
	:param position_lst: (lst) store position tuple (y, x)
	:param ans_lst: (lst) store answer
	:return: (base-case) all the answer
	"""
	# 加位置在這裡錯誤
	# w = (y, x)
	# position.append(w)
	global dict_position

	# base case
	if len(current_word) >= 4 and current_word in dictionary:
		if current_word not in ans_lst:
			ans_lst.append(current_word)
			print('Found ' + '\"' + current_word + '\"')

			# removing current_word from dictionary to make sure roomy can be found after finding room
			for e in range(len(dictionary)):
				if current_word == dictionary[e]:
					dict_position = e
			dictionary.pop(dict_position)
			helper(y, x, current_word, position_lst, ans_lst)

	# recursive case
	else:
		for j in range(-1, 2, 1):
			for i in range(-1, 2, 1):
				# find 8 different positions except (x, y)
				f_x = x + i
				f_y = y + j
				if 0 <= f_x < len(boggle_dict[y]):
					if 0 <= f_y < len(boggle_dict):
						if (f_y, f_x) not in position_lst:

							# !!!! adding position tuple in position_lst to make sure position has been check
							position_lst.append((f_y, f_x))

							# Choose
							ele = boggle_dict[f_y][f_x]

							# Explore
							current_word += ele
							if has_prefix(current_word):
								helper(f_y, f_x, current_word, position_lst, ans_lst)

							# Un-choose
							current_word = current_word[:len(current_word)-1]
							position_lst.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary
	with open(FILE, 'r') as f:
		for line in f:
			dictionary.append(line[:len(line) - 1])


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True


if __name__ == '__main__':
	main()
