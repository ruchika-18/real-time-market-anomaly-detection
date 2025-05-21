# two methods with the same name but different number of parameters of same type and call the methods
class OverloadExample:
    # Method with same name 'display' and different number of parameters
    def display(self, a, b=None):
        if b is None:
            print(f"Method called with one parameter: {a}")
        else:
            print(f"Method called with two parameters: {a}, {b}")
# Create an object of the class
obj = OverloadExample()
# Call method with one argument
obj.display(5)
# Call method with two arguments
obj.display(5, 10)

#two methods with the same name but different number of parameters of different data type and call the methods
class OverloadExample:
    def display(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            print(f"Called with one integer: {args[0]}")
        elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], float):
            print(f"Called with a string and a float: {args[0]}, {args[1]}")
        else:
            print("Invalid arguments")
# Create object
obj = OverloadExample()
# Call method with one int
obj.display(10)
# Call method with string and float
obj.display("value", 3.14)

#two methods with the same name and same number of parameters of same type
class MyClass:
    def show(self, x):
        if x == 0:
            print("Called with 0")
        else:
            print(f"Called with: {x}")

# Test
obj = MyClass()
obj.show(0)     # Will trigger first condition
obj.show(5)     # Will trigger else

