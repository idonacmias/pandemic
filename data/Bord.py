class Bord:
	def __init__(self, num_player):
		self.infaction_rate = 2
		self.outbreack = 0
		self.cure_blue = 0
		self.cure_red = 0
		self.cure_yellow = 0
		self.cure_black = 0
		self.infaction_card = Bord.get_infaction_card()
		self.cure_card = Bord.get_cure_card()
		self.player = Bord.get_player(num_player)

	@staticmethod
	def get_infaction_card():
		pass

	@staticmethod
	def get_cure_card():
		pass 

	@staticmethod
	def get_player(num_player):
		pass


def main(bord):
	print(bord)



