"""
File: hangman.py
Name: 林坤毅 Jordan
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program will first import a random word from Jerry's function 'random_word()'
    Second, it will show a hint contains only hyphens(-), which the number of hyphens will match the length of answer.
    Last, user can start playing the hangman game with only 7 choices to make mistake.
    """
    answer = random_word()
    header(answer)
    input_ch(answer, N_TURNS)


def input_ch(answer, nturn):
    """
    :param answer: str, the answer for this hangman game.
    :param nturn: the number of guesses left.
    """
    x = old_word(answer)
    # temporary answer
    while True:
        result = 'no'
        input_ch = input('Your guess: ')
        finalinput = input_ch.upper()
        ch_or_not_ch = finalinput.isalpha()

        if ch_or_not_ch != True or len(finalinput) != 1:
            # format is wrong
            print('illegal format.')

        else:
            # format is right
            if nturn > 1:
                for ch in answer:
                    if finalinput == ch:
                        temp = replace(x, ch, answer)
                        x = temp
                        # change the temporary answer x
                        result = 'yes'
                        # setting 'result = yes' is for repeat characters in answer
                        # If I add you are correct... here, it will repeat for the same character in answer

                if result == 'yes':
                    if x == answer:
                        print('You are correct!')
                        print('You win!!')
                        print('The word was: ' + answer)
                        break
                    print('You are correct!')
                    print('The word looks like: ' + temp)
                    print('You have ' + str(nturn) + ' guesses left.')

                else:
                    nturn -= 1
                    print('There is no ' + str(finalinput) + '\'s in the word.')
                    print('The word looks like:' + x)
                    print('You have ' + str(nturn) + ' guesses left.')

            elif nturn == 1:
                print('There is no ' + str(finalinput) + '\'s in the word.')
                print('You are completely hung ：（')
                print('The word was: ' + answer)
                break


def replace(temporaryans, enterword, answer):
    """
    :param temporaryans: str, temporary answer.
    :param enterword: str, the character that user guesses.
    :param answer: str, the answer for this hangman game.
    :return: str, the temporary answer after hyphens replacement.
    """
    # s = replace('-----', 'A', answer)
    while True:
        i = answer.find(enterword)
        if i >= 0:
            y = temporaryans[:i]
            # ---
            y += enterword
            # ---A
            y += temporaryans[i+1:]
            # ---A-
            temporaryans = y
            answer = answer[:i] + '-' + answer[i+1:]
        else:
            ans = y
            break
    return ans


def old_word(answer):
    """
    :param answer: str, the answer for this hangman game.
    :return: str, hyphens(-).
    """
    ans = ""
    for i in range(len(answer)):
        ans += '-'
    return ans


def header(answer):
    """
    :param answer: str, the answer for this hangman game.
    :return: str, Hints for the hangman game.
    """
    n = ""
    for i in range(len(answer)):
        n = n + '-'
    print('The word looks like: ' + n)
    print('You have 7 guesses left.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"

#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
