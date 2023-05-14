from random import shuffle, randrange 

from models.Cities import Cities
from models.Player import Player

class Bord:
	def __init__(self,cities, num_player, difficulty):
		difficulty += 4
		self.infaction_rate = 2
		self.outbreack = 0
		self.research_stations_cuonter = 6
		self.research_stations_location = ["Atlanta"]
		self.cure_blue = 0
		self.cure_red = 0
		self.cure_yellow = 0
		self.cure_black = 0
		self.disease_cudes_blue = 24
		self.disease_cudes_red = 24
		self.disease_cudes_yellow = 24
		self.disease_cudes_black = 24
		self.cities = cities
		self.infaction_deck = Bord._generate_infaction_deck(self.cities)
		self.discard_infaction_deck = []
		self.cure_deck = Bord._generate_cure_deck(cities)
		self.discard_cure_deck = []
		self.players = [Player() for _ in range(num_player)]
		self._deal_first_ruond_cards(num_player)
		self._insert_epidemic(difficulty)


	def __str__(self):
		my_str =[]
		for player in self.players:
			my_str.append(player)
		my_str.append(self.cure_deck)
		my_str.append(self.infaction_deck)
		# my_str.append(self.cities[self.infaction_deck[0]])
		string = str(my_str)
		return string

	@staticmethod
	def _generate_infaction_deck(cities):
		infaction_deck = [city for city in cities]
		shuffle(infaction_deck)
		return infaction_deck
	
	@staticmethod
	def _generate_cure_deck(cities):
		cure_deck = [Bord._create_cure_card(card) for card in cities.values()]
		shuffle(cure_deck)
		return cure_deck

	@staticmethod
	def _create_cure_card(card):
		return {'name' : card.name, 'color' : card.color, 'population' : card.population}

	def _deal_first_ruond_cards(self, num_player):
		num_cards_for_player = [4, 3, 2][num_player - 2]
		for player in self.players:
			player.cards = player.cards + self.give_player_cards(num_cards_for_player)

	def give_player_cards(self, num_cards_for_player):
		cards = self.cure_deck[:num_cards_for_player]
		del self.cure_deck[:num_cards_for_player]
		return cards

	def _insert_epidemic(self, difficulty):
		split_deack = int(len(self.cure_deck) / difficulty)
		for i in range(difficulty):
			position = randrange(split_deack) + (i * split_deack) 
			self.cure_deck.insert(position, "epidemic")

	def handel_epidemic(self):
		print('Bord handel_epidemic')
		pass

	def infect_cities(self):
		print('Bord infect cities')
		infected_cities = self.infaction_deck[:self.infaction_rate]
		for city_name in infected_cities:
			city = self.cities[city_name]
			print(city.color)
			
