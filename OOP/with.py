class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
car1 = Car('Tesla', 'Red') #values automatically set

print(car1.brand, car1.color)

"""
syntax:
    def __init__(self, parameter1, parameter2):
        self.property1 = parameter1
        self.property2 = parameter2
        
__init__() constructor
self.property:
"""