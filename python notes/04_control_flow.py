import random

# ============================================================
# IF / ELIF / ELSE
# ============================================================
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# nested if else
x = 10
if x > 5:
    if x < 15:
        print("x is between 5 and 15")
    else:
        print("x is greater than or equal to 15")
else:
    print("x is less than or equal to 5")

# elif
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
else:
    print("x is less than or equal to 5")

# ============================================================
# INDENTATION
# ============================================================
# In Python, indentation defines the scope of loops, functions,
# and other code blocks.
# Standard practice: 4 spaces per level of indentation.
# Inconsistent indentation causes IndentationError.
if x > 5:
    print("x is greater than 5")   # indented 4 spaces - part of if block
else:
    print("x is not greater than 5")  # indented 4 spaces - part of else block

# shorthand if else (ternary operator)
x, y = 10, 20
z = x if x > y else y
print(z)  # 20
# use shorthand only for simple conditions
# complex conditions should use regular if/else for readability

# ============================================================
# WHILE LOOP
# ============================================================
i = 0
while i < 5:
    print(i)
    i += 1

# while with else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("while loop is finished")

# ============================================================
# FOR LOOP
# ============================================================
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# you can use for with: range, strings, lists, tuples,
# dictionaries, sets, and other iterable objects

for i in range(5):
    print(i)  # 0 to 4

for char in "hello":
    print(char)  # each character

for key in {"name": "Alice", "age": 30}:
    print(key)  # prints keys

for value in {"name": "Alice", "age": 30}.values():
    print(value)  # prints values

for item in {1, 2, 3}:
    print(item)  # each item in set

# for with else
for i in range(5):
    print(i)
else:
    print("loop is finished")

# ============================================================
# RANGE FUNCTION
# ============================================================
range(0, 5)          # sequence from 0 to 4
list(range(15))      # list of numbers from 0 to 14
range(1, 11, 2)      # sequence of odd numbers from 1 to 10
list(range(1, 11, 2)) # [1, 3, 5, 7, 9]

# ============================================================
# SEQUENCES
# ============================================================
["apple", "banana", "cherry"]  # list  - mutable sequence
("apple", "banana", "cherry")  # tuple - immutable sequence

# ============================================================
# NESTED LOOPS
# ============================================================
rows = int(input("enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(0, i):
        print("*", end="")
    print()  # new line after each row

# real world uses of loops:
# - display products on shopping sites
# - read data from a database
# - perform calculations for each item in a list

# ============================================================
# BREAK
# ============================================================
# exits the loop immediately when condition is met
for i in range(10):
    if i == 5:
        break
    print(i)  # prints 0 to 4

# break in linear search - stops when element is found
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index of target element
    return -1          # return -1 if not found

# ============================================================
# CONTINUE
# ============================================================
# skips current iteration and moves to next
for i in range(10):
    if i == 5:
        continue       # skip 5
    print(i)           # prints 0-9 except 5

# real world use: skip irrelevant items while processing a list
def process_items(items):
    for item in items:
        if not is_relevant(item):
            continue   # skip non-relevant items
        print(item)    # process only relevant items

# ============================================================
# PASS
# ============================================================
# does nothing - placeholder for future code
# allows syntactically correct code without logic yet
for i in range(10):
    if i == 5:
        pass           # does nothing when i is 5
    print(i)           # prints 0-9 including 5

# ============================================================
# ENUMERATE
# ============================================================
# get index and value of each item in a list
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"the index of {fruit} is {index}")
# index of apple is 0, banana is 1, cherry is 2

# specify starting index with start parameter
for index, fruit in enumerate(fruits, start=1):
    print(f"the index of {fruit} is {index}")
# index of apple is 1, banana is 2, cherry is 3
