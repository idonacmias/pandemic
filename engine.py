
def run_game(bord):
	# print(bord)
	player_cunter = 0
	while game_status(bord) == 2:
		corent_player = bord.players[player_cunter]
		print(f'corent_player: {corent_player.name}')
		for _ in range(4):
			corent_player.action()
		
		new_cure_cards = bord.give_player_cards(2)
		epidemic_this_turn = 0
		for i, card in enumerate(new_cure_cards):
			if card == 'epidemic':
				epidemic_this_turn += 1
				new_cure_cards.pop(i)
				bord.handel_epidemic()
				bord.discard_cure_deck.append('epidemic')

		corent_player.cards = corent_player.cards + new_cure_cards
		hande_limt(bord, corent_player)
		bord.infect_cities()
		input('next turn')

def game_status(bord):
	if is_disease_cudes_left(bord) or bord.outbreack >= 8 or len(bord.cure_deck) < 0:
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

def hande_limt(bord, corent_player)
	if len(corent_player.cards) > 7:
		print(bord.discard_cure_deck)
		discard_temp = corent_player.discard()
		bord.discard_cure_deck += discard_temp
		print(bord.discard_cure_deck)
