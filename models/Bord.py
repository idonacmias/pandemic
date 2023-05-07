from random import shuffle, randrange 
from models.Player import Player

class Bord:
	def __init__(self, cities, num_player, difficulty):
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
		self.infaction_deck = cities
		self.temp_player_cards = []
		self.cure_deck = (num_player, difficulty)
		self.players = [Player(self.temp_player_cards[i]) for i in range(num_player)]
		del self.temp_player_cards



		# for player in self.players:
		# 	print(player)
		# print(self.cure_deck)
		# print(self.infaction_deck)
		# print(cities[self.infaction_deck[0]])

	@property
	def infaction_deck(self):
		return self._infaction_deck 
	
	@infaction_deck.setter
	def infaction_deck(self, cities):
		infaction_deck = [city for city in cities]
		shuffle(infaction_deck)
		self._infaction_deck = infaction_deck


	@property
	def cure_deck(self):
		return self._cure_deck 
	
	@cure_deck.setter
	def cure_deck(self, data):
		num_player = data[0]
		difficulty = data[1] + 4
		cure_deck = [Bord.create_cure_card(card) for card in self.cities.values()]
		shuffle(cure_deck)
		num_cards_for_player = [4, 3, 2]
		num_cards_for_player = num_cards_for_player[num_player - 2]
		for _ in range(num_player):
			self.temp_player_cards.append([cure_deck.pop(0) for _ in range(num_cards_for_player)])

		split_deack = int(len(cure_deck) / difficulty)
		for i in range(difficulty):
			position = randrange(split_deack) + (i * split_deack) 
			cure_deck.insert(position, "epidemic")

		self._cure_deck = cure_deck

	@staticmethod
	def create_cure_card(card):
		return {'name' : card.name, 'color' : card.color, 'population' : card.population}