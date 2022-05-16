import random
import draw_hangman
from pyfiglet import Figlet
from termcolor import colored, cprint
from time import sleep

random_words = [
    'arsenal', 'aardvark', 'beetlejuice', 'cairo', 'portland', 'disguise', 'geography', 'volcano',
    'sandwiche', 'pineapple', 'beetroot', 'giraffe'
]

rules_string = ('To play the game you must simply guess the correct randomly generated word.\n'
                'The game starts with an empty space for each letter of the word and the layer has 7 lives\n'
                'to guess the correct letters in the word. After each incorrect guess the player will lose\n'
                'a life and a piece of the person is drawn onto the gallows. If the player loses all of their\n'
                'lives the game is over and the player has lost. If the player has guessed it correctly with\n'
                'any lives left, the player has won!')

""" Global variables """

options = ['Play ','Rules', 'Quit']
lives = 7
guessed_list = []
f = Figlet(font='banner3-D')
f2 = Figlet(font='cybermedium')

""" Functions to print green and red """

print_red = lambda x: cprint(x, 'red')
print_green = lambda x: cprint(x, 'green')


def pick_random_word(word_list):
    """ Generate a random word from the word list """
    index = random.randint(0, (len(word_list) -1))
    return word_list[index]

def rules():
    """ Dispaly The rules in a typewriter effect """
    global rules_string
    print('\n')
    print_green(f2.renderText('The Rules'))
    print('\n')
    for char in rules_string:
        print(char, end='', flush=True)
        sleep(0.04)
    print('\n')
    back = input('Press any key followed by  Enter to return: ')
    if back:
        main()

def user_guess(blank_string):
    """ Function takes a user guess an validates it is a letter and has not been guessed before """
    while True:
        guess = input('Please Choose A Letter: ' ).lower()
        if guess.isdigit() or len(guess) != 1:
            print('\n', 'Please enter one letter from A - Z', '\n')
        elif guess in blank_string:
            print('\n', 'You have already tried that, Try a different letter', '\n')
        else:
             return guess

def restart_game():
    """ Function to restart the game or exit it"""
    while True:
        replay = input('Do you want to play again? : ')
        if replay.lower() == 'y':
            print('\n', 'Get Ready to play', '\n')
            main()
        elif replay.lower() == 'n':
            print('\n', 'Sorry to hear that , goodbye')
            quit()
        else: print('\n', 'Please enter a valid response, either y or n ', '\n')

def check_game_win(list):
    """ Function to check  if the player has won """
    if '_' not in list:
        print('\n')
        print_green(f2.renderText('Congratultions you won the game!'))
        print('\n')
        global lives
        print(f'You won with {lives} lives left !')
        print('\n')
        if lives == 7:
            print_green(f2.renderText('FLAWLESS VICTORY'))
        lives = 7
        restart_game()
    else:
        return

def check_game_over(random_word):
    """ Function checking whether the player has lost"""
    global lives
    if lives <= 0:
        print('\n')
        print_red(f2.renderText('Unlucky \n Game Over'))
        print('\n', f"The random word was \n \n -- {random_word} --", '\n')
        lives = 7
        restart_game()
    else: return

def draw_hangman_game(lives):
    """ Function to draw the hangman with respect to the players lives """
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
    """ Function to check whether the guess is in the random word """
    while True:
        global guessed_list
        guess = user_guess(guessed_list)
        guessed_list.append(guess)
        if guess in random_word:
            """ Looping through the blank word for multiple instances of the guessed word"""
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
            """ Remove a LIfe and redraw the hangman """
            lives = lives-1
            draw_hangman_game(lives)
            check_game_over(random_word)
            print_red(f"You have {lives} lives left")
            print('\n')
            for i in blank_string:
                print(i, sep='', end='')
            print('\n')
        check_game_win(blank_string)

def main_menu():
    """ Function for the player to chose to play , see the rules or exit """
    print_green('Please choose from the following options')
    print('\n')
    for count, item in enumerate(options,1):
        print(count, item, end='               ')
    print('\n')
    while True:
        answer = input('Press 1, 2 or 3, then Enter\n')
        if answer== '1':
            print('\n')
            print_green('Game Loading...')
            print('\n')
            return
        elif answer == '2':
            rules()
        elif answer == '3':
            quit()
        else: print('\n', 'PLease enter a valid response 1, 2 or 3', '\n')

def main():
    global guessed_list
    guessed_list = []
    print('\n \n')
    print(colored(f.renderText('Hangman'), 'green'))
    print('\n \n')
    main_menu()
    random_word = pick_random_word(random_words)
    blank_string = len(random_word) * ['_']
    draw_hangman.all_lives()
    for i in blank_string:
        print(i, sep='', end='')
    print('\n')
    check_guess(random_word, blank_string)

main()