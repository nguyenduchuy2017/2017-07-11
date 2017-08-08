import random

# карты с номиналами (par) от 1 (туз) до 10, валет ("J"), дама ("О") и король ("К"). У каждой
# карты есть также атрибут suit, представляющий масть карты. Есть 4 значения атрибута:
#     "с" (сluЬs)-трефы, "d" (diamonds)-бyбны, "h" (hcarts)- червы и, наконец, "s" (spades) - пики.


card_par = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'O', 'K']
card_suit = ['c', 'd', 'h', 's']

def card_point_list(card_par, card_suit):

	card_point_1 = [{str(par)+suit: par} for par in card_par for suit in card_suit if str(par).isdigit()]
	card_point_2 = [{str(par)+suit: 10} for par in card_par for suit in card_suit if str(par).isalpha()]
	card_point = card_point_1 + card_point_2
	# print(card_point)

	return card_point


def cards_creation():

	cards = [str(par)+suit for par in card_par for suit in card_suit]
	return cards


cards = cards_creation()
print('Cards : ', cards)
card_point = card_point_list(card_par, card_suit)
print('Card_point : ', card_point)
players_general_info = []
players_point_info = []


def banker_info_creation():

	banker_name = input('I am banker, my name is : ')
	players_point_info.append({banker_name: []})
	capital = 200
	point_total= 0
	win = 0
	lost = 0
	remain = capital + win - lost
	player_info = {banker_name: {'name': banker_name, 'capital': capital, 'point_total': point_total, 'win': win, \
								 'lost': lost, 'remain': remain}}

	players_general_info.append(player_info)
	return


def players_general_info_creation():

	for num in range(0, num_of_players):
		player_name = input('Enter your name: ')
		players_point_info.append({player_name: []})
		capital = 20
		point_total = 0
		win = 0
		lost = 0
		remain = capital + win - lost
		player_info = {player_name: {'capital': capital, 'point_total': point_total, \
									 'win': win, 'lost': lost, 'remain': remain}}

		players_general_info.append(player_info)
	return players_general_info


def card_value(card_point, card_name):

	for card_dict in card_point:
		for card in card_dict:
			if card_name == card:
				value_of_card = card_dict.get(card)
			# print(point)
	return value_of_card


def cards_distribution(player):

	print(player, ', your card(s) : ', end='')
	card = random.choice(cards)
	value_of_card = card_value(card_point, card)

	for point_dict in players_point_info:
		for name in point_dict:
			if player == name:
				point_dict[player].append(value_of_card)

	cards.remove(card)

	print(card)


num_of_players = int(input('Enter the quantity of the players : '))
players_general_info = players_general_info_creation()
banker_info_creation()

print('players_point_info : ', players_point_info)

for player_info in players_point_info:
	for player in player_info:
		cards_distribution(player)
		cards_distribution(player)


for player_info in players_point_info:

	for player in player_info:
		print(player, end="")
		answer = input (", would you want to get more card: ('y' or 'n') ")

		while answer.lower() == 'y':
			cards_distribution(player)
			print(player, end="")
			answer = input(", would you want to get more card ('y' or 'n'):")

		else:
			if answer.lower() == 'n':
				break
			else:
				print(player, end="")
				answer = input(", would you want to get more card ('y' or 'n'): ")


def player_point():

	for player_info in players_point_info:

		for player in player_info:

			if players_point_info.index(player_info) == len(players_point_info) - 1:
				banker_point_total = sum(player_info[player])
				print('banker_point_total :', banker_point_total)

	for player_info in players_point_info:

		for player in player_info:

			if 1 not in player_info[player]:
				print(player, sum(player_info[player]))

				if sum(player_info[player]) == banker_point_total or banker_point_total and sum(player_info[player]) > 21:
					print(player , " and banker are draw !")
				elif sum(player_info[player]) < banker_point_total:
					print(player , " lost by  banker !")
					#
					# for element in players_general_info:
					# 	print(element.get(player))
							# .get('lost') += 1
						# element.get(player).get('remain') -= 1

				else:
					print(player , " wins  banker !")
			else:
				if sum(player_info[player]) <= 11:
					special_point_total = sum(player_info[player]) + 10
					print(player, special_point_total)
				else:
					print(player, sum(player_info[player]))
	return


print('players_general_info : ', players_general_info)

print('players_point_info ', players_point_info)
player_point()
print('players_general_info : ', players_general_info)


