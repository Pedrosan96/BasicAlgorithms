from abc import ABC, abstractmethod
"""Task: Implement the Builder Design Pattern to create a custom computer system."""
class Computer:
    def __init__(self):
        # Initialize the attributes
        self.__dict__ = {'processor': "", 'memory': "", 'storage': "",  'graphics_card': "", 'operating_system': "", 'extras': []}

class ComputerBuilder(ABC):
    @abstractmethod
    def add_processor(self):
        pass

    @abstractmethod
    def add_memory(self):
        pass

    @abstractmethod
    def add_storage(self):
        pass

    @abstractmethod
    def add_graphics_card(self):
        pass

    @abstractmethod
    def add_operating_system(self):
        pass

    @abstractmethod
    def add_extras(self):
        pass

class CustomComputerBuilder(ComputerBuilder):
    def __init__(self):
        # Initialize a Computer object
        self.computer = Computer()

    # Override abstract methods and set Computer attributes
    def add_processor(self, processor):
        self.computer.__dict__['processor'] = processor

    def add_memory(self, memory):
        self.computer.__dict__['memory'] = memory

    def add_storage(self, storage):
        self.computer.__dict__['storage'] = storage

    def add_graphics_card(self, graphics_card):
        self.computer.__dict__['graphics_card'] = graphics_card

    def add_operating_system(self, operating_sys):
        self.computer.__dict__['operating_system'] = operating_sys

    def add_extras(self, extras):
        self.computer.__dict__['extras'].extend(extras)

class ComputerDirector:
    def __init__(self, builder):
        # Initialize the builder instance
        self.builder = builder

    def build_computer(self, specs):
        # Call the add_* methods of the builder with the specs
        self.builder.add_processor(specs["processor"])
        self.builder.add_memory(specs["memory"])
        self.builder.add_storage(specs["storage"])
        self.builder.add_graphics_card(specs["graphics_card"])
        self.builder.add_operating_system(specs["operating_system"])
        self.builder.add_extras(specs["extras"])


# Helper function to test the computer building process
def test_computer_building(specs, expected_output):
    builder = CustomComputerBuilder()
    director = ComputerDirector(builder)
    director.build_computer(specs)
    computer = builder.computer
    assert computer.__dict__ == expected_output, f"Expected {expected_output}, but got {computer.__dict__}"

# Test cases
test_specs = {
    'processor':        'Intel Core i5',
    'memory':           '8GB',
    'storage':          '512GB SSD',
    'graphics_card':    'Integrated',
    'operating_system': 'Windows 11',
    'extras':           ['Wi-Fi']
}

expected_output = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated',
    'operating_system': 'Windows 11',
    'extras': ['Wi-Fi']
}

test_computer_building(test_specs, expected_output)

print("All tests passed!")
