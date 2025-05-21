#defining a static variable and access that through a class
class MyClass:
    static_var = 42  # Static variable
# Accessing through class
print(MyClass.static_var)  # Output: 42
#Change within the class
MyClass.static_Var = 12
print(MyClass.static_var)

#accessing that through an instance
instance = MyClass()
print(instance.static_var)

#Change within an instance
instance.static_var = 15
print(instance.static_var)
print(MyClass.static_var)


