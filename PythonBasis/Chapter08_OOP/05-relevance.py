"""
Created by Ignorant on 2024/2/4
Description: Relevance
"""


class Road(object):
    def __init__(self, name, length):
        self.name = name
        self.length = length


class Car(object):
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road, length):
        if length > road.length:
            return "The length is greater than the road's length"
        return "The {} has been driven in the speed of {} km/h for {} minutes on the {}.".format(
            self.brand, self.speed, road.length / self.speed * 60, road.name)

    def __str__(self):
        return "class Car: {}".format(dict([("brand", self.brand), ("speed", self.speed)]))


road1 = Road("S19", 2000)
car = Car("Ford", 100)
print(car.get_time(road1, 1000))
