#function for arithmetic operators
def arithmetic_operations(a, b):
    print("Addition (a + b):", a + b)
    print("Subtraction (a - b):", a - b)
    print("Multiplication (a * b):", a * b)
    if b != 0:
        print("Division (a / b):", a / b)
    else:
        print("Division (a / b): Error! Division by zero.")

# Example usage
num1 = 10
num2 = 5
arithmetic_operations(num1, num2)

#method for increment and decrement operators
def increment_decrement_demo():
    # Manual increment and decrement
    a = 0
    print("Initial value of a:", a)

    a += 1  # Increment by 1
    print("After a += 1:", a)

    a = a + 1  # Another way to increment
    print("After a = a + 1:", a)

    a -= 1  # Decrement by 1
    print("After a -= 1:", a)

    # Increment using a for loop
    print("\nincremented for loop:")
    for i in range(0, 5):  # From 0 to 4
        print(i)

    # Decrement using a for loop
    print("\ndecremented for loop:")
    for i in range(4, -1, -1):  # From 4 to 0
        print(i)

# Call the function
increment_decrement_demo()

# a program to find the two numbers equal or not.
x = input("enter first number: ")
y = input("enter second number: ")
if x==y:
    print("both numbers are equal")
else:
    print("both numbers are not equal")

 #program for relational operators
    def relational_operators_demo(a, b):
        print("a =", a)
        print("b =", b)

        print("\nRelational Operator Results:")
        print("a < b  :", a < b)
        print("a <= b :", a <= b)
        print("a > b  :", a > b)
        print("a >= b :", a >= b)

    # Example usage
    num1 = 10
    num2 = 20
    relational_operators_demo(num1, num2)

#Print the smaller and larger number
x = float(input('Enter first number: '))
y = float(input('Enter second number: '))
#To print larger number
if x > y:
     print(x, "is greater ")
else:
    print(y, " is greater ")
#To print smaller number
if x < y:
     print(x, "is smaller ")
else:
    print(y, " is smaller ")

