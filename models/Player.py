from .constances import HAND_LIMIT, NUMBER_CARDS_FOR_CURE

class Player:

	def __init__(self):
		self.name = input('player name: ')
		self.cards = []
		self.location = 'Atlanta'
		self.actions = {'discover_cure' : self.discover_cure, 
		   				'share_knowlege' : self.share_knowlege,
				   		'treat_disease' : self.treat_disease,
				   		'build_a_research_station' : self.build_a_research_station}

	def __str__(self):
		cards = "\n".join([str(i) + ')' + card['name'] for i, card in enumerate(self.cards)])
		return f'''{self.name} in {self.location} \nholds:\n{cards}'''

	def do_action(self, cities):
		my_action = self.choose_actions()
		self.actions[my_action](cities)
		print(f'Player {self.name} did an action!')

	
	def choose_actions(self): 
		actions = [action_name for action_name in self.actions.keys()]
		action_num = input(''.join([f'{i}) {action_name} \n' for i, action_name in enumerate(actions)]))
		if action_num.isnumeric():
			action_num = int(action_num)
			if action_num >= 0 and action_num < len(actions):
				return actions[action_num]

		print('not a valid action')
		return self.choose_actions()

	def discover_cure(self, cities):
		print('discover_cure')
		print(self.cards)
		if len(self.cards) > NUMBER_CARDS_FOR_CURE:
			cards_for_cure = self.choose_cards(NUMBER_CARDS_FOR_CURE)
			
			print(self.location)
			print(cards_for_cure, '\n', self.cards)

		else:
			print('not enugh cards')
			self.choose_actions()

	def choose_cards(self, num_of_cards):
		chosen_cards = []
		while num_of_cards > 0:
			self.display_cards()
			card_num = self.choose_a_card()
			chosen_cards.append(self.cards.pop(card_num))
			num_of_cards -= 1
	
		return chosen_cards


	def share_knowlege(self, cities):
   		print('share_knowlege')

	def treat_disease(self, cities):
   		print('treat_disease')

	def build_a_research_station(self, cities):
   		print('build_a_research_station')


	def discard(self):
		discard_pile_temp = []
		while len(self.cards) > HAND_LIMIT:
			self.display_cards()
			card_num = self.choose_a_card()
			discard_pile_temp.append(self.cards.pop(card_num))

		return discard_pile_temp

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
