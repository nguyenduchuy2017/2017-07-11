import re


num_of_rows = ''


def num_of_rows_check():

	global num_of_rows

	while True:
		try:
			num_of_rows = int(input('Enter the quantity of rows(colums) :'))

			if num_of_rows > 0:
				break
			if num_of_rows <= 0:
				print("This number is negative. Enter the number >0 ; ")

		except ValueError:
			print('That \'s not a number. Pl., Enter the number >0 : ')
	return num_of_rows


def game_board_init(num_of_rows):

	print()

	for x in range(num_of_rows):

		for y in range(num_of_rows):
			GBC[x, y] = ' '

			if (y+1) % num_of_rows == 0:
				print('!' + GBC.get((x, y)) + ' !')
			else:
				print('!', GBC.get((x, y)), end='')

	print()


def game_board_update(num_of_rows):

	for x in range(num_of_rows):
		for y in range(num_of_rows):

			if (y+1) % num_of_rows == 0:
				print('! ' + GBC.get((x, y)) + '!')
			else:
				print('!', GBC.get((x, y)), end='')


def player_name_check(player_name):

	while True:

		name_check = re.findall(r'^[a-zA-Z][a-zA-Z0-9-_ \.]{1,20}$', player_name)

		if name_check:
			break
		else:
			player_name = input('Incorrect username ! Pl., Enter correct username: ')

	return player_name


def coord_num_check():

	num = int(input())

	while True:

		if num < num_of_rows and num >= 0:

			break

		else:
			print("Incorrect number ! Enter the coord ", num_of_rows, "> coord >=0 ; ", )
			num = int(input())

	return num


def repeat_game():

	global ways_counter

	ways_counter = 0

	while True:
		
		if repeat_play == 'y':
			game_board_init(num_of_rows)
			player_1_way()
		elif repeat_play == 'n':
			print('The game is over !')
			exit()


def player1_way_check(x, y):

	while GBC[(x, y)] is not ' ':
		print('Incorrect ! Please, enter correct coord : ')
		player_1_way()


def player2_way_check(x, y):

	while GBC[(x, y)] is not ' ':
		print('Incorrect ! Please, enter correct coord : ')
		player_2_way()

def result_check(counter, player):

	global repeat_play

	if counter == num_of_rows:
		print(player, " , You are winner !!!")
		repeat_play = input('Do you want to play again ? ("y" or "n") ')
		repeat_game()

def check_for_winner():

	counter_5 = counter_6 = counter_7 = counter_8 = 0

	for x in range(num_of_rows):
		counter_1 = counter_2 = counter_3 = counter_4 = 0

		for y in range(num_of_rows):

			if GBC[(x, y)] == 'X':
				counter_1 += 1
				result_check(counter_1, player_1)

			elif GBC[(x, y)] == 'O':
				counter_2 += 1
				result_check(counter_2, player_2)

			if GBC[(y, x)] == 'X':
				counter_3 += 1
				result_check(counter_3, player_1)

			elif GBC[(y, x)] == 'O':
				counter_4 += 1
				result_check(counter_4, player_2)

			if x == y and GBC[(x, y)] == 'X':
				counter_5 += 1
				result_check(counter_5, player_1)

			elif x == y and GBC[(x, y)] == 'O':
				counter_6 += 1
				result_check(counter_6, player_1)

			if (y == num_of_rows - 1 - x) and GBC[(x, y)] == 'X':
				counter_7 += 1
				result_check(counter_7, player_1)

			elif (y == num_of_rows - 1 - x) and GBC[(x, y)] == '0':
				counter_8 += 1
				result_check(counter_8, player_1)


def player_1_way():

	global ways_counter
	global num_of_rows
	global player_1

	print(player_1, ' please, enter coord X ( 0 =< X < ', num_of_rows, ') : ')
	player1_x = coord_num_check()

	print(player_1, ' please, enter coord Y ( 0 =< Y < ', num_of_rows, ') : ')
	player1_y = coord_num_check()


	player1_way_check(player1_x, player1_y)
	GBC[(player1_x, player1_y)] = 'X'
	game_board_update(num_of_rows)
	ways_counter += 1
	check_for_winner()

	if ways_counter == max_number_way:
		repeat_play = input('You are draw ! Do you want to play again ? ("y" or "n") ')
		repeat_game()

	player_2_way()


def player_2_way():

	global ways_counter
	global num_of_rows
	global player_2

	print(player_2, ' please, enter coord X ( 0 =< X < ', num_of_rows, ') : ')
	player2_x = coord_num_check()

	print(player_2, ' please, enter coord Y ( 0 =< Y < ', num_of_rows, ') : ')
	player2_y = coord_num_check()

	player2_way_check(player2_x, player2_y)
	GBC[(player2_x, player2_y)] = 'O'
	game_board_update(num_of_rows)
	check_for_winner()
	ways_counter += 1
	check_for_winner()

	if ways_counter == max_number_way:
		repeat_play = input('You are draw ! Do you want to play again ? ("y" or "n") ')
		repeat_game()

	player_1_way()



num_of_rows = num_of_rows_check()

player_1 = input('Player 1, Please, enter your name: ')
player_1 = player_name_check(player_1)
player_2 = input('Player 2, Please, enter your name: ')
player_2 = player_name_check(player_2)
GBC = game_board_coord = {}
max_number_way = num_of_rows**2
ways_counter = 0

game_board_init(num_of_rows)
player_1_way()
