class Player:

	def __init__(self):
		self.name = input('player name: ')
		self.cards = []
		self.location = 'Atlanta'
	
	def __str__(self):
		return f'''{self.name} in {self.location} \n holds {self.cards}'''

	def display_cards(self):
		print(''.join([f"{i}) {card['name']}: {card['color']} \n" for i, card in enumerate(self.cards)]))

	def action(self):
		print(f'Player {self.name} do an action!')

	def discard(self):
		discard = []
		self.display_cards()
		for _ in range(len(self.cards) - 7):
			card_num = self.choose_a_card()
			discard.append(self.cards.pop(card_num))

		return discard

	def choose_a_card(self):
		print('choose a card:')
		self.display_cards()
		card_num = input('card number: ')
		if card_num.isnumeric():
			card_num = int(card_num)
			if card_num >= 0 and card_num < len(self.cards):
				return card_num

		print('not a valid card')
		return self.choose_a_card()