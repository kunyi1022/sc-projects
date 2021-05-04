"""
File: caesar.py
Name: 林坤毅 Jordan
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program will ask user to enter a number to check the movement of alphabet's order, then user can enter a
    ciphered word or sentence base on their alphabet movement.
    Then function 'deciphered(x,y)' will transform those ciphered characters into right word or sentence.
    """
    secret = int(input('Secret number: '))
    string = input('What\'s the ciphered string?')
    string = string.upper()
    print('The deciphered string is: ' + deciphered(after_move(secret), string))


def deciphered(aftermove, string):
    """
    :param aftermove: str, moved alphabet series.
    :param string: str, ciphered word or sentence need to be deciphered.
    :return: str, deciphered word or sentence.
    """
    ans = ""
    for i in range(len(string)):
        j = aftermove.find(string[i])
        # j is the position of string[i] in moved alphabet series
        if j >= 0:
            # alphabet
            character = ALPHABET[j]
            ans = ans + character
        else:
            # blank space
            ans = ans + string[i]
    return ans


def after_move(secret):
    """
    :param secret: int, the total right side movement that alphabet need to move.
    :return: sre, moved alphabet.
    """
    ans = ""
    back = ALPHABET[:26 - secret]
    front = ALPHABET[26 - secret:]
    new_alphabet = front + back
    ans += new_alphabet
    return ans

#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
