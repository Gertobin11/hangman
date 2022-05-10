import random
import draw_hangman
from pyfiglet import Figlet
from termcolor import colored, cprint

random_words = [
    'arsenal', 'aardvark', 'beetlejuice', 'cairo', 'portland', 'disguise', 'geography', 'volcano',
    'sandwiche', 'pineapple', 'beetroot', 'giraffe'
]

options = ['Play ','Rules', 'Quit']

lives = 7

guessed_list = []

f = Figlet(font='banner3-D')

print_red = lambda x: cprint(x, 'red')
print_green = lambda x: cprint(x, 'green')


def pick_random_word(word_list):
    index = random.randint(0, (len(word_list) -1))
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

def draw_hangman_game(lives):
    if lives == 7:
        draw_hangman.all_lives()
    elif lives == 6:
        draw_hangman.six_lives()
    elif lives == 5:
        draw_hangman.five_lives()
    elif lives == 4:
        draw_hangman.four_lives()
    elif lives == 3:
        draw_hangman.three_lives()
    elif lives ==2:
        draw_hangman.two_lives()
    elif lives == 1:
        draw_hangman.one_life()
    else:
        draw_hangman.gameover_draw()


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
            global lives
            draw_hangman_game(lives)
            print_green('Correct!')
            print('\n')
            for space in blank_string:
                print(space, sep='', end='')
            print('\n')                
        else:
            lives = lives-1
            draw_hangman_game(lives)
            check_game_over(random_word)
            print_red(f"You have {lives} lives left")
            print('\n')
            for i in blank_string:
                print(i, sep='', end='')
            print('\n')
        check_game_win(blank_string)


def main():
    global guessed_list
    guessed_list = []
    print('\n \n')
    print(colored(f.renderText('Hangman'), 'green'))
    print('\n \n')
    print_green('Please choose from the following options')
    print('\n')
    for count, item in enumerate(options,1):
        print(count, item, end='               ')
    print('\n')
    while True:
        answer = input('Enter 1, 2 or 3 : ')
        if answer== '1':
            print('\n')
            print_green('Game Loading...')
            print('\n')
            break
        elif answer.lower() == 'n':
            print('\n', 'Sorry to hear that , goodbye')
            quit()
        else: print('\n', 'PLease enter a valid response, either y or n ', '\n')
    random_word = pick_random_word(random_words)
    blank_string = len(random_word) * ['_']
    draw_hangman.all_lives()
    for i in blank_string:
        print(i, sep='', end='')
    print('\n')
    check_guess(random_word, blank_string)

main()