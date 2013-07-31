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


wordlist = load_words()
# your code begins here!
guesses_left = 8

def hangman():
    random_word_pick = choose_word(wordlist)
    return random_word_pick

def guess():
    guess = raw_input('Please guess a letter:')
    
    print 'Good guess:'
    for i in len(random_word_pick):
        if guess == i:
            print guess
        else:
            print '_'
    print '----------'
    guesses_left =- 1



random_word_pick = hangman()
print 'Welcome to the game, Hangman!\nI am thinking of a word that is',
print len(random_word_pick), 'letters long.\n-------------\n You have', guesses_left, 'guesses left.'

print random_word_pick
