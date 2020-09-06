"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *

# Fill these in with your details
__author__ = "{{Lachlan Mohr}} ({{s4481974}})"
__email__ = "l.mohr@uqconnect.edu.au"
__date__ = "30/08/2020"

has_gotten_score = []

# Write your code here (i.e. functions)
def new_guess_line(guess_no, word_length, rowIndex):
	"""
	this is a function to create a new line inside the main game after a guess. This function is used in the create_guess_line function. Grabbing the tuples from a1_support that space out the index's depending on the guess number
	"""
	string = "Guess {}|".format(guess_no) 

	for x in range(word_length):													
			if x >= GUESS_INDEX_TUPLE[rowIndex][guess_no - 1][0] and x<=GUESS_INDEX_TUPLE[rowIndex][guess_no - 1][1]:			#this for loop starts printing stars or hyphens depending on what guess you are on
				string += " * |"																								#this function is used in the create_guess_line function. Grabbing the tuples from a1_support that space out the index's depending on the guess number	
			else:
				string += " - |"
	return string

worldlen_to_tuple_dictionary = {6:0,7:1,8:2,9:3}																				#this dictionary is simply for ease of use


def create_guess_line(guess_no, word_length):
	"""
	#this function is used to return the guess line associated with what guess you are up to, as different guesses require you to guess different parts of the word
	"""
	if word_length == 6:
		if guess_no == 1:
			return new_guess_line(1,6,0)
		elif guess_no == 2:
			return new_guess_line(2,6,0)
		elif guess_no == 3:
			return new_guess_line(3,6,0)
		elif guess_no == 4:
			return new_guess_line(4,6,0)
		elif guess_no == 5:
			return new_guess_line(5,6,0)
		elif guess_no == 6:
			return new_guess_line(6,6,0)
	if word_length == 7:
		if guess_no == 1:
			return new_guess_line(1,7,1)
		elif guess_no == 2:
			return new_guess_line(2,7,1)
		elif guess_no == 3:
			return new_guess_line(3,7,1)
		elif guess_no == 4: 
			return new_guess_line(4,7,1)
		elif guess_no == 5:
			return new_guess_line(5,7,1)
		elif guess_no == 6:
			return new_guess_line(6,7,1)
		elif guess_no == 7:
			return new_guess_line(7,7,1)
	if word_length == 8:
		if guess_no == 1:
			return new_guess_line(1,8,2)
		elif guess_no == 2:
			return new_guess_line(2,8,2)
		elif guess_no == 3: 
			return new_guess_line(3,8,2)
		elif guess_no == 4: 
			return new_guess_line(4,8,2)
		elif guess_no == 5:
			return new_guess_line(5,8,2)
		elif guess_no == 6:
			return new_guess_line(6,8,2)
		elif guess_no == 7:
			return new_guess_line(7,8,2)
		elif guess_no == 8:
			return new_guess_line(8,8,2)
	if word_length == 9:
		if guess_no == 1:
			return new_guess_line(1,9,3)
		elif guess_no == 2:
			return new_guess_line(2,9,3)
		elif guess_no == 3:
			return new_guess_line(3,9,3)
		elif guess_no == 4: 
			return new_guess_line(4,9,3)
		elif guess_no == 5:
			return new_guess_line(5,9,3)
		elif guess_no == 6:
			return new_guess_line(6,9,3)
		elif guess_no == 7:
			return new_guess_line(7,9,3)
		elif guess_no == 8:
			return new_guess_line(8,9,3)
		elif guess_no == 9:
			return new_guess_line(9,9,3)
	

def select_word_at_random(word_select):
	"""
	#this is my random word generator function. Depending on the input of the player, the function will return a word from either the words_fixed.txt file or the words_arbitrary.txt file.
	"""
	if word_select == "FIXED":
			loaded_word = load_words("FIXED")
			return loaded_word[random_index(loaded_word)]
	elif word_select == "ARBITRARY":
			loaded_word = load_words("ARBITRARY")
			return loaded_word[random_index(loaded_word)]
	else:
		return None




def compute_value_for_guess(word, start_index, end_index, guess):
	"""
	This function is for point scoring, this simply indexes each letter of the word and matches it with your guess, pulling the VOWELS and CONSONANT variables from a1support.py
	"""
	
	sliced_substring = word[start_index:end_index + 1] 			#this assigns the sliced_substring as an arrary from the start of the word up to an including the last letter. 
	
	points = 0
	
	for x in range(len(guess)):
		if guess[x] == sliced_substring[x]:						
			for y in range(len(VOWELS)):						#this is a for loop to check your guess letters at a given position (index) against the variable VOWELS in a1_supportand assigning 14 points if guessed in the correct position
				if guess[x] == VOWELS[y]:		
					points += 14
			for y in range(len(CONSONANTS)):					#as with the for loop above, this one does the same but checks for consonants in the CONSONANTS variable inside of a1_support
				if guess[x] == CONSONANTS[y]:
					points += 12
		else:
			for z in range(len(guess)):							#this loop just iterates over the guess and checks for any matching letter, regardless of position and assigns it 5 points
				if guess[z] == sliced_substring[x]:
					points += 5
		
	return points

