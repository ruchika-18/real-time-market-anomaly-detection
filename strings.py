#different ways of creating string
string = 'hola'
print(string)

string = "hola"
print(string)

string1 = '''hii'''
print(string1)

string2 = """welcome
                everyone"""
print(string2)
print()

#Concatenating two strings using + operator
my_str = string + string1
print("Concatenated string is:",str)
print()

# Finding the length of the string
print("length of the string:",len(my_str))
print()

#Extracting a string using Substring
string1 = '''hii'''
substring = string1[1:3]  # Extracts characters from index 1 to 2
print("Substring from string1 is:", substring)

# Searching in strings using index()
str3 = 'helloworld'
str1 = 'llo'
str2 = 'h'
print("Position of llo:",str3.index(str1))
print("Position of o:",str3.index(str2))
print()

#Matching a String Against a Regular Expression With matches()
import re
pattern = r"\d{3}"  # Matches exactly 3 digits
string = "123"
if re.fullmatch(pattern, string):
    print("Matched!")
else:
    print("Not matched.")

#Comparing strings
str5 = 'hello everyone'
str6 = 'welcome everyone'
str7 = str5
print(str5 == str6)
print(str5 == str7)
print(str6 == str7)
print(str5 != str6)
print()

#startsWith(), endsWith() and compareTo()
string = 'hello everyone'
print(string.startswith("hello"))
print(string.endswith("one"))
print()

#Trimming strings with strip()
str7 = 'Hello everyone hi'
print(str7.strip("hi"))
print()

#Replacing characters in strings with replace()
string = 'hi you'
print(string.replace("hi","hey"))
print()

# Splitting strings with split()
str9 = 'hey-you-man'
print(str9.split("-"))
print()

# Converting integer objects to Strings
number = 18
number_as_str = str(number)
print(number_as_str)
print(type(number_as_str))

#Converting to uppercase and lowercase
string = 'hi'
string1 = 'everyone'
print(string.upper())
print(string1.lower())



