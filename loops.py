# program to print  “Bright IT Career”  ten times using for loop
for i in range(10):
    print("Bright IT Career")

#program to print 1 to 20 numbers using the while loop.
num = 1
while num <= 20:
    print(num)
    num += 1

#Program to equal operator and not equal operators
x = 5
y = 10
print(x ==y) #Equal operator
print(x != y) #Not Equal operator

#program to print the odd and even numbers.
n = int(input('enter a number'))
if n % 2 == 0:
    print('Even')
else:
    print('odd')

#program to print largest number among three numbers.
num1 = int(input('enter first number'))
num2 = int(input('enter second number'))
num3 = int(input('enter the third number'))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("Largest number is: ",largest)

#program to print even number between 10 and 20 using while
num = 10
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1

#program to print 1 to 10 using the do-while loop statement
num = 1
while True:
    print(num)
    num += 1
    if num > 10:
        break

#program to find Armstrong number or not
num = int(input("Enter a number: "))
num_str = str(num)
num_digits = len(num_str)
sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** num_digits
if num == sum_of_powers:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

# Program to check if a number is prime
n = int(input('Enter a number: '))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if count == 2:
    print('It is a prime number.')
else:
    print('It is not a prime number.')

#program to check palindrome or not.
n = int(input('Enter a number: '))
m = n
rev = 0
while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r

if m == rev:
    print('Number is a palindrome')
else:
    print('Number is not a palindrome')

# Program to check whether a number is EVEN or ODD using switch
n = int(input("Enter a number: "))
match n % 2:
    case 0:
        print("The number is EVEN")
    case 1:
        print("The number is ODD")

#program according to given M/F using switch
gender = input('enter gender')
if gender =='m' or gender == 'M':
    print('male')
else:
    print('female')






