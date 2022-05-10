import random
from tokenize import blank_re

random_words = [
    'arsenal', 'aardvark', 'beetlejuice', 'cairo', 'portland', 'disguise', 'geography', 'volcano',
    'sandwiche', 'pineapple', 'beetroot', 'giraffe'
]

lives = 7
guessed_list = []


def pick_random_word(word_list):
    index = random.randint(0, len(word_list))
    return word_list[index]

def user_guess(blank_string):
    while True:
        guess = input('Please Choose A Letter: ' )
        if guess.isdigit() or len(guess) != 1:
            print('\n', 'Please enter one letter from A - Z', '\n')
        elif guess in blank_string:
            print('\n', 'You have already tried that, Trysomething new', '\n')
        else:
             return guess

def check_game_win(list):
    if '_' not in list:
        print('\n', 'Congradultions you won the game!', '\n')
        global lives
        lives = 7
        replay = input('Do you want to play again? : ')
        if replay.lower() == 'y':
            print('\n', 'Get Ready to play', '\n')
            main()
        elif replay.lower() == 'n':
            print('\n', 'Sorry to hear that , goodbye')
            quit()
        else: print('\n', 'Please enter a valid response, either y or n ', '\n')
    else:
        return

def check_game_over(random_word):
    global lives
    if lives <= 0:
        print('\n', 'Unlucky - Game Over', '\n')
        print('\n', f"The random word was \n \n -- {random_word} --", '\n')
        lives = 7
        while True:
            replay = input('Do you want to play again? : ')
            if replay.lower() == 'y':
                print('\n', 'Get Ready to play', '\n')
                main()
            elif replay.lower() == 'n':
                print('\n', 'Sorry to hear that , goodbye')
                quit()
            else: print('\n', 'Please enter a valid response, either y or n ', '\n')
    else: return


def check_guess(random_word, blank_string):
    while True:
        global guessed_list
        guess = user_guess(guessed_list)
        guessed_list.append(guess)
        if guess in random_word:
            for i in range(len(random_word)):
                if random_word[i] == guess:
                    blank_string[i] = guess
            print('\n')
            for space in blank_string:
                print(space, sep='', end='')
            print('\n')                
        else:
            global lives
            lives = lives-1
            check_game_over(random_word)
            print('\n', f"You have {lives} lives left", '\n')
            for i in blank_string:
                print(i, sep='', end='')
            print('\n')
        check_game_win(blank_string)


def main():
    global guessed_list
    guessed_list = []
    print('\n', 'Welcome to Hangman', '\n')
    while True:
        answer = input('Do you wish to proceed with the game? Please choose Y / N: ')
        if answer.lower() == 'y':
            print('\n', 'Get Ready to play', '\n')
            break
        elif answer.lower() == 'n':
            print('\n', 'Sorry to hear that , goodbye')
            quit()
        else: print('\n', 'PLease enter a valid response, either y or n ', '\n')
    random_word = pick_random_word(random_words)
    blank_string = len(random_word) * ['_']
    for i in blank_string:
        print(i, sep='', end='')
    print('\n')
    check_guess(random_word, blank_string)

main()