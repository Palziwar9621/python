# ============================================================
# STRINGS
# ============================================================
# A string is a sequence of Unicode characters
# Enclosed in single, double, or triple quotes
# Strings are IMMUTABLE - cannot be modified after creation

string1 = 'Hello, World!'
string2 = "Hello, World!"
string3 = '''Hello, World!'''
string4 = """Hello, World!"""

# accessing characters
print(string1[0])   # H  (first character)
print(string1[-1])  # !  (last character)

# slicing
print(string1[0:5])     # Hello
print(string1[0:12:2])  # Hlo ol (every second character)
print(string1[::-1])    # !dlroW ,olleH (reverse)

# editing/deleting strings
# strings are immutable so you cannot change individual characters
# instead create a new string
string1 = "Hello, World!"
string2 = string1[:5] + " Python!"  # 'Hello Python!'
del string1  # deletes the variable from memory

# arithmetic operations on strings
string1 = "Hello, World!"
string2 = "Python is great!"
concatenated_string = string1 + " " + string2
print(concatenated_string)  # Hello, World! Python is great!
print(string1 * 3)          # repeats string1 three times

# relational operations
print(string1 == string2)  # False
print(string1 != string2)  # True
print(string1 > string2)   # False (lexicographical order)
print(string1 < string2)   # True  (lexicographical order)

# membership operations
print("Hello" in string1)   # True
print("Python" in string1)  # False

# logical operations on strings
# strings are truthy if non-empty, falsy if empty
"hello" and "world"  # returns "world" - both truthy, returns last
"" or "world"        # returns "world" - "" is falsy, returns second
"hello" or ""        # returns "hello" - first is truthy, stops there
not "hello"          # False - "hello" is truthy, not inverts it
not ""               # True  - "" is falsy, not inverts it

# loop through string
string1 = "Hello, World!"
for char in string1:
    print(char)

# common built-in functions for strings
print(len(string1))     # 13 - length
max(string1)            # 'r' - max character by ASCII value
min(string1)            # ' ' - min character by ASCII value
sorted_string = sorted(string1)  # list of chars sorted by ASCII
print(sorted_string)

# string methods
print(string1.upper())       # HELLO, WORLD!
print(string1.lower())       # hello, world!
print(string1.title())       # Hello, World!
print(string1.capitalize())  # Hello, world!
print(string1.strip())       # removes leading/trailing whitespace
print(string1.replace("Hello", "Hi"))      # Hi, World!
print(string1.split(", "))                 # ['Hello', 'World!']
print(string1.join(["Hello", "World"]))    # HelloHello, World!World
print(string1.find("World"))   # 7 - returns -1 if not found
print(string1.index("World"))  # 7 - raises ValueError if not found
print(string1.count("o"))      # 2
print(string1.startswith("Hello"))  # True
print(string1.endswith("!"))        # True
print(string1.isalpha())   # False (has comma and space)
print(string1.isdigit())   # False
print(string1.isalnum())   # False
print(string1.isspace())   # False
print(string1.islower())   # False
print(string1.isupper())   # False
print(string1.istitle())   # False

# f-string formatting
name = "Alice"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")

# ============================================================
# LISTS
# ============================================================
# Mutable, ordered collection - can contain different data types
# 1. array - homogenous (same type)
# 2. list  - heterogenous (different types)

my_list = [1, 2, 3, "hello", True]
print(my_list)
print(my_list[0])    # 1  (first element)
print(my_list[-1])   # True (last element)
print(my_list[1:4])  # [2, 3, 'hello']
print(my_list[::-1]) # reversed list

# nested lists
L = [1, 2, "lol", [4, 5]]
x = L[3][0]  # 4 - accessing nested list element

L1 = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
x = L1[0][1][0]  # 4

# lists are mutable - can change after creation
my_list = [1, 2, 3]
my_list[0] = 10              # change element at index 0
my_list[1:4] = [20, 30, 40] # change a slice
my_list.append(50)           # add one item to end
my_list.extend([60, 70])     # add multiple items to end
my_list.insert(1, 15)        # insert 15 at index 1
my_list.remove(20)           # remove first occurrence of 20
my_list.pop()                # remove and return last element
my_list.pop(1)               # remove and return element at index 1
del my_list[0]               # delete element at index 0
my_list.clear()              # remove all elements

# list operations
my_list = [1, 2, 3]
print(my_list + [4, 5])      # [1, 2, 3, 4, 5] concatenation
print(my_list * 2)            # [1, 2, 3, 1, 2, 3] repetition
print(4 in my_list)           # False
print(5 not in my_list)       # True

for item in my_list:
    print(item)

# functions on lists
print(len(my_list))           # 3
print(max(my_list))           # 3
print(min(my_list))           # 1
sorted_list = sorted(my_list)
sorted_list_descending = sorted(my_list, reverse=True)
my_list.sort()                # sort in place ascending
my_list.sort(reverse=True)    # sort in place descending
my_list.reverse()             # reverse in place
print(my_list.index(2))       # index of first occurrence of 2
print(my_list.count(2))       # number of occurrences of 2

# ============================================================
# SETS
# ============================================================
# unordered, no duplicates
my_set = {1, 2, 3}
cities  = {"tokyo", "madrid", "berlin", "delhi"}
cities2 = {"tokyo", "madrid", "kabul", "seoul"}

cities3 = cities.union(cities2)         # all unique elements from both
cities4 = cities.intersection(cities2)  # common elements
cities7 = cities.difference(cities2)    # in cities but not in cities2

# NOTE: these methods update the set IN PLACE and return None
# so do NOT assign them to a variable
cities_copy = cities.copy()
cities_copy.symmetric_difference_update(cities2)  # elements in either but not both
cities_copy2 = cities.copy()
cities_copy2.difference_update(cities2)           # removes cities2 elements from cities

# set methods
cities.add("paris")        # add element
cities.remove("paris")     # remove - raises KeyError if not present
cities.discard("paris")    # remove - NO error if not present
cities.isdisjoint(cities2) # True if no common elements
cities.issubset(cities2)   # True if cities is subset of cities2
cities.issuperset(cities2) # True if cities contains all of cities2
cities.copy()              # shallow copy
cities.update(cities2)     # add all elements from cities2
cities5 = cities.copy()
cities5.intersection_update(cities2)  # keep only common elements

# pop from set
try:
    cities.pop()           # remove and return arbitrary element
except KeyError:
    print("the set is empty")

cities.clear()             # remove all elements

# ============================================================
# DICTIONARIES
# ============================================================
# unordered, changeable, indexed collections
# written with curly brackets, have keys and values

person = {"name": "john", "age": 30, "city": "new york"}

print(person)                # entire dictionary
print(person["name"])        # direct key access
print(person.get("age"))     # safe access using get method

# direct access with non-existent key raises KeyError
# print(person["age1"])      # KeyError - key does not exist

# get() returns None instead of raising error
print(person.get("age1"))    # None - no error

print(person.keys())         # all keys
print(person.values())       # all values

for key in person.keys():
    print(key)
    print(f"the value of {key} is {person[key]}")

# ============================================================
# IS vs ==
# ============================================================
# is  -> identity - checks if same object in memory
# ==  -> equality - checks if values are equal

a = [1, 2, 3]
b = [1, 2, 3]  # different object, same values
c = a           # same object as a

print(a is b)   # False - different objects in memory
print(a == b)   # True  - same values
print(a is c)   # True  - same object in memory
print(a == c)   # True

# small integers are cached by Python (usually -5 to 256)
x = 3
y = 3
print(x is y)   # True  - cached
print(x == y)   # True

p = (1, 2, 3)
q = (1, 2, 3)
print(p is q)   # False - not guaranteed same object
print(p == q)   # True