def display_guess_matrix(guess_no, word_length, scores):
	"""
	the function here creates the displayed matrix. I have made it completely dynamic (so the length of word doesn't matter). By counting the required wall horizontals between each number, and printing them depending on word length.
	"""
	my_bool_array = [False] * word_length				
	for x in range(len(scores)):								#this boolean is for ease of use, used later on in the function to help with points not being printed if the guess has not been guessed.
		my_bool_array[x] = True

	string = "       {}".format(WALL_VERTICAL)

	for x in range(word_length):								#the loop here helps make the display matrix dynamic depending on the length of the word, it keeps adding numbers until it hits the full range of the word
		string += " {} {}".format(x+1, WALL_VERTICAL)				
	string += "\n{}".format(WALL_HORIZONTAL*9)
	for x in range(word_length):								#this is also used to make the display matrix dynamic, the number of wall horizontals between letters is 4, thus printing 4 for every letter in the word
		string += "{}".format(WALL_HORIZONTAL*4)

	for x in range(guess_no):
		
		string += "\n{}".format(create_guess_line(x + 1, word_length))
		
		if my_bool_array[x] == True:							#this boolean simply checks for the length of the guesses and halts printing of the scores if the guess hasn't actually been guessed yet
			string += "   {} Points".format(scores[x])

		string += "\n{}".format(WALL_HORIZONTAL*9)
		for x in range(word_length):
			string += "{}".format(WALL_HORIZONTAL*4)
	print(string)


def main():
	"""
	Handles top-level interaction with user.
	"""
	# Write the code for your main function here
	scores = ()
	game_word = None
	word_select = None
	word_length = None
	guess_no = 1
	has_quit = False

	print(WELCOME)
	while True:

		player_input = input(INPUT_ACTION)

		if player_input == "s":
			break
		elif player_input == "h":
			print(HELP)
			break
		elif player_input == "q":
			has_quit = True										#the boolean here is for ease of use. As for some reason we are not allowed to use the exit() function at any time. It changes the boolean to true and quits the game
			break
		else:
			print(INVALID)
	if has_quit == False:										#the game continues if the boolean is still false (only done by pressing 'h' or 's' and not 'q')
		while True:
			word_select = input("Do you want a 'FIXED' or 'ARBITRARY' length word?: ")
			if word_select == "FIXED":
				game_word = select_word_at_random("FIXED")
				break
			elif word_select == "ARBITRARY":
				game_word = select_word_at_random("ARBITRARY")
				break											#this loop assigns game_word to the random word picked from the select_word_at_random function
		
		word_length =len(game_word)

		for x in range(word_length):
			has_gotten_score.append(False)
		
		print("Now try and guess the word, step by step!!")
		
		for x in range(word_length):

			allowed_guess_length = 0
			
			display_guess_matrix(guess_no, word_length, scores)
			
			for y in range(GUESS_INDEX_TUPLE[worldlen_to_tuple_dictionary.get(word_length)][guess_no - 1][0], GUESS_INDEX_TUPLE[worldlen_to_tuple_dictionary.get(word_length)][guess_no - 1][1] + 1):
			
				allowed_guess_length += 1

			while True:
				
				string = ""

				if guess_no == word_length:
					string = "Now enter your final guess. i.e. guess the whole word: "
				else:
					string = "Now enter Guess {}: ".format(guess_no)
				player_guess = input(string)
				if len(player_guess) == allowed_guess_length:
					break
			
			temp_score = compute_value_for_guess(game_word, GUESS_INDEX_TUPLE[worldlen_to_tuple_dictionary.get(word_length)][guess_no - 1][0], GUESS_INDEX_TUPLE[worldlen_to_tuple_dictionary.get(word_length)][guess_no - 1][1], player_guess)
			scores += (temp_score,)
			has_gotten_score[guess_no - 1] = True
			guess_no += 1

		if player_guess == game_word:
			print("You have guessed the word correctly. Congratulations.")
		else:
			print('Your guess was wrong. The correct word was "{}"'.format(game_word))
	

#Winston was here 03/09/2020

		
	
			

		



if __name__ == "__main__":
	main()
