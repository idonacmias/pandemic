from .constances import HAND_LIMIT, NUMBER_CARDS_FOR_CURE

class Player:

	def __init__(self):
		self.name = input('player name: ')
		self.cards = []
		self.location = ''

	def __str__(self):
		cards = "\n".join([str(i) + ')' + card['name'] for i, card in enumerate(self.cards)])
		return f'''{self.name} in {self.location.name} \nholds:\n{cards}'''

	def discover_cure(self):
		print('discover_cure')

		if not self.location.resarch_station:
			print('not in reserch stetion')
			return None

		elif len(self.cards) < NUMBER_CARDS_FOR_CURE:
			print('not enugh cards')
			return None

		elif not self.is_enugh_same_coler_cards():
			print('not enugh cards of the same color')
			return None

		else:
			print('start cure discaver')
			cards_for_cure = self.choose_cards(NUMBER_CARDS_FOR_CURE)
			cards_colors = [card['color'] for card in cards_for_cure]
			if len(set(cards_colors)) != 1:
				self.cards += cards_for_cure
				print('cards are not the same color')
				return None
			
			else:
				print(f'cure discoverd for {cards_colors[0]}')
				return cards_colors[0]

	def is_enugh_same_coler_cards(self):
		color_cards = [card['color'] for card in self.cards]
		for color in color_cards:
			if(color_cards.count(color) >= NUMBER_CARDS_FOR_CURE):
				return True
		
		return False


	def share_knowlege(self):
   		print('share_knowlege')

	def treat_disease(self):
   		print('treat_disease')

	def build_a_research_station(self):
   		print('build_a_research_station')


	def discard(self):
		discard_pile_temp = []
		while len(self.cards) > HAND_LIMIT:
			self.display_cards()
			card_num = self.choose_a_card()
			discard_pile_temp.append(self.cards.pop(card_num))

		return discard_pile_temp

	def choose_cards(self, num_of_cards):
		chosen_cards = []
		while num_of_cards > 0:
			card_num = self.choose_a_card()
			chosen_cards.append(self.cards.pop(card_num))
			num_of_cards -= 1
	
		return chosen_cards

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

	def display_cards(self):
		print(''.join([f"{i}) {card['name']}: {card['color'].value} \n" for i, card in enumerate(self.cards)]))
