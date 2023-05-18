from random import shuffle, randrange 

# from models.Cities import Cities
from models.Player import Player
from models.InfectionDeck import InfectionDeck
from models.constances import STARTER_CARDS

class CureDeck:
	def __init__(self,cities, num_player, difficulty, players):
		difficulty += 4
		self.deck = CureDeck._generate_deck(cities)
		self.deal_first_ruond_cards(num_player, players)
		self._insert_epidemic(difficulty)
		self.discard = []

	def __str__(self):
		string = "\n".join([''.join(name for name in card.values()) for i, card in enumerate(self.deck)])
		return string

	@staticmethod
	def _generate_deck(cities):
		deck = [CureDeck._create_cure_card(city) for city in cities.values()]
		shuffle(deck)
		return deck

	@staticmethod
	def _create_cure_card(city):
		return {'name' : city.name, 'color' : city.color, 'population' : city.population}

	def deal_first_ruond_cards(self, num_player, players):
		num_cards = STARTER_CARDS[num_player - 2]
		for player in players:
			player.cards = self.give_player_cards(num_cards) 
		
	def give_player_cards(self, num_cards):
		self.deck, cards = self.deck[num_cards:], self.deck[:num_cards]
		return cards

	def _insert_epidemic(self, difficulty):
		split_deack = len(self.deck) // difficulty
		for i in range(difficulty):
			position = randrange(split_deack) + (i * split_deack) 
			self.deck.insert(position, "epidemic")



