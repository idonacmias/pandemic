from models.City import City
import json
from dataclasses import dataclass


# @dataclass
class Cities:
	


	# city : City = {city['name'] : City(City) for city in cities}

	def __init__(self, cities):
		pass				
		# for city in cities:
			# self.city = City(**city)

		# print(self.city)


json_file = open("models/cities.json", "r")
cities = json.load(json_file)
json_file.close()
cities = {city["name"] : City(**city) for city in cities}
# print(cities)
cities = Cities(cities)
