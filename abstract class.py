# abstract class with abstract and non-abstract methods.
from abc import ABC, abstractmethod
# Abstract class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):  # abstract method
        pass

    def sleep(self):       # non-abstract method
        print("Sleeping...")
# Subclass implementing abstract method
class Dog(Animal):
    def make_sound(self):
        print("Bark!")
# Usage
d = Dog()
d.make_sound()
d.sleep()

#Create a sub class for an abstract class. Create an object in the child class for the abstract class and access the non-abstract methods
from abc import ABC, abstractmethod
# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def fuel_type(self):
        print("This vehicle uses diesel or petrol.")

# Subclass implementing abstract method
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

# Create object of the subclass
my_car = Car()

# Access non-abstract method from abstract class
my_car.fuel_type()

# Also access the implemented abstract method
my_car.start_engine()

#Create an instance for the child class in child class and call abstract methods
from abc import ABC, abstractmethod
# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Child class
class Dog(Animal):
    def sound(self):
        print("Dog barks")

    def call_self(self):
        d = Dog()
        d.sound()
# Run it
dog = Dog()
dog.call_self()

# Create an instance for the child class in child class and call non-abstract methods
from abc import ABC, abstractmethod
# Abstract base class
class Parent(ABC):
    def greet(self):  # Non-abstract method
        print("Hello from Parent!")

    @abstractmethod
    def task(self):   # Abstract method
        pass

# Child class
class Child(Parent):
    def task(self):  # Implement abstract method
        print("Task done by Child.")

    def call_non_abstract(self):
        obj = Child()
        obj.greet()

# Create object and call method
c = Child()
c.call_non_abstract()





