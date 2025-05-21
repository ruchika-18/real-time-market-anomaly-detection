class A:
    def __init__(self): self.val = "A"
    def a1(self): print("A1")
    def show(self): print("Show A")

class B(A):
    def __init__(self): super().__init__(); self.val = "B"
    def b1(self): print("B1")
    def show(self): print("Show B")

class C(B):
    def __init__(self): super().__init__(); self.val = "C"
    def c1(self): print("C1")
    def show(self): print("Show C")

# Create instances
a, b, c = A(), B(), C()

# Own methods
a.a1(); a.show()
b.a1(); b.b1(); b.show()
c.a1(); c.c1(); c.show()

# Overridden method via superclass reference
ref = A(); ref = B(); ref.show()
ref = C(); ref.show()

# Data member polymorphism
print(a.val, b.val, c.val)
