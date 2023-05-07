import json
from dataclasses import dataclass, field

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


    def __str__(self):
        return f'{self.name} , {self.color}'

json_file = open("models/cities.json", "r")
cities = json.load(json_file)
json_file.close()

cities = {city["name"] : City(**city) for city in cities}
