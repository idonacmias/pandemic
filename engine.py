from models.constances import PLAYER_ACTIONS_PER_TURN, MAX_OUTBREACK

def run_game(bord):
	player_cunter = 0
	num_player = len(bord.players)
	while game_status(bord) == 2:
		corent_player = bord.players[player_cunter]
		print(f'corent_player: {corent_player.name}')
		for _ in range(PLAYER_ACTIONS_PER_TURN):
			corent_player.do_action()
		
		new_cure_cards = bord.give_player_cards(2)
		chack_epidemic(bord, new_cure_cards)
		corent_player.cards = corent_player.cards + new_cure_cards
		hande_limt(bord, corent_player)
		bord.infect_cities()
		player_cunter = switch_player(num_player, player_cunter)
		input('next turn')

def game_status(bord):
	if is_disease_cudes_left(bord) or bord.outbreack >= MAX_OUTBREACK or len(bord.cure_deck) < 0:
		print('you lose!')
		return 0

	if is_four_vaccines_found(bord):
		print('you won!')
		return 1

	return 2

def is_disease_cudes_left(bord):
	return bord.disease_cudes_blue <= 0 and bord.disease_cudes_red <= 0 and bord.disease_cudes_yellow <= 0 and bord.disease_cudes_black <= 0

def is_four_vaccines_found(bord):
	return bord.cure_blue > 0 and bord.cure_red > 0 and bord.cure_yellow > 0 and bord.cure_black > 0

def chack_epidemic(bord, new_cure_cards, secend=False):
	if 'epidemic' in new_cure_cards:
		new_cure_cards.remove('epidemic')
		bord.handel_epidemic()
		bord.discard_cure_deck.append('epidemic')
		chack_epidemic(bord, new_cure_cards, secend=True)

	return new_cure_cards 		

def hande_limt(bord, corent_player):
	discard_pile_temp = corent_player.discard()
	bord.discard_cure_deck += discard_pile_temp

def switch_player(num_player, player_cunter):
	if player_cunter == num_player - 1:
		player_cunter = 0
	
	else:
		player_cunter += 1
	
	return player_cunter		
