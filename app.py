from models.Bord import Bord
from models.City import cities

import engine

if __name__ == '__main__':
	bord = Bord(cities=cities, num_player=1, difficulty=0)

