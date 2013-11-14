from ps3a import *
import time
from perm import *
word_list = load_words()

#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
   """
    
    n = len(hand)
    while n > 0:
        list_of_possible_words = get_perms(hand, n)
        n -= 1
        for i in list_of_possible_words:
            if is_valid_word(i, hand, word_list) == True:
                return i
    return None




#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.
     * The computer chooses a word using comp_choose_words(hand, word_dict).
     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.
     * The sum of the word scores is displayed when the hand finishes.
     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    
    #temp hand
    n = len(hand)
    total_points = 0
    chosen_word = comp_choose_word(hand, word_list)
    print'Current Hand:', display_hand(hand)
    while chosen_word != None:
        chosen_word_score = get_word_score(chosen_word, n)
        print '"', chosen_word, '" earned',chosen_word_score, 'points.'
        total_points += chosen_word_score
        update_hand(hand, chosen_word)
        chosen_word = comp_choose_word(hand, word_list)
    
    print "Total score: ", total_points, "."
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
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
            print 'Enter "u" to play the hand yourself\n'
            print 'Enter "c" to have the computer play a hand\n'
            game_options = raw_input('Please select an option: ')

            if game_options == 'u':
                dealt_hand = deal_hand(HAND_SIZE)
                current_hand = dealt_hand.copy()
                play_hand(current_hand, word_list)
            elif game_options == 'c':
                dealt_hand = deal_hand(HAND_SIZE)
                current_hand = dealt_hand.copy()
                comp_play_hand(current_hand, wordlist)
            else:
                print 'Enter "u" to play the hand yourself\n'
                print 'Enter "c" to have the computer play a hand\n'
                game_options = raw_input('Please select an option: ')

        elif game_options == 'r':
            print 'Enter "u" to play the hand yourself\n'
            print 'Enter "c" to have the computer play a hand\n'
            game_options = raw_input('Please select an option: ')

            if game_options == 'u':
                play_hand(dealt_hand, word_list)

            elif game_options == 'c':
                comp_play_hand(current_hand, wordlist)

        elif game_options == 'e':
            exit

        else:
            print 'Welcome to the word game!\n Options are as follows:\n'
            print 'Enter "n" to play a new random hand\n'
            print 'Enter "r" to play the last hand again\n'
            print 'Enter "e" to exit the game\n'
            game_options = raw_input('Please select an option: ')



    # TO DO...
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words
    play_game(word_list)


##hand = {'a': 1, 'c': 1, 't': 1, 'h': 0, 'm':0, 'z':0}
##print comp_choose_word(hand, word_list)
    
