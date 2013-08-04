# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program

alphabet = 'abcdefghijklmnopqrstuvwxyz'
available_letters = list(alphabet)
guesses_left = 8
wordlist = load_words()
guessed_letters =[]
word_construction = []
# your code begins here!

##def avail_letters(last_guess, current_letters):
##    
##    for i in current_letters:
##        if current_letters[i] == last_guess:
##            current_letters = current_letters - current_letters[:i]
##    return current_letters

def guess(random_word_pick):
    global available_letters
    global word_construction
    global guessed_letters
    global guesses_left
        
    print 'Available letters:', ", ".join(available_letters)
    guess = raw_input('Please guess a letter:')

    while guess not in available_letters:
        print 'That letter has already been guessed.'
        guess = raw_input('Please guess a letter:')

    available_letters.remove(guess)
    guessed_letters.append(guess)
    count = 0
    current_indice = 0

    for i in random_word_pick:
        if guess == i:
            print 'Good guess:'
            count = 1
                    
    if count != 1:
        print 'Oops! That letter is not in my word:'
        
    for i in random_word_pick:
        if i in guessed_letters:
            print i,
        else:
            print '_',

    for i in random_word_pick:
        if i in guessed_letters:
            word_construction[current_indice] = i
        else:
            word_construction[current_indice] = ' '
        current_indice += 1

    guesses_left -= 1
    if list(random_word_pick) == word_construction:
        guesses_left = -1
        
    print '\n----------'
    

    if guesses_left == 0:
        print 'You are out of guesses, better luck next time!'
        
    elif guesses_left == -1:
        print 'Congratulations, you guessed the word!'
        
    else:
        print 'You have',guesses_left,'guesses left.'

def hangman():
    global available_letters
    global guessed_letters
    global word_construction
    guessed_letters =[]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    available_letters = list(alphabet)
    global guesses_left
    guesses_left = 8
    random_word_pick = choose_word(wordlist)
    print 'the random word pick is', random_word_pick
    for i in random_word_pick:
        word_construction.append(' ')

    print 'Welcome to the game, Hangman!\nI am thinking of a word that is',
    print len(random_word_pick), 'letters long.\nYou have 8 guesses left.\n'

    
    while guesses_left>0:
        guess(random_word_pick)


hangman()
