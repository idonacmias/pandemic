from .constances import HAND_LIMIT
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
		return f'''{self.name} in {self.location} \n holds {self.cards}'''

	def do_action(self):
		my_action = self.choose_actions()
		self.actions[my_action]()
		print(f'Player {self.name} do an action!')

	
	def choose_actions(self): 
		actions = [action_name for action_name in self.actions.keys()]
		action_num = input(''.join([f'{i}) {action_name} \n' for i, action_name in enumerate(actions)]))
		if action_num.isnumeric():
			action_num = int(action_num)
			if action_num >= 0 and action_num < len(actions):
				return actions[action_num]

		print('not a valid action')
		return self.choose_actions()

	def discover_cure(self):
		print('discover_cure')

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
