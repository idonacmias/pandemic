import json
from dataclasses import dataclass, field

from models.Color import Color
from models.constances import MAX_CUBE_IN_CITY

@dataclass
class City:
    name : str
    color : str
    population : int 
    roads : list
    disease_cubes : list = field(default_factory=lambda: [0]*4)
    outbreack_bool = False

    def __post_init__(self):
        self.color = Color[self.color]

    def __str__(self):
        return f'{self.name} , {self.color} \n {self.disease_cubes}'

    def infect(self, cities, disease_pool, color=0):
        if color == 0:
            color = self.color
        
        if self.disease_cubes[color - 1] < MAX_CUBE_IN_CITY:
            self.disease_cubes[color - 1] += 1
            disease_pool[color - 1] -= 1

        else:
            self.outbreack(cities, disease_pool)
        
        print(self)

    def outbreack(self, cities, disease_pool):
        self.outbreack_bool = True
        print(f'{self.name} is outbreacking')
        print(f'disses spred to {self.roads}')
        for city_name in self.roads:
            city = cities[city_name]
            if not city.outbreack_bool: 
                city.infect(cities, disease_pool, self.color)

    def epidemic_infect(self, cities, disease_pool):
        city_disease = self.disease_cubes[self.color.value - 1]
        if city_disease + 3 > MAX_CUBE_IN_CITY:
            print('epidemic_infect!!!!!!!!!!!!')
            self.outbreack(cities, disease_pool)

        disease_pool[self.color.value - 1] -= city_disease - MAX_CUBE_IN_CITY
        city_disease = 3

with open("models/cities.json", "r") as json_file:
    cities = json.load(json_file)

cities = {city["name"] : City(**city) for city in cities}

