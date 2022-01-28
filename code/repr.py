class Dog:
    def __init__(self, name: str, breed: str, collar_color: str):
        self._name = name # type: str
        self._breed = breed # type: str
        self._collar_color = collar_color

    def __repr__(self) -> str:
        return f"name: {self._name}, breed: {self._breed}, collar_color: {self._collar_color}"

    def __str__(self) -> str:
        return "Your dog, {self._name} is a {self._breed}"
