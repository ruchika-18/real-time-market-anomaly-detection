#program to print your name
name = input("Enter your name")
print("hi,", name)

#program for a Single line comment and multi-line comments
#here is a single line comment
print("hello from a program with comments!")
"""
This is a multi-line comment.
using triple double quotes.
It can span multiple lines.

"""

'''
we can also use triple single quotes
for multi-line comments

'''

print("Comments helps in explaining the code.")

#Define variables for different Data Types int, Boolean, char, float, double and print on the console
#integer variable
age = 25

#boolean variable
is_student = True

# Character (a single-character string in Python)
initial = 'A'

# Float variable
height = 5.9

# Double (Python's float is equivalent to double-precision)
weight = 72.3456789012345

# Printing all variables
print("Age (int):", age)
print("Is Student (bool):", is_student)
print("Initial (char):", initial)
print("Height (float):", height)
print("Weight (double):", weight)

#Define the local and Global variables with the same name and print both variables and understand the scope of the variables
x = 10
# Uses global because there is no local 'x'
def alpha():
    print('Inside alpha() :', x)

# Variable 'x' is redefined as a local
def beta():
    x = 20
    print('Inside beta() :', x)

# Uses global keyword to modify global 'x'
def gamma():
    global x
    x = 30  # Value of 'x' modified
    print('Inside gamma() :', x)

# Global scope
print('global :', x)
alpha()
print('global :', x)
beta()
print('global :', x)
gamma()
print('global :', x)


