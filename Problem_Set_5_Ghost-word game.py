# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print ("  ", len(wordlist), "words loaded.")
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

word_list = load_words()
player_turn=True  #True if player 1, False if player 2
start=True
print('Welcome to Ghost')
word_fragment=''


def ghost():
    global word_fragment
    global start
    global player_turn
    if start==True:
        print('Welcome to Ghost')
        print('Player 1 goes first.')
        print('Current word fragment:'+ ' ')
        letter=input('Player 1 says letter: ')
        word_fragment=word_fragment+letter
        player_turn=False
        start=False
    print('Current word fragment:'+ word_fragment)
    if possible_words(word_fragment)==False:
        if player_turn==False:
             print('Player 1 loses because no word starts with'+word_fragment)
             return 
        else:
             print('Player 2 loses because no word starts with'+word_fragment)
             return 
    if len(word_fragment)>=3 and word_fragment  in word_list:
        if player_turn==False:
             print('Player 1 loses because '+word_fragment+' is a word')
             return 
        else:
             print('Player 2 loses because '+word_fragment+' is a word')
             return 
    if player_turn==True:
        print('Player 1 turn')
        letter=input('Player 1 says letter: ')
        word_fragment=word_fragment+letter
        player_turn=False
        ghost()
        return
    else:
        print('Player 2 turn')
        letter=input('Player 2 says letter: ')
        word_fragment=word_fragment+letter
        player_turn=True
        ghost()
        return
    
    
    
    
def possible_words(fragment):
    for word in word_list:
        length=len(fragment)
        part_word=word[0:length]
        if fragment==part_word:
            return True
    return False