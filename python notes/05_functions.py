import math
import random
import time
import os
from functools import reduce

# ============================================================
# BUILT-IN FUNCTIONS
# ============================================================
print(len("Hello, World!"))      # 13
print(len([1, 2, 3, 4, 5]))     # 5
print(len({1, 2, 3}))           # 3
print(abs(-5))                    # 5
print(pow(2, 3))                  # 8
print(min(1, 2, 3))               # 1
print(max("kolkata"))             # 't' - max by ASCII value
print(round(3.14159, 2))          # 3.14
quotient, remainder = divmod(10, 3)  # (3, 1)
print(bin(10))    # '0b1010'
print(oct(10))    # '0o12'
print(hex(10))    # '0xa'
x = 10
print(id(x))      # memory address of object - unique identifier
print(ord('A'))   # 65 - ASCII value of 'A'
print(sum([1, 2, 3, 4, 5]))  # 15
# help(len)       # displays documentation for len() function

# ============================================================
# BUILT-IN MODULES
# ============================================================
# Modules are pre-written code for specific tasks
# imported using the import statement

# math module - mathematical functions and constants
print(math.sqrt(16))       # 4.0

# random module - random number generation
print(random.randint(1, 10))        # random int between 1 and 10
random.shuffle([1, 2, 3, 4, 5])    # shuffles list in place, returns None

# time module - working with time and dates
print(time.time())  # current time in seconds since epoch (Jan 1 1970)

# os module - interacting with operating system
print(os.getcwd())  # current working directory

# ============================================================
# OS MODULE - FULL METHOD LIST
# ============================================================
# os.getcwd()              - returns current working directory
# os.listdir(path)         - list files and dirs at path
# os.mkdir(path)           - create new directory
# os.remove(path)          - remove file
# os.rmdir(path)           - remove empty directory
# os.path.join(p1, p2)     - join two paths
# os.path.exists(path)     - True if path exists
# os.path.isfile(path)     - True if path is a file
# os.path.isdir(path)      - True if path is a directory
# os.environ               - dict of environment variables
# os.system(command)       - execute system command
# os.path.basename(path)   - base name of path
# os.path.dirname(path)    - directory name of path
# os.path.splitext(path)   - split into (root, extension)
# os.path.abspath(path)    - absolute path
# os.path.relpath(path)    - relative path from start
# os.path.normpath(path)   - normalize path
# os.rename(src, dst)      - rename file or directory
# os.walk(top)             - generate filenames in directory tree
# docs: https://docs.python.org/3/library/os.html

# example - create directories in a loop
if not os.path.exists("data"):
    os.mkdir("data")
for i in range(0, 100):
    os.mkdir(f"data/day{i+1}")  # creates day1, day2, ... day100

# ============================================================
# HOW IMPORTING MODULES WORKS
# ============================================================
# When you import a module, Python searches in this order:
# 1. Current directory
# 2. Standard library
# 3. site-packages directory (third-party packages)
# 4. PYTHONPATH environment variable directories
# 5. Built-in modules compiled into the interpreter
# If not found anywhere -> ModuleNotFoundError

# import syntax options:
# import module_name
# from module_name import function_name
# import module_name as alias
# from math import *   <- avoid this, causes namespace pollution
#                         hard to tell where functions come from

# print(dir(math))  # shows all attributes and methods of math module

# ============================================================
# IF __NAME__ == "__MAIN__"
# ============================================================
# When a module is imported, all its code runs
# To prevent certain code from running on import, use:
# if __name__ == "__main__":
#     ...code here only runs when file is executed directly...

# Example:
# in kratim.py:
def greet(name):
    return f"Hello, {name}!"

# in main.py:
# from kratim import greet
# if __name__ == "__main__":
#     name = "Alice"
#     print(greet(name))  # runs only when main.py is run directly
#                         # not when imported as a module

# ============================================================
# LAMBDA FUNCTIONS (anonymous functions)
# ============================================================
# small, unnamed functions defined in one line
# syntax: lambda arguments: expression
# use for short, simple, throwaway functions
# avoid for complex logic - reduces readability

