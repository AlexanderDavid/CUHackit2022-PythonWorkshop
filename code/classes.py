from random import choice

class Dog:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    def bark(self):
        print("WOOF")

    @staticmethod
    def make_random_dog():
        names = ["Frido", "Spot", "Kansas", "Lucky"]
        breeds = ["German Shepard", "Border Collie", "Golden Doodle", "Labrador"]
        return Dog(choice(names), choice(breeds))
