# ============================================================
# OBJECT ORIENTED PROGRAMMING (OOP)
# ============================================================
# Why OOP?
# Procedural programming: focuses on procedures/routines that operate on data
# OOP: focuses on objects that encapsulate both data AND behavior
#
# OOP allows:
# - Better code organization
# - Code reusability through inheritance
# - Modelling real-world entities effectively
# - Encapsulation (hiding internal state)
# - Polymorphism (flexible, extensible code)
# - Easier collaboration on large projects
#
# Key concepts: classes, objects, inheritance, polymorphism, encapsulation

# ============================================================
# BASIC CLASS EXAMPLE
# ============================================================
class definitions:
    def person(name, age):
        print(f"Name: {name}, Age: {age}")

definitions.person("Alice", 30)  # Name: Alice, Age: 30

# ============================================================
# CLASS WITH __init__ (CONSTRUCTOR) AND METHODS
# ============================================================
class Person:
    def __init__(self, name, age):
        self.name = name   # attribute
        self.age = age     # attribute

    def greet(self):       # method
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def changeName(self, new_name):
        self.name = new_name

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
print(person1.greet())  # Hello, my name is Alice and I am 30 years old.
print(person2.greet())  # Hello, my name is Bob and I am 25 years old.

alice = Person("Alice", 30)
print(alice.greet())           # Hello, my name is Alice...
alice.changeName("Malice")
print(alice.greet())           # Hello, my name is Malice...

# SELF
# self is a reference to the current instance of the class
# used to access attributes and methods within the class
# convention is to name it 'self' but any name technically works
# Python automatically passes the object as first argument when method is called
# self ka matlab wo object hai jispe method call ho rha hai
# self ke through hum us object ke attributes aur methods ko access kar sakte hain

# ============================================================
# CONSTRUCTORS
# ============================================================
# A constructor is a special method called automatically when
# an object is created. Defined using __init__().
# Used to initialize attributes of the class.

# 1. DEFAULT CONSTRUCTOR - no parameters
class DefaultConstructorExample:
    def __init__(self):
        self.message = "This is a default constructor"

# 2. PARAMETERIZED CONSTRUCTOR - takes parameters
class ParameterizedConstructorExample:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 3. COPY CONSTRUCTOR - creates object as copy of another
class CopyConstructorExample:
    def __init__(self, other):
        self.name = other.name
        self.age = other.age

original = ParameterizedConstructorExample("Alice", 30)
copy = CopyConstructorExample(original)
print(copy.name)  # Alice
print(copy.age)   # 30

# CAR CLASS EXAMPLE
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print(f"Car created: {self.make} {self.model} ({self.year})")

a = Car("Toyota", "Camry", 2020)
print(a.make)    # Toyota
print(a.model)   # Camry
print(a.year)    # 2020

# ============================================================
# GETTERS AND SETTERS
# ============================================================
# Allow controlled access to attributes
# Getter: retrieves attribute value
# Setter: sets attribute value with optional validation
# Use @property decorator for getter
# Use @<attribute>.setter decorator for setter
# Underscore prefix (_name) signals attribute is intended as private

class PersonWithValidation:
    def __init__(self, name):
        self._name = name  # _ indicates intended to be private

    @property
    def name(self):        # getter
        return self._name

    @name.setter
    def name(self, new_name):  # setter with validation
        if isinstance(new_name, str) and new_name:
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string.")

p = PersonWithValidation("Alice")
print(p.name)      # Alice  (uses getter)
p.name = "Bob"     # uses setter
print(p.name)      # Bob
# p.name = ""      # raises ValueError
