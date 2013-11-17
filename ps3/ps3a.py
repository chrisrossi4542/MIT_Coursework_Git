# 6.00 Problem Set 3A Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

	The score for a word is the sum of the points for letters
	in the word multiplied by the length of the word, plus 50
	points if all n letters are used on the first go.

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    word_score = 0
    for i in word:
        word_score += SCRABBLE_LETTER_VALUES[i]
    word_score *= len(word)

    if len(word) == n:
        word_score += 50
    
    return word_score
 
    
    
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
	In other words, this assumes that however many times
	a letter appears in 'word', 'hand' has at least as
	many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = hand
    for i in word:
        new_hand[i] = hand.get(i) - 1
    return new_hand



#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    in_word_list = False
    instance_of_letter = 0
##    letter_in_hand = True
##    letter_not_in_hand = False
    for i in word_list:
        if i == word:
            in_word_list = True
    if in_word_list == False:
        return False
        exit
    return True

##this still doesnt work if the word has two r's but only one r is in my hand. 

    temp_hand = hand.copy()
    for i in word:
        if temp_hand.get(i,0) > 0:
            temp_hand[i] -= 1
        else:
            return False
            
        
##    for i in word:
##        if hand.get(i,0) > 0:
##            hand[i] -= 1
##        elif hand.get(i,0) < 0:
##            return False
##            exit

    return True

             

def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      
    """
    global HAND_SIZE
    word = ' '
    total_points = 0

    
    while word != '.':
        print'Current Hand:', display_hand(hand)
        word = raw_input('Enter word, or a "." to indicate that you are finished:')
        
        current_word_valid = is_valid_word(word, hand, word_list)

        if word == '.':
            print 'You have exited the round, please select another option.\n'

        elif current_word_valid == True:
            total_points += get_word_score(word, HAND_SIZE)
            HAND_SIZE -= len(word)
            update_hand(hand, word)
            print '"', word, '" earned',get_word_score(word, HAND_SIZE), 'points. Total:', total_points, 'points'
    
        elif current_word_valid == False:
            print 'Invalid word, please try again.'

        


    print "Total score: ", total_points, "."
    



#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    game_options = 'z'
    global HAND_SIZE
    print 'Welcome to the word game!\n Options are as follows:\n'
    print 'Enter "n" to play a new random hand\n'
    print 'Enter "e" to exit the game\n'

    while game_options != 'e':
        game_options = raw_input('Please select an option: ')

##I feel pretty strongly that I need to use recursion here. Need to go back and make sure I understand that
        
    
        if game_options == 'n':
            ## not sure why dealt_hand is getting updated when I play a hand
            dealt_hand = deal_hand(HAND_SIZE)
##            print "current full hand: ", current_full_hand
            current_hand = dealt_hand.copy()
##            print "current in use hand: ", current_hand
            play_hand(current_hand, word_list)
##            print "current full hand after hand has been played:", current_full_hand
##            print "current in use hand after hand is played: ", current_hand

        elif game_options == 'r':
            play_hand(dealt_hand, word_list)

        elif game_options == 'e':
            exit

        else:
            print 'Welcome to the word game!\n Options are as follows:\n'
            print 'Enter "n" to play a new random hand\n'
            print 'Enter "r" to play the last hand again\n'
            print 'Enter "e" to exit the game\n'
            game_options = raw_input('Please select an option: ')


#
# Build data structures used for entire session and play game
#
##if __name__ == '__main__':
##    word_list = load_words()
##    play_game(word_list)

##word_list = load_words()
##hand = {'a': 1, 'c': 1, 'i': 1, 'h': 1, 'm':2, 'z':1}
##word = "him"
##print is_valid_word(word,hand,word_list)

##play_hand(hand, word_list)
