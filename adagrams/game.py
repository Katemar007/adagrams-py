from random import randint
import random
from collections import Counter

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

LETTERS_LIST = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L', 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V', 'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']


def draw_letters():
    
    tiles = []
    for x in range(10):
        random_integer = random.randint(0, len(LETTERS_LIST)-1)
        letter = LETTERS_LIST[random_integer]
        if tiles.count(letter) == LETTER_POOL[letter]:
            break
        #tiles.append(LETTERS_LIST[random_integer])
        tiles.append(letter)
    return tiles

    

def uses_available_letters(word, letter_bank):
    # for number in range(len(word)):
    #     for letter in word:
    #         if letter_bank.count(letter) >= word.count(letter):
    #             continue
    #         elif letter not in letter_bank or letter_bank.count(letter) < word.count(letter):
    #             return False
    #         return True   
    word = word.upper()
    word_counts = Counter(word)
    letter_bank_counts = Counter(letter_bank)
    
    for letter, count in word_counts.items():
        if letter_bank_counts[letter] < count:
            return False
    
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass
