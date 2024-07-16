# Prevents a user from creating an object of that class
#+ compels a user to ovverride abstract methods in a child class

#abstract class   = a class which contains one or more abstract methods.
#abstract methods = a method tahat has a declaration but does not have an implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("this car is stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("this motorcycle is stopped")

car= Car()
motorcycle = Motorcycle()


car.go()
motorcycle.go()
car.stop()
motorcycle.stop()
