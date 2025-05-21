#function to add integer values of an array
def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
# Example usage
numbers = [10, 20, 30, 40]
result = sum_of_array(numbers)
print("Sum of the array:", result)

#function to calculate the average value of an array of integers
def average_of_array(arr):
    if len(arr) == 0:
        return 0
    total = sum(arr)
    average = total / len(arr)
    return average
# Example usage
numbers = [10, 20, 30, 40, 50]
avg = average_of_array(numbers)
print("Average value of the array:", avg)

#program to find the index of an array element
def find_index(arr, target):
    if target in arr:
        index = arr.index(target)
        print(f"The index of {target} is: {index}")
    else:
        print(f"{target} is not in the list.")
# Example usage
numbers = [10, 20, 30, 40, 50]
element_to_find = int(input("Enter the number to find its index: "))
find_index(numbers, element_to_find)

# function to test if array contains a specific value
def contains_value(arr, target):
    return target in arr
# Example usage
numbers = [5, 10, 15, 20, 25]
value = int(input("Enter a number to check: "))
if contains_value(numbers, value):
    print(f"{value} exists in the array.")
else:
    print(f"{value} does not exist in the array.")

# function to remove a specific element from an array
def remove_element(arr, target):
    if target in arr:
        arr.remove(target)
        print(f"{target} has been removed.")
    else:
        print(f"{target} not found in the array.")
    return arr
# Example usage
numbers = [10, 20, 30, 40, 50]
value = int(input("Enter the number to remove: "))
updated_list = remove_element(numbers, value)
print("Updated array:", updated_list)

# function to copy an array to another array
def copy_array(source_array):
    copied_array = source_array.copy()
    return copied_array

# Example usage
original = [1, 2, 3, 4, 5]
copy = copy_array(original)

print("Original array:", original)
print("Copied array:", copy)

# function to insert an element at a specific position in the array
def insert_at_position(arr, value, position):
    if position < 0 or position > len(arr):
        print("Invalid position!")
    else:
        arr.insert(position, value)
        print(f"{value} inserted at position {position}.")
    return arr

# Example usage
numbers = [10, 20, 30, 40]
val = int(input("Enter the value to insert: "))
pos = int(input("Enter the position (0-based index): "))

updated_array = insert_at_position(numbers, val, pos)
print("Updated array:", updated_array)

#a function to find the minimum and maximum value of an array
def find_min_max(arr):
    if not arr:
        return None, None  # Handle empty list
    minimum = min(arr)
    maximum = max(arr)
    return minimum, maximum

# Example usage
numbers = [12, 5, 8, 19, 33, 1, 17]
min_val, max_val = find_min_max(numbers)

print("Minimum value in the array:", min_val)
print("Maximum value in the array:", max_val)

#function to reverse an array of integer values
def reverse_array(arr):
    return arr[::-1]

#function to find the duplicate values of an array
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# program to find the common values between two arrays
def find_common_values(arr1, arr2):
    return list(set(arr1) & set(arr2))
#example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
common = find_common_values(arr1, arr2)
print(common)  # Output: [4, 5]

# a method to remove duplicate elements from an array
#Initialize array
arr = [10,20,30,10,40,50]
final_array = [] #empty array
#Using loop to remove duplicated elements
for i in arr:
    if i not in final_array:
        final_array.append(i)
print(final_array)

# a method to find the "second largest" number in an array
#Initialize array
arr = [11,4,22,99,66,5,80,33,77]
arr.sort() #Sorting in ascending order.
print("Second largest number:",arr[-2]) #displaying the second last element.

#method to find number of even number and odd numbers in an array
def find_even_odd(arr):
    even_numbers = [num for num in arr if num % 2 == 0]
    odd_numbers = [num for num in arr if num % 2 != 0]
    return even_numbers, odd_numbers

# function to get the difference of largest and smallest value
#Initialize array
arr = [30,5,7,23,4]
arr.sort() #Sorting in ascending order
print("Difference of largest and smallest value:",arr[3]-arr[2])

# method to verify if the array contains two specified elements(12,23)
arr = [9,16,12,3,23,80]
for i in arr:
    if i == 12:
        print("Exist in array")
    if i == 23:
        print("Exist in array")

# program to remove the duplicate elements and return the new array
def remove_duplicates(arr):
    seen = set()
    unique = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            unique.append(num)
    return unique











