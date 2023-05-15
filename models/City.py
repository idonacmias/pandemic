import json
from dataclasses import dataclass, field

from models.Color import Color

@dataclass
class City:
    name : str
    color : str
    population : int 
    roads : list
    disease_cube_red : int = 0
    disease_cube_blue : int = 0
    disease_cube_yellow : int = 0
    disease_cube_black : int = 0

    def __post_init__(self):
        self.color = Color(self.color)


    def __str__(self):
        return f'{self.name} , {self.color}'

with open("models/cities.json", "r") as json_file:
    cities = json.load(json_file)

cities = {city["name"] : City(**city) for city in cities}

# print(type(cities['Hong Kong'].color))
# print(cities['Hong Kong'].color)
# print(cities['Hong Kong'])
