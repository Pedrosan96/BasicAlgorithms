from abc import ABC, abstractmethod
from enum import Enum
"""The factory will receive a parameter to determine which animal type to create and a dictionary containing the context data for initializing the animal objects.


Task: Create an Animal Factory that can create different types of animals (e.g., Dog, Cat, Fish) based on the input parameter and context data."""

# Step 0: Create an enumeration for animal types
class AnimalType(Enum):
    DOG = "Dog"
    CAT = "Cat"
    FISH = "Fish"


# Step 1: Create an abstract Animal class
class Animal(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass


# Step 2: Create concrete animal classes
class Dog(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, context: dict):
        self.name = context["name"]
        self.age = context["age"]

    def get_info(self):
        return self.name, self.age


class Cat(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, context: dict):
        self.name = context["name"]
        self.age = context["age"]

    def get_info(self):
        return self.name, self.age


class Fish(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, context: dict):
        self.name = context["name"]
        self.age = context["age"]

    def get_info(self):
        return self.name, self.age


# Step 3: Create an AnimalFactory class
class AnimalFactory:
    def create_animal(self, animal_type: AnimalType, context: dict) -> Animal:
        # Implement the logic to create an animal based on the animal_type parameter and context data
        if animal_type == AnimalType.DOG:
            return Dog(context)
        elif animal_type == AnimalType.CAT:
            return Cat(context)
        elif animal_type == AnimalType.FISH:
            return Fish(context)
        else:
            raise ValueError(f"Unknown animal type: {animal_type!r}")


# Step 4: Test the AnimalFactory class
def main():
    animal_factory = AnimalFactory()

    # Test the AnimalFactory by creating different types of animals and passing context data
    dog = animal_factory.create_animal(AnimalType.DOG, {"name": "Dog", "age": 11})
    print(dog.get_info())

    cat = animal_factory.create_animal(AnimalType.CAT, {"name": "Cat", "age": 7})
    print(cat.get_info())

    fish = animal_factory.create_animal(AnimalType.FISH, {"name": "Fish", "age": 1})
    print(fish.get_info())


if __name__ == "__main__":
    main()
