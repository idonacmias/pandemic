class Player:

	def __init__(self, cards):
		self.name = input('player name: ')
		self.cards = cards
		self.location = 'Atlanta'
	
	def __str__(self):
		return f'''{self.name} in {self.location} \n holds {self.cards}'''