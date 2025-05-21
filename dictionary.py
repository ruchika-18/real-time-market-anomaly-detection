#creating  a dictionary with at least 5 key value pairs of student id and name
students = {
    "S001": "Alice",
    "S002": "Bob",
    "S003": "Charlie",
    "S004": "David",
    "S005": "Eve"
}
print("Initial Dictionary:", students)

#adding values in the dictionary
students["S006"] = "Frank"
print("After Adding S006:", students)

#updating values in the dictionary
students["S002"] = "Bobby"
print("After Updating S002:", students)

#accessing the value in the dictionary
print("Value for S003:", students["S003"])

#creating a nested loop dictionary
student_details = {
    "S001": {"Name": "Alice", "Age": 20},
    "S002": {"Name": "Bobby", "Age": 21},
    "S003": {"Name": "Charlie", "Age": 22}
}
print("Nested Dictionary:", student_details)

#accessing the values of nested loop dictionary
print("Name of S001:", student_details["S001"]["Name"])
print("Age of S003:", student_details["S003"]["Age"])

#printing the keys present in a particular dictionary
print("Keys in students dictionary:", students.keys())

#deleting a value from a dictionary
del students["S004"]
print("After deleting S004:", students)
