# program to generate Arithmetic Exception without exception handling
print("Arithmetic Exception Example: Division by Zero")
numerator = 100
denominator = 0
result = numerator / denominator
print("Result:", result)

# Handling the Arithmetic exception using try-catch block
a = 10
b = 0
try:
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Caught an Arithmetic Exception: Cannot divide by zero.")
print("Program completed safely.")

# method which throws exception, Call that method in main class without try block
class MyClass:
    def risky_method(self):
        raise ValueError("This is a custom exception!")
# Main code
print("Calling method that throws an exception...")

obj = MyClass()
obj.risky_method()
print("This line will not be executed.")

#Write a program with multiple catch blocks
def divide_numbers(a, b):
    return a / b
try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    result = divide_numbers(x, y)
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid integers.")

except Exception as e:
    print("General error occurred:", str(e))
print("Program completed.")

#a program to throw exception with your own message
def check_age(age):
    if age < 18:
        raise Exception("Custom Error: Age must be 18 or above.")
    else:
        print("Access granted.")
# Call the function
age = int(input("Enter your age: "))
check_age(age)
print("Program completed.")

#a program to create your own exception
class InvalidAgeError(Exception):
    def __init__(self, message):
        super().__init__(message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    print("Age is valid.")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print("Error:", e)

#a program with finally block
def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    finally:
        print("This block always runs (finally).")

# Test the function
x = int(input("Enter numerator: "))
y = int(input("Enter denominator: "))
divide(x, y)

#a program to generate Arithmetic Exception
def divide(a, b):
    return a / b
try:
    num1 = 10
    num2 = 0
    result = divide(num1, num2)
    print("Result:", result)
except ZeroDivisionError as e:
    print("Arithmetic Exception occurred:", e)

#a program to generate FileNotFoundException
try:
    # Trying to open a file that does not exist
    file = open("non_existent_file.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("FileNotFoundError occurred:", e)

#a program to generate ClassNotFoundException
try:
    # Trying to import a non-existent module (or class)
    import nonexistent_module
except ModuleNotFoundError as e:
    print("Simulated ClassNotFoundException occurred:", e)

#program to generate IOException
try:
    # Open a file in read-only mode and try writing to it
    with open("readonly_test.txt", "r") as file:
        file.write("Trying to write to a read-only file.")
except OSError as e:
    print("IOException (OSError) occurred:", e)

#a program to generate NoSuchFieldException
class Student:
    def __init__(self, name):
        self.name = name
try:
    s = Student("Alice")
    print(s.age)  # 'age' field does not exist
except AttributeError as e:
    print("Simulated NoSuchFieldException occurred:", e)









