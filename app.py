from models.Bord import Bord
from models.City import cities

import engine

# def run_game(bord):
# 	while game_status(bord) == 2:
# 		pass


# def game_status(bord):
# 	if is_disease_cudes_left(bord) or bord.outbreack >= 8 or len(bord.cure_deck) < 0:
# 		print('you lose!')
# 		return 0

# 	if is_four_vaccines_found(bord):
# 		print('you won!')
# 		return 1

# 	return 2

# def is_disease_cudes_left(bord):
# 	return bord.disease_cudes_blue <= 0 and bord.disease_cudes_red <= 0 and bord.disease_cudes_yellow <= 0 and bord.disease_cudes_black <= 0

# def is_four_vaccines_found(bord):
# 	return bord.cure_blue > 0 and bord.cure_red > 0 and bord.cure_yellow > 0 and bord.cure_black > 0


if __name__ == '__main__':
	# cities=Cities()
	# print(cities)
	bord = Bord(cities=cities, num_player=2, difficulty=0)
	engine.run_game(bord)

