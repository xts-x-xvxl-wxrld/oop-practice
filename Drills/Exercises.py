"""#OOP Exercise 1: Create a Class with instance attributes
class Domino:
        def __init__(self, margarita, peperoni):
            self.peperoni = peperoni
            self.margarita = margarita"""

"""#OOP Exercise 2: Create a Vehicle class without any variables and methods
class Domino:
    def __init__(self, ):
        self.self = self"""


"""#OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass"""


"""#OOP Exercise 4: Class Inheritance
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)"""


"""#OOP Exercise 5: Define a property that must have the same value for every class instance (object)
class Vehicle:

    color = 'White'

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass"""


"""#OOP Exercise 6: Class Inheritance
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        fare = self.capacity * 100
        total = fare + (fare * .10)
        return total


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())"""


"""#OOP Exercise 7: Check type of an object

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(type(School_bus))"""


"""#OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus, Vehicle))"""