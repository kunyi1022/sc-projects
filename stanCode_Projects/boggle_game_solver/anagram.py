"""
File: anagram.py
Name: 林坤毅 Jordan
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
FILE2 = 'test.txt'            # Test use (easy)

# Global Variable
dictionary = []
final_ans = []


def main():
    read_dictionary()
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        if s == '-1':
            break
        else:
            find_anagrams(s)


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    global dictionary
    with open(FILE, 'r') as f:
        for line in f:
            dictionary.append(line[:len(line)-1])


def find_anagrams(s):
    """
    :param s: (str) the word that user keyed.
    :return: all anagrams from the word user typed.
    """
    print('Searching...')
    helper(s, [], '')
    print(str(len(final_ans)) + ' anagrams: ' + str(final_ans))

    # clear all the answers in final_ans to make program run endless
    for i in range(len(final_ans)):
        final_ans.pop()


def helper(s, current_lst, ans):
    """
    :param s: (str) The word that user keyed.
    :param current_lst: (list) A list store numbers that converted from original word.
    :param ans: (list) A list store all the anagrams from word s.
    :return: (base-case) All the anagrams from word s.
    """
    # base case
    if len(current_lst) == len(s):
        for j in range(len(s)):
            ans += s[int(current_lst[j])]
        if ans in dictionary and ans not in final_ans:
            final_ans.append(ans)
            print('Found: ' + ans)
            print('Searching...')

    else:
        for i in range(len(s)):
            # !!!! USE number to do permutation, instead of string (repeat character will have trouble)
            if str(i) not in current_lst:
                # Choose
                ele = str(i)

                # Explore
                current_lst += [ele]
                # string manipulation to explore
                sub_s = ''
                for k in range(len(current_lst)):
                    sub_s += s[int(current_lst[k])]
                if has_prefix(sub_s):
                    helper(s, current_lst, ans)

                # Un-choose
                current_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s:
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True



if __name__ == '__main__':
    main()