def double(x):
    return x * 2

# equivalent lambda
double_lambda = lambda x: x * 2
cube_lambda   = lambda x: x ** 3
avg_lambda    = lambda x, y: (x + y) / 2

print(double_lambda(5))    # 10
print(cube_lambda(3))      # 27
print(avg_lambda(10, 20))  # 15.0

# passing lambda as argument to a function
def apply_function(func, values):
    return [func(x) for x in values]

numbers = [1, 2, 3, 4, 5]
print(apply_function(lambda x: x * 2,  numbers))  # [2, 4, 6, 8, 10]
print(apply_function(lambda x: x ** 2, numbers))  # [1, 4, 9, 16, 25]

# ============================================================
# MAP, FILTER, REDUCE
# ============================================================
# higher-order functions that operate on iterables

numbers = [1, 2, 3, 4, 5]

# map() - applies function to each element, returns iterable
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)       # [2, 4, 6, 8, 10]

# filter() - keeps elements where function returns True
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

# reduce() - rolling computation on sequential pairs
# from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
print(total)         # 15

# ============================================================
# *ARGS AND **KWARGS
# ============================================================
# *args   - variable number of positional arguments (stored as tuple)
# **kwargs - variable number of keyword arguments (stored as dict)

def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)  # prints 1, 2, 3 on separate lines

def my_function2(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function2(name="Alice", age=30, city="New York")

# ============================================================
# DECORATORS
# ============================================================
# A decorator modifies a function's behavior without changing its code
# Higher-order function: takes a function, returns a new function
# Used for: logging, access control, memoization

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)  # call original with its args
        print("After the function is called.")
        return result                   # return original result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before the function is called.
# Hello!
# After the function is called.

@my_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
# Output:
# Before the function is called.
# After the function is called.
# Hello, Alice!

# ============================================================
# LOCAL AND GLOBAL VARIABLES
# ============================================================
# Local variables  - defined inside a function, only accessible there
#                    created when function is called, destroyed when it returns
# Global variables - defined outside functions, accessible everywhere
#                    created at program start, exist until program ends
# Best practice: use local variables whenever possible
# use global keyword to modify a global variable inside a function

global_variable = "I am a global variable"

def my_function3():
    global global_variable  # tells Python to use global, not create local
    global_variable = "I have been modified inside the function"

print(global_variable)  # I am a global variable
my_function3()
print(global_variable)  # I have been modified inside the function

# global variables can be useful for values needed across multiple
# functions or modules, but overusing them makes code harder to maintain
# prefer passing variables as function arguments and returning values

# ============================================================
# VIRTUAL ENVIRONMENTS
# ============================================================
# A virtual environment is a self-contained directory with a Python
# installation and packages for a specific project.
# Avoids conflicts between different projects and their dependencies.

# How to create using venv module:
# 1. Open terminal, navigate to project directory
# 2. Run: python -m venv myenv
# 3. Activate:
#    Windows:      myenv\Scripts\activate
#    Mac/Linux:    source myenv/bin/activate
# 4. Install packages: pip install package_name
#    (installs in venv, not globally)
# 5. Deactivate: deactivate

# In VS Code:
# 1. Open terminal in VS Code
# 2. python -m venv myenv
# 3. Windows: myenv\Scripts\activate

# ============================================================
# REQUIREMENTS.TXT
# ============================================================
# Lists all dependencies for a Python project with versions
# Used to reproduce the environment on a different machine

# Generate requirements.txt:
#   pip freeze > requirements.txt

# Install from requirements.txt:
#   pip install -r requirements.txt

# Example requirements.txt:
# numpy==1.21.0
# pandas==1.3.0
# scikit-learn==0.24.2

# Note: pip freeze includes ALL installed packages, not just yours
# Review and remove unnecessary ones before sharing

# ============================================================
# HIGHER ORDER FUNCTIONS
# ============================================================
# Functions that take other functions as arguments OR
# return functions as their result
# In Python, functions are first-class citizens - treated like objects
# Can be passed as arguments, returned from functions, assigned to variables
# Examples: map(), filter(), reduce(), sorted(), decorators
