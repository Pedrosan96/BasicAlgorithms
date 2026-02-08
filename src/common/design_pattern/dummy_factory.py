from abc import ABC, abstractmethod
from enum import Enum
"""The factory will receive a parameter to determine which vehicle type to create.

Your Task is to: Create a Vehicle Factory that can create different types of vehicles (e.g., Car, Motorcycle, Bicycle) based on the input parameter. Make sure that the input parameters are defined as an enumeration."""
# Step 0: Create an enumeration for vehicle types
class VehicleType(Enum):
    CAR = "Car"
    MOTORCYCLE = "Motorcycle"
    BICYCLE = "Bicycle"

# Step 1: Create an abstract Vehicle class
class Vehicle(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

# Step 2: Create concrete vehicle classes
class Car(Vehicle):
    # Implement the get_name() method
    def get_name(self):
        return "Car"

class Motorcycle(Vehicle):
    # Implement the get_name() method
    def get_name(self):
        return "Motorcycle"

class Bicycle(Vehicle):
    # Implement the get_name() method
    def get_name(self):
        return "Bicycle"

# Step 3: Create a VehicleFactory class
class VehicleFactory:
    def create_vehicle(self, vehicle_type: VehicleType) -> Vehicle:
        if vehicle_type == VehicleType.CAR:
            return Car()
        elif vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle()
        elif vehicle_type == VehicleType.BICYCLE:
            return Bicycle()
        else:
            # If unrecognized tests expect exactly a ValueError here
            raise ValueError(f"Unknown vehicle type: {vehicle_type!r}")

# Step 4: Test the VehicleFactory class
def main():
    vehicle_factory = VehicleFactory()

    # Test the VehicleFactory by creating different types of vehicles
    car = vehicle_factory.create_vehicle(VehicleType.CAR)
    print(car.get_name())

    motorcycle = vehicle_factory.create_vehicle(VehicleType.MOTORCYCLE)
    print(motorcycle.get_name())

    bicycle = vehicle_factory.create_vehicle(VehicleType.BICYCLE)
    print(bicycle.get_name())

if __name__ == "__main__":
    main()
