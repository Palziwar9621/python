# ============================================================
# PRINT
# ============================================================
print("hello world")
# print() outputs data to the console
# can take multiple arguments separated by space by default
print("hello", "world", sep="-")   # hello-world
print("hello", end=" ")             # no newline at end
print("world")                      # prints on same line as above due to end=" "

# ============================================================
# DATA TYPES
# ============================================================
# basic types: int, float, str, bool, complex
# container types: list, tuple, set, dict
# user defined types: classes and objects

# type() checks the type of a variable or value
x = 10
print(type(x))  # <class 'int'>

# ============================================================
# COMMENTS
# ============================================================
# single line comment

"""
This is a multi line comment in python
"""

# ============================================================
# VARIABLES
# ============================================================
x = 10            # integer
y = 3.14          # float
name = "Alice"    # string
is_student = True # boolean

# multiple assignment in one line
a, b, c = 1, 2.5, "hello"

# dynamic typing - variable type can change
x = 10       # x is an integer
x = "hello"  # now x is a string (dynamic binding)

# ============================================================
# KEYWORDS
# ============================================================
# Keywords are reserved words in Python
# They have specific meaning and cannot be used as variable names
# They define the structure and syntax of the language
# Python keywords are case-sensitive - must be written in lowercase
# "if" is a keyword but "If" or "IF" would cause a SyntaxError
import keyword
print(keyword.kwlist)

# ============================================================
# IDENTIFIERS
# ============================================================
# An identifier is a name used to identify a variable, function,
# class, module, or other object.
# Rules:
# 1. Can only contain letters (a-z, A-Z), digits (0-9), underscores (_)
# 2. Cannot start with a digit
# 3. Cannot be a keyword
# 4. Case-sensitive: myVariable and myvariable are different identifiers

# ============================================================
# INPUT AND TYPE CONVERSION
# ============================================================
# input() reads a line from console and returns it as a string
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # convert input to integer

# type conversion - converting a value from one data type to another
# always ensure value is compatible to avoid errors
# trying to convert non-numeric string to int raises ValueError

# implicit type conversion (type coercion)
# Python automatically converts types when needed
x = 10      # int
y = 3.14    # float
z = x + y   # z is float because of implicit conversion

# explicit type conversion (type casting)
# manually converting using int(), float(), str(), etc.
x = "10"
y = int(x)  # string to integer
print(y)    # 10

# ============================================================
# LITERALS
# ============================================================
# A literal is a fixed value directly represented in code

integer_literal = 42
float_literal = 3.14
string_literal = "Hello, World!"
boolean_literal = True

# numeric literals in different formats
decimal_literal     = 42
binary_literal      = 0b1010
octal_literal       = 0o52
hexadecimal_literal = 0x2A

# complex literals: written as a + bj
complex_literal = 2 + 3j
print(complex_literal, complex_literal.imag, complex_literal.real)

# string literals - single, double, or triple quotes
single_quote_literal = 'Hello'
double_quote_literal = "Hello"
triple_quote_literal = '''Hello'''  # can span multiple lines
multi_line_string_literal = """This is a multi-line string literal"""
print(multi_line_string_literal)

# unicode literals - \u or \U followed by hex code point
unicode_literal = "\u03A9"  # Greek letter Omega
print(unicode_literal)  # Ω

# raw string literals - prefix r or R, backslashes treated as literal
raw_string_literal = r"C:\Users\Username\Documents"
print(raw_string_literal)  # prints backslashes literally

# boolean literals
is_raining = True
is_sunny = False

# None - represents absence of a value / null value
# used when a variable has no value or function returns nothing
result = None
