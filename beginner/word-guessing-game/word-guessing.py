# word guessing game

# ---- Word bank ----
# stored in words.txt
# each line is a different word and is the pool of words

# ---- Read the file ----
# When reading lines from a file, they have newline character at the end \n
# Therefore, we have to srip that to clean them and put into a list

# ---- Select a random word ----
# game needs to pick one word at random for player to guess
# method 1 : generate a random number and use it as an index
# method 2 : use random.choice() to automatically do it

import random

word_list =[]
game_title = 'Word Raider'
# track infromation
misplaced_guess = []
incorrect_guess = []
max_turns = 5
turns_taken = 0

# just to open -> file = open("words.txt","r")
# use both open and close
with open("words.txt","r") as file:
    # loop through line by line of the file
    for line in file:
        # print(line)
        clean_words = line.strip()
        word_list.append(clean_words)
    
print(word_list)

# pick a random word for user to guess from the list
word_to_guess = random.choice(word_list)
print(word_to_guess)

# intial game state
print("Welcome to", game_title)
print("The word has", len(word_to_guess), "letters.")
print('You have', max_turns-turns_taken, 'turns left')