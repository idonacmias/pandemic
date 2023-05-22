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

    def infect(self, color=0):
        if color == 0:
            color = self.color
        
        if self.disease_cubes[color.value - 1] < MAX_CUBE_IN_CITY:
            self.disease_cubes[color.value - 1] += 1

        else:
            self.outbreack_bool = True
            # self.outbreack()
            return 'outbreack'
        
        print(self)

    # def outbreack(self):
    #     self.outbreack_bool = True
    #     for city in self.roads:
    #         if not city.outbreack_bool: 
    #             city.infect(self.color)

    def epidemic_infect(self):
        if self.disease_cubes[self.color.value - 1] > 0:
            print('epidemic_infect!!!!!!!!!!!!')
            self.outbreack()

        self.disease_cubes[self.color.value - 1] = 3

with open("models/cities.json", "r") as json_file:
    cities = json.load(json_file)

cities = {city["name"] : City(**city) for city in cities}

