from random import choice

class Dog:
    def __init__(self, name: str, breed: str):
        self._name = name # type: str
        self._breed = breed # type: str

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    def bark(self):
        print("WOOF")

    @staticmethod
    def make_random_dog() -> "Dog":
        names = ["Frido", "Spot", "Kansas", "Lucky"] # type: List[str]
        breeds = ["German Shepard", "Border Collie", "Golden Doodle", "Labrador"] # type: List[str]
        return Dog(choice(names), choice(breeds))
