from random import shuffle 

from models.Cities import Cities


class InfectionDeck:
	def __init__(self, cities):
		self.infection_rate = [2, 2, 2, 3, 3 ,4 ,4]
		self.infection_cunter = 0
		self.deck = InfectionDeck._generate_infection_deck(cities)
		self.discard = []

	def __str__(self):
		string = "\n".join([str(i) + ')' + str(card) for i, card in enumerate(self.deck)])
		return string

	@staticmethod
	def _generate_infection_deck(cities):
		infection_deck = [city for city in cities]
		shuffle(infection_deck)
		return infection_deck

	def draw_cards(self):
		print('InfectionDeck draw cards')
		rate = self.infection_rate[self.infection_cunter]
		self.deck, cards = self.deck[rate:], self.deck[:rate]
		self.discard += cards
		return cards

	def handel_epidemic(self):
		print('handel_epidemic')
		self.infection_cunter += 1
		infected_city = self.deck.pop(-1)
		self.discard.append(infected_city)
		shuffle(self.discard) 
		self.deck = self.discard + self.deck
		self.discard = []
		return infected_city