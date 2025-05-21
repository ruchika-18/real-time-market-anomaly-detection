class MyClass:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Default Constructor")
        elif b is None:
            print(f"One-Argument Constructor: {a}")
        else:
            print(f"Two-Argument Constructor: {a}, {b}")

# Test
MyClass()
MyClass(10)
MyClass(10, 20)


class SuperClass:
    def __init__(self, x=None):
        if x is None:
            print("Superclass Default Constructor")
        else:
            print(f"Superclass One-Arg Constructor: {x}")

class SubClass(SuperClass):
    def __init__(self, x=None):
        super().__init__(x)
        print("Subclass Constructor")

# Test
SubClass()
SubClass(5)


class AccessDemo:
    def __init__(self):
        print("Public Constructor")

    def _protected_constructor(self):
        print("Protected Constructor")

    def __private_constructor(self):
        print("Private Constructor")

    def default_constructor(self):
        print("Default (package-private) Constructor")


class ConstructorAttributes:
    def __init__(self, x):
        self.a = x
        print(f"Constructor with a = {self.a}")

    @classmethod
    def copy_constructor(cls, other):
        return cls(other.a)

# Test
obj1 = ConstructorAttributes(50)
obj2 = ConstructorAttributes.copy_constructor(obj1)




