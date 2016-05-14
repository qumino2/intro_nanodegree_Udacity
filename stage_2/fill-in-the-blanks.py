# sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
# adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
# don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
# tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
#0. If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/
paragraph_easy = "The __1__ is a bunch of computers that communicate\n\
with each other. When writing HTML, we tell __2__s the type\n\
of each __3__ by using HTML __4__s."
answers_easy =["web", "browser", "element", "tag"]
blanks_easy = ["__1__", "__2__", "__3__", "__4__"]

paragraph_medium = "__1__ stands for __2__ Style Sheets and they give __3__s a way\n\
to control the __4__ of related HTML elements. This is done by giving\n\
similar __5__ elements the same __6__ name and then specifying\n\
the style that should apply to that class."
answers_medium = ["CSS", "Cascading", "programmer", "style", "HTML", "class"]
blanks_medium = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__"]

paragraph_hard = "HTML elements are either __1__ or __2__.\n\
When writing __3__, programmers use special text __4__s.\n\
For example, some text editors will automatically generate\n\
a __5__ HTML tag when you write an __6__ tag.\n\
When programmers don't avoid __7__,\n\
they will often have to do the __8__ thing over and over." 
answers_hard = ["inline", "block", "code", "editor", "closing", "opening", "repetition", "same"]
blanks_hard = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__", "__8__"]


def user_choose_level():
	level_choice = raw_input("Please select a game difficulty by typing it in!\n\
Possible choices include easy, medium, and hard.\n")
	if level_choice.lower() == "easy":
		print "You've chosen easy!\n\nYou will get 5 guesses per problem\n"
		return user_guess_word(paragraph_easy, answers_easy, blanks_easy)
		
	elif level_choice.lower() == "medium":
		print "You've chosen medium!\n\nYou will get 5 guesses per problem\n"
		return user_guess_word(paragraph_medium, answers_medium, blanks_medium)
		
	elif level_choice.lower() == "hard":
		print "You've chosen hard!\n\nYou will get 5 guesses per problem\n"
		return user_guess_word(paragraph_hard, answers_hard, blanks_hard)

	else:
		print "That's not an option!"
		user_choose_level()
	

def user_guess_word(paragraph, answers, blanks):
	
	i = 0 #index of blanks
	j = 5 #number of trys left
	while i < len(blanks):

		guess = raw_input(paragraph + "\n\n\n" + "What should be substituted in for " + blanks[i] + "?")
		if guess.lower() == answers[i].lower():
			paragraph = paragraph.replace(blanks[i], answers[i])
			i += 1
			print "\nCorrect!\n"
			if i == len(blanks):
				print paragraph + "\n\nYou won!\n"

		else:
			j -= 1
			if j > 0:
				print "That isn't the correct answer! Let's try again; you have " + str(j) + " trys left!\n" 
			else:
				print "You've failed too many straight guesses!  Game over!"
				break


user_choose_level()

