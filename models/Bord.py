from random import shuffle, randrange 

from models.Player import Player
from models.InfectionDeck import InfectionDeck
from models.CureDeck import CureDeck
from models.constances import PLAYER_ACTIONS_PER_TURN, MAX_OUTBREACK, STARTER_CARDS, CURE_CARDS_PER_TURN



class Bord:
	def __init__(self, cities, num_player, difficulty):
		self.infaction_rate = 2
		self.outbreack = 0
		self.research_stations_cuonter = 6
		self.research_stations_location = ["Atlanta"]
		self.cure = [0] * 4
		self.disease_pool = [24] * 4
		self.players = [Player() for _ in range(num_player)]
		for player in self.players:
			player.location = cities['Atlanta']
		self.corent_player = self.players[0]
		self.cities = cities
		self.infection_deck = InfectionDeck(cities)
		self.cure_deck = CureDeck(cities, num_player, difficulty, self.players)
		self.player_actions = {'discover_cure' : self.discover_cure, 
				   			   'share_knowlege' : self.share_knowlege,
			   	    		   'treat_disease' : self.treat_disease,
				   			   'build_a_research_station' : self.build_a_research_station}
		self.action_option = [action_name for action_name in self.player_actions.keys()]

		self.run_game(num_player)

	def __str__(self):
		cities = '\n'.join([str(city) for city in self.cities])
		players = "\n\n".join([str(player) for player in self.players])
		string = f'''
cities:\n{cities} 
\ncure_deck:\n{self.cure_deck}
\ninfection_deck:\n{self.infection_deck}
\nplayers:\n{players}'''
		return string

	def run_game(self, num_player):
		print(f'bord: \n{self}')
		input()
		player_cunter = 0
		while self.game_status() == 2:
			print(f'corent_player: {self.corent_player.name}')
			self.player_do_actions()
			self.player_draw_cards()
			self.infect()
			player_cunter = self.switch_player(num_player, player_cunter)
			print(f'disease pool: {self.disease_pool}')
			input('next turn')

	def game_status(self):
		if self.is_disease_pool_full() or self.outbreack >= MAX_OUTBREACK or len(self.cure_deck.deck) < 0:
			print('you lose!')
			return 0

		if self.is_four_vaccines_found():
			print('you won!')
			return 1

		return 2

	def is_disease_pool_full(self):
		for disease in self.disease_pool:
			if disease < 1:
				print('no disease in disease pool')
				return True

	def is_four_vaccines_found(self):
		return 0 not in self.cure

	def player_do_actions(self):
		for _ in range(PLAYER_ACTIONS_PER_TURN):
			self.player_do_one_action()

	def player_do_one_action(self):
			action = self.choose_actions()
			self.player_actions[action]()

	def choose_actions(self): 
		action_num = input(''.join([f'{i}) {action_name} \n' for i, action_name in enumerate(self.action_option)]))
		if not action_num.isnumeric():
			print('expected intiger')
			return self.choose_actions()

		if int(action_num) >= len(self.action_option):
			print('action number out of range')
			return self.choose_actions()

		return self.action_option[int(action_num)]


	def discover_cure(self):
		cure_color = self.corent_player.discover_cure()
		if not cure_color:
			return self.player_do_one_action()

		if self.cure[cure_color] > 0:
			print('cure already discoverd')
			return self.player_do_one_action()

		self.cure[cure_color - 1] += 1

	def share_knowlege(self):
   		print('share_knowlege')

	def treat_disease(self):
   		print('treat_disease')

	def build_a_research_station(self):
   		print('build_a_research_station')


	def player_draw_cards(self):
			new_cure_cards = self.cure_deck.give_player_cards(CURE_CARDS_PER_TURN)
			self.chack_epidemic(new_cure_cards)
			self.corent_player.cards += new_cure_cards
			self.hande_limt()

	def chack_epidemic(self, new_cure_cards, secend=False):
		if 'epidemic' in new_cure_cards:
			new_cure_cards.remove('epidemic')
			infected_card = self.infection_deck.handel_epidemic()
			self.cities[infected_card].epidemic_infect(self.disease_pool)
			self.cure_deck.discard.append('epidemic')
			self.chack_epidemic(new_cure_cards, secend=True)

		return new_cure_cards 		

	def hande_limt(self):
		self.cure_deck.discard += self.corent_player.discard()

	def switch_player(self, num_player, player_cunter):
		print(f'player_cunter: {player_cunter}')
		player_cunter = Bord.promote_cunter(num_player, player_cunter)
		print(f'new player_cunter: {player_cunter}')
		self.corent_player = self.players[player_cunter]
		return player_cunter
	
	@staticmethod
	def promote_cunter(num_player, player_cunter):
		if player_cunter == num_player - 1:
			player_cunter = 0
		
		else:
			player_cunter += 1
		
		return player_cunter		

	def infect(self):
		print('infect')
		infected_cards = self.infection_deck.draw_cards()
		print(infected_cards)
		for infected_card in infected_cards:
			city = self.cities[infected_card]
			city.infect(self.disease_pool, city.color)
