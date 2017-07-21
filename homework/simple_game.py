import random

user_name = input("What's your name ? ")
print("Hello, {}".format(user_name))
print("""There are 3 levels of game and 3 questions in each level.For every correct answer player gets 1 point
and 0 for incorrect answer.If none of 3 answers is correct in any level the player will be prefered to
REPLAY that level.If one or more correct answers in the some are made, the player is prefered to the 
next level.The max level is 3.
""")
print("Let's strart the game")

question_answer_list = [{('15+29') : 44, ('274+31') : 305, ('93-45') : 48, ('524-115') : 409, ('11+12') : 23, ('12+13') : 25, ('13+14') : 27, ('14+15') : 29}, {('2087+4478') : 6565, ('212+9063') : 9275, ('8437-2978') : 5459, ('6218-3829') : 2389},
						{('91+22*47') : 1125, ('(732-597)/5') : 27, ('100/4+50*2') : 125, ('250*4/50') : 20}]

counter = 0			# counter of quantity questions in each level (3 questions)
score = 0			# summary of quantity correct answers
temp_score = 0		# be used to define if none answer of 3 questions in some level is correct
attempt = "y"		# quantity of attempts of game . Max. attempt is 3.
level = 1			# gam is begun at the level 1


def random_question_and_correct_answer():
	""" Random choice of questions and correct answer """

	keys_list = list(question_answer_list[level -1].keys())
	random_question_number = random.choice(keys_list)
	print("How many is : ", random_question_number)
	return question_answer_list[level - 1 ][random_question_number]

def compare_answers(correct_answer):
	""" Check the user answer with the correct answer"""
	global counter
	global score
	global attempt
	global level
	global temp_score

	if user_answer == correct_answer:
		score += 1
		print("Your answer is right and your score is : ", score)
	else:
		print("You are wrong ! Pl. try to answer correctly the next question . Your score is : ", score)
	counter += 1


while attempt == "y":

	while counter < 3:
		correct_answer = random_question_and_correct_answer()
		user_answer = int(input())
		compare_answers(correct_answer)

	else:
		if score == temp_score:		# condition when player answer incorrect all of 3 questions in some level
			attempt = input("None of 3 your answers is correct. Do you want to replay this level ? (y or n) ")
			if attempt == "y":
				counter = 0
				print("You will play in level :", level)
			if attempt == "n":
				break

		if score > temp_score:
			temp_score = score

			if level == 3:
				print("You have reached 3 attempts .Thank you for game !")
				exit()
			else:
				attempt = input("Do you want to play more ? (y or n)")
				if attempt == "y":
					counter = 0
					level += 1
					print("You will play in level :", level)
				if attempt == "n":
					break

