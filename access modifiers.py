#1.class with private fields
class A:
    def __init__(self):
        self.__x = 100     # private field
        self.__y = 200     # private field

    def __display(self):   # private method
        print("Private method called")

    def main(self):        # main-like method
        print("x:", self.__x)
        print("y:", self.__y)
        self.__display()

class B(A):
    def try_access(self):
        # Trying to access private fields/methods
        try:
            print("Accessing __x:", self.__x)
        except AttributeError:
            print("Cannot access private field '__x'")

        try:
            self.__display()
        except AttributeError:
            print("Cannot call private method '__display'")

# Execution
a = A()
a.main()

b = B()
b.try_access()

#2.class with protected fields
class Base:
    def __init__(self):
        self._x = 10
        self._y = 20

    def _protected_method(self):
        print("Base: protected method")

    def main_access(self):
        print("In Base:", self._x, self._y)
        self._protected_method()

class SamePackage:
    def access(self):
        b = Base()
        print("SamePackage:", b._x, b._y)
        b._protected_method()

class Child(Base):
    def access(self):
        print("Child (subclass):", self._x, self._y)
        self._protected_method()

class Other:
    def access(self):
        b = Base()
        print("Other (unrelated):", b._x, b._y)
        b._protected_method()

# Simulate all accesses
Base().main_access()
SamePackage().access()
Child().access()
Other().access()

#3.class with public fields
# public_class.py

class PublicClass:
    def __init__(self):
        self.x = 10  # public field
        self.y = 20  # public field

    def greet(self):  # public method
        print("Hello from PublicClass!")

# Same "package"
class SamePackage:
    def access(self):
        obj = PublicClass()
        print("SamePackage:", obj.x, obj.y)
        obj.greet()

# Simulating different "package"
class DifferentPackage:
    def access(self):
        obj = PublicClass()
        print("DifferentPackage:", obj.x, obj.y)
        obj.greet()

# Test all
SamePackage().access()
DifferentPackage().access()


