from sys import exit
# IPND Stage 2 Final Project
#This is a fill in the blanks Ninja Turtle game
#refrence for easy_question here. https://en.wikipedia.org/wiki/Teenage_Mutant_Ninja_Turtles
easy_question =   '''
The Ninja Turtles were named after four renaissance Italian artists. Can you guess their names?
___1___ is the scientist, inventor, engineer, and technological genius. He wears a purple mask and has a bo staff.
___2___ is the tactical, courageous leader and devoted student sensei Splinter. He wears a blue mask and has two katana.
___3___ is a free-spirited, relaxed, and often goofey jokester, and known for his love of pizza.
He wears an orange mask and has a pair of nunchucks.
___4___ is the teams bad boy, he is very strong and he has a chip on the front of his shell. He wears a red mask and has a pair of sai.'''

#refrence for madium_question http://screenrant.com/teenage-mutant-ninja-turtles-tmnt-best-worst-villains/?view=all
medium_question = '''
The Ninja Turtles have to fight many differnet bad guys. Can you guess some of their names?
 __1__This bad guy likes to say, "Tonight I dine on turtle soup." He is the leader of the foot clan.
 __2__ is a genius scientist who turned himself into a fly.
 __3__ is a brain-like creature who uses a robot body to get around. He is also a General from Dimension X
 Using the DNA of a warthog and a rhino, Shredder uses mutagen to create __4__.
 __5__ is a feared ninja warrior of the foot clan. She is the long-lost daughter of Splinter.'''

# refrence for hard_question http://teenage-mutant-ninja-turtles-2012-series.wikia.com/wiki/TMNT_(2012_TV_Series)_Wiki
hard_question = '''
I hope you trained like a Ninja and ate enough pizza becuase these questions are hard.
Professor Honeycutt refused to build a transmat device for General Blanque of the federation military
in their war against the Triceraton Republic. He was categorized as a __1__ (short for fugitive android.)
__2__ is second in command of the foot clan. Formerly know as Takeshi, he is a mutant Bengal Tiger from Japan.
__3__ is a bounty hunter and space assasian hired to hunt down the turtles in Dimension X.
__4__ is the ruler of Sectoid 1 and ruler of all insect life in the universe.
__5__ is a mutant bat that is the only living member of an alien species from the Dimension X planet Dexion V.
__6__ is a mutant gray wolf employed by shredder to fight the turtles. He was abducted from the bronx zoo by the foot clan.
 '''

easy_answer = [
("1","donnie"),
("2", "leo"),
("3","mikey"),
("4","raph")
]
medium_answer = [
("1","shredder"),
("2","baxter stockmen"),
("3","krang"),
("4","bebop and rocksteady"),
("5", "karai")
]
hard_answer = [
("1", "fugitoid"),
("2", "tiger claw"),
("3", "armaggon"),
("4", "lord dregg"),
("5", "wingnut"),
("6", "rahzar")
]

# gets name from user
print "Hi! before we start, what's your name?"
name = raw_input("> ")
# ask the user if they want to play.
def want_to_play():
	game_answer = ["yes", "no"]
	print "ok %s, do you want to play a game about Ninja Turtles? \"Yes\" or \"No\"" % name
	game = raw_input("> ")
	if game.lower() != game_answer[0]:
		print "no problem %s, we can play next time." % name
		exit(0)
	else:
		print "Great!!"
		return how_many_tries()

# ask the user to choose a level
def choose_level(guess):
	game_levels = ["easy", "medium", "hard"]
	levels = raw_input("Please select a level from \"easy\", \"medium\", or \"hard\": ")
	while levels.lower() not in game_levels:
		print "that's not an option, please select between \"easy\", \"medium\" , \"hard\"."
		return choose_level(guess)
	else:
		eval_function(guess, levels)

# ask the user how many tries they want
def how_many_tries():
    	print "How many tries would you like %s?" % name
    	guess = raw_input("> ")
    	tries = 0
    	max_trys = ["1","2","3","4","5"]
    	while guess not in max_trys:
    		print "sorry %s, that's not an option. please select between 1-5 tries." % name
    		return how_many_tries()
    	if tries <= max_trys:
    		return choose_level(guess)

# makes sure the users input matches answers
def correct_answer(replacement, result, new_question, guess ):
	guess = int(guess)
	tries = 1
	while tries <= guess:
		user_input = raw_input("What's the answer to number: " + replacement + " ")
		if result == user_input.lower():
			print ""
			print "BOOYAKASHA!! good job %s!" % name
			new_question = new_question.replace(replacement, result)
			print new_question
			return new_question
		else:
			if tries < guess:
				print "Total bummer %s, Thats not right, try again dude." % name
				print "you have "+ str(guess - tries) + " tries left."
			else:
				print ""
				print "Sorry %s, you have no more tries left. The right answer was: " % name + result + "."+" Train like a ninja and try again."
				exit(0)
			tries +=1

#prints the right question with the right answer key
def eval_function(guess, station):
	question_paragraph = eval(station + "_question")
	answers = eval(station + "_answer")
	print question_paragraph
	word_in_pos(question_paragraph, answers, guess)

#keeps score, takes user_input & calls on correct_answer function
def word_in_pos(question_paragraph, results, guess):
	score = 0
	new_question = question_paragraph
	for replacement,result in results:
		score += 1
		replaced_question = correct_answer(replacement, result, new_question, guess)
    	if score == len(result):
       		print ""
       		print "WOW!! Amazing job %s! You got all %d questions right. Are you sure you're not a ninja turtle?" % (name, score)
       		print ""
       		exit(0)



print want_to_play()





