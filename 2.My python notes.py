#print 
print("hello world") # this will print "hello world" to the console
#print is a built-in function in Python that is used to output data to the console. It can take multiple arguments and will print them separated by a space by default. You can also specify a different separator using the sep parameter, and you can specify an end character using the end parameter. For example:
print("hello", "world", sep="-") # this will print "hello-world" to the console
print("hello", end=" ") # this will print "hello " to the console without a newline at the end
print("world") # this will print "world" to the console on the same line as "hello" because we specified end=" " in the previous print statement 
#data types in python
#basic types: int, float, str, bool, complex
#container types: list, tuple, set, dict
#user defined types: classes and objects
#type() function is used to check the type of a variable or value in Python. It returns the type of the object passed as an argument. For example:
x = 10
print(type(x)) # this will print <class 'int'> to the console because x is an integer
#comments in python
# single line comment
# this is a single line comment in python
# multi line comment
"""
This is a multi line comment in python
"""
#variables in python
x = 10 # this is an integer variable
y = 3.14 # this is a float variable
name = "Alice" # this is a string variable
is_student = True # this is a boolean variable
# we can also assign multiple variables in a single line    
a, b, c = 1, 2.5, "hello" # this will assign 1 to a, 2.5 to b, and "hello" to c
#dynamic typing in python
# In Python, you can change the type of a variable by assigning a new value to it. For example:
x = 10 # x is an integer
# dynamic binding allows us to change the type of a variable by assigning a new value to it
x = "hello" # now x is a string
#keywords in python
# and, as, assert, break, class, continue, def, del, elif,
# keywords are reserved words in Python that have a specific meaning and cannot be used as variable names or identifiers. They are used to define the structure and syntax of the language, and they play a crucial role in how Python code is written and executed. It is important to be familiar with the keywords in Python to avoid syntax errors and to write code that is clear and understandable.
#python keywords are case-sensitive, which means that they must be written in lowercase. For example, "if" is a keyword, but "If" or "IF" would not be recognized as a keyword and would result in a syntax error if used in the code. It is important to use the correct case when writing Python code to ensure that it is syntactically correct and functions as intended.
import keyword
print(keyword.kwlist) # this will print a list of all the keywords in Python        
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#identifiers in python
# An identifier in Python is a name used to identify a variable, function, class, module, or other object. It must follow certain rules:    
#1. An identifier can only contain letters (a-z, A-Z), digits (0-9), and underscores (_).
#2. An identifier cannot start with a digit.
#3. An identifier cannot be a keyword in Python.
#4. An identifier is case-sensitive, which means that "myVariable" and "myvariable" would be considered different identifiers.
# input and type conversion in python
name = input("Enter your name: ") # this will prompt the user to enter their name and store it in the variable name 
# The input() function in Python is used to take input from the user. It reads a line of text from the console and returns it as a string. If you want to convert the input to a different data type, you can use type conversion functions such as int(), float(), or bool(). For example: 
age = int(input("Enter your age: ")) # this will prompt the user to enter their age, convert it to an integer, and store it in the variable age
# type conversion is the process of converting a value from one data type to another. In Python, you can use built-in functions to perform type conversion. For example, you can use int() to convert a string to an integer, float() to convert a string to a float, and str() to convert a value to a string. It is important to ensure that the value being converted is compatible with the target data type to avoid errors during type conversion. For example, trying to convert a non-numeric string to an integer using int() will raise a ValueError. It is always a good practice to handle potential exceptions that may arise during type conversion to ensure that your code is robust and can handle unexpected input gracefully.
# implicit type conversion, also known as type coercion, is the automatic conversion of one data type to another by the Python interpreter when performing operations that involve different data types. For example, if you add an integer and a float together, Python will automatically convert the integer to a float before performing the addition. This allows for seamless operations between different data types without requiring explicit type conversion by the programmer. However, it is important to be aware of implicit type conversion and how it may affect the behavior of your code, especially when working with mixed data types, to avoid unintended consequences or errors.
# for example:
x = 10 # x is an integer
y = 3.14 # y is a float
z = x + y # z will be a float because of implicit type conversion
# explicit type conversion, also known as type casting, is the process of manually converting a value from one data type to another using built-in functions in Python. For example, you can use int() to convert a string to an integer, float() to convert a string to a float, and str() to convert a value to a string. Explicit type conversion allows you to control the data types of your variables and ensure that they are compatible with the operations you want to perform. It is important to use explicit type conversion when necessary to avoid errors and ensure that your code behaves as expected.
# for example:
x = "10" # x is a string
y = int(x) # y will be an integer because of explicit type conversion
print(y) # this will print 10 to the console
# literals in python
# A literal in Python is a fixed value that is directly represented in the code. It can be of various data types, such as integers, floats, strings, booleans, and more. For example:
integer_literal = 42 # this is an integer literal
float_literal = 3.14 # this is a float literal
string_literal = "Hello, World!" # this is a string literal
boolean_literal = True # this is a boolean literal
# numeric literals can be written in different formats, such as decimal, binary, octal, and hexadecimal. For example:
decimal_literal = 42
binary_literal = 0b1010
octal_literal = 0o52
hexadecimal_literal = 0x2A
#complex literals are written in the form of a + bj, where a is the real part and b is the imaginary part. For example:
complex_literal = 2 + 3j
print(complex_literal,complex_literal.imag,complex_literal.real) # this will print (2+3j) to the console and 3.0 and 2.0 respectively
#string literals can be enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """). For example:   
single_quote_literal = 'Hello'
double_quote_literal = "Hello"
triple_quote_literal = '''Hello''' # this is a triple quote literal that can span multiple lines
#multiple line string literals can be created using triple quotes. For example:
multi_line_string_literal = """This is a multi-line string literal"""
print(multi_line_string_literal) # this will print the multi-line string to the console
#unicode literals are written using the \u or \U escape sequences followed by the hexadecimal code point of the character. For example:
unicode_literal = "\u03A9" # this is a unicode literal for the Greek letter Omega
print(unicode_literal) # this will print Ω to the console
# raw string literals are prefixed with an 'r' or 'R' and treat backslashes as literal characters. For example:
raw_string_literal = r"C:\Users\Username\Documents" # this is a raw string literal that will treat backslashes as literal characters
print(raw_string_literal) # this will print C:\Users\Username\Documents to the console without interpreting the backslashes as escape characters
#boolean literals are simply the values True and False, which represent the two possible states of a boolean variable. For example: 
is_raining = True # this is a boolean literal representing the state of raining
is_sunny = False # this is a boolean literal representing the state of sunny
# None is a special literal in Python that represents the absence of a value or a null value. It is often used to indicate that a variable has no value or that a function does not return anything. For example:
result = None # this is a None literal representing the absence of a value
# operators in python
# arithmetic operators: +, -, *, /, %, **, //
#** is the exponentiation operator, which raises the left operand to the power of the right operand. For example:
x = 2
y = 3
z = x ** y # z will be 8 because 2 raised to the power of 3 is 8
#// is the floor division operator, which performs integer division and returns the largest integer less than or equal to the result. For example:
x = 7
y = 3
z = x // y # z will be 2 because 7 divided by 3 is 2.333... and the floor division operator returns the largest integer less than or equal to that result, which is 2
# comparison operators: ==, !=, >, <, >=, <=
# logical operators: and, or, not
# assignment operators: =, +=, -=, *=, /=, %=, **=, //=
# bitwise operators: &, |, ^, ~, <<, >>
#bitwise operators are used to perform bitwise operations on integers. For example:
x = 5 # in binary: 0101
y = 3 # in binary: 0011
z = x & y # z will be 1 because 0101 & 0011 is 0001(and)
z = x | y # z will be 7 because 0101 | 0011 is 0111(or)
z = x ^ y # z will be 6 because 0101 ^ 0011 is 0110(xor)
z = ~x # z will be -6 because ~0101 is 1010 in two's complement representation, which is -6 in decimal (not)
z = x << 1 # z will be 10 because 0101 << 1 is 1010(left shift)
z = x >> 1 # z will be 2 because 0101 >> 1 is 0010(right shift)
# membership operators: in, not in
# membership operators are used to test if a value is present in a sequence (such as a list, tuple, or string) or not. For example:
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # this will print True because "banana" is in the fruits list
print("grape" in fruits) # this will print False because "grape" is not in the fruits list

# identity operators: is, is not
# identity operators are used to compare the memory locations of two objects. The is operator returns True if both operands refer to the same object in memory, while the is not operator returns True if both operands do not refer to the same object in memory. For example:
a = [1, 2, 3]
b = a
print(a is b) # this will print True because both a and b refer to the same object in memory
print(a is not b) # this will print False because both a and b refer to the same object in memory   
c = [1, 2, 3]
print(a is c) # this will print False because a and c refer to different objects in memory, even though they have the same content
# operator precedence in python
# precedence order: 1. (), 2. **, 3. +x, -x, 4. *, /, //, %, 5. +, -, 6. <<, >>, 7. &, 8. ^, 9. |, 10. comparison operators, 11. not, 12. and, 13. or
# if else statements in python
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
# nested if else statements in python
x = 10
if x > 5:
    if x < 15:
        print("x is between 5 and 15")
    else:
        print("x is greater than or equal to 15")
else:
    print("x is less than or equal to 5")
#else if statements in python
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
else:
    print("x is less than or equal to 5")
#indentation in python
# In Python, indentation is used to define the scope of loops, functions, and other code blocks. It is important to use consistent indentation throughout your code to avoid syntax errors. The standard practice is to use four spaces for each level of indentation. For example:
if x > 5:
    print("x is greater than 5") # this line is indented with four spaces and is part of the if block   
else:
    print("x is not greater than 5") # this line is indented with four spaces and is part of the else block 
#while loop in python
i = 0
while i < 5:
    print(i)
    i += 1
# guessing game using while loop and if else statements
import random
number_to_guess = random.randint(1, 100)
guess=int(input("Guess a number between 1 and 100: "))
guess_times=1
while guess != number_to_guess:
    if number_to_guess < guess:
        print("higer,try lower")
    else:
        print("lower, try higher")
    guess_times+=1
    guess=int(input("Guess a number between 1 and 100: "))
print(f"Congratulations! You guessed the number in {guess_times} attempts.")
#for loop in python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# range function in python
range(0,5) # this will create a range object that represents the sequence of numbers from 0 to 4
list(range(15)) # this will create a list of numbers from 0 to 14
range(1,11,2) # this will create a range object that represents the sequence of odd numbers from 1 to 10
list(range(1,11,2)) # this will create a list of odd numbers from 1 to 10
# sequences in python
["apple", "banana", "cherry"] # this is a list, which is a mutable sequence in Python
("apple", "banana", "cherry") # this is a tuple, which is an immutable sequence in Python
#for loop in python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# you can use for with range, strings, lists, tuples, dictionaries, sets, and other iterable objects in Python. For example:
for i in range(5):
    print(i) # this will print the numbers from 0 to 4 to the console
for char in "hello":
    print(char) # this will print each character in the string "hello" to the console
for key in {"name": "Alice", "age": 30}:
    print(key) # this will print the keys of the dictionary to the console  
for value in {"name": "Alice", "age": 30}.values():
    print(value) # this will print the values of the dictionary to the console
for item in {1, 2, 3}:
    print(item) # this will print each item in the set to the console
# nested loops in python
rows=int(input("enter number of rows:"))
for i in range(1,rows+1):
    for j in range(0,i):
        print("*",end="")
    print() # this will print a new line after each row of stars
    print(i) # this will print the numbers from 0 to 4 to the console
# in real life world, loop is used to perform a task repeatedly until a certain condition is met. For example, you might use a loop to process a list of items, to read data from a file, or to perform a calculation until a specific result is achieved. Loops are an essential part of programming and allow us to automate repetitive tasks and work with large amounts of data efficiently.
# for example, you might use loop to make containers on online shopping sites to display products, to read data from a database, or to perform calculations for each item in a list. Loops are a fundamental concept in programming and are used in a wide variety of applications to automate tasks and process data efficiently.
# break statement in python
for i in range(10):
    if i == 5:
        break # this will exit the loop when i is equal to 5
#break can be used in linear search algorithm to exit the loop when the target element is found, which can improve the efficiency of the search by avoiding unnecessary iterations through the remaining elements in the list. For example:
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i # return the index of the target element
    return -1 # return -1 if the target element is not found
# continue statement in python
for i in range(10):
    if i == 5:
        continue # this will skip the rest of the loop body when i is equal to 5    
    print(i) # this will print the numbers from 0 to 9 to the console, except for 5
#continue can be used in a loop to skip the current iteration and move on to the next one. For example, you might use continue in a loop that processes a list of items to skip over any items that do not meet a certain condition, allowing you to focus on processing only the relevant items in the list. This can help improve the efficiency of your code by avoiding unnecessary processing of irrelevant items. For example:
def process_items(items):
    for item in items:
        if not is_relevant(item):
            continue # skip processing this item if it is not relevant
        # process the relevant item here
        print(item)
# pass statement in python
for i in range(10):
    if i == 5:
        pass # this will do nothing when i is equal to 5
    print(i) # this will print the numbers from 0 to 9 to the console, including 5
# pass can be used as a placeholder in a loop or function definition when you want to define the structure of your code but have not yet implemented the logic. It allows you to write syntactically correct code without having to fill in the details immediately, which can be useful during the development process when you are still working on the overall design of your code.
#built in functions in python
# len() function is used to get the length of a sequence (such as a string, list, or tuple) or a collection (such as a dictionary or set). For example:
length = len("Hello, World!") # returns 13
length = len([1, 2, 3, 4, 5]) # returns 5
length = len({1, 2, 3}) # returns 3
# print, input, type, int,
#abs() function is used to get the absolute value of a number. For example:
absolute_value = abs(-5) # returns 5
# pow function is used to calculate the power of a number. For example:
power = pow(2, 3) # returns 8 because 2 raised to the power of 3 is 8
# min/max function is used to get the minimum or maximum value from a sequence of numbers. For example:
minimum = min(1, 2, 3) # returns 1
maximum = max("kolkata") # returns "t" because it is the maximum character in the string based on ASCII values
#round function is used to round a number to a specified number of decimal places. For example:
rounded_value = round(3.14159, 2) # returns 3.14 because it rounds the number to 2 decimal places
#divmod function is used to get the quotient and remainder of a division operation. For example:
quotient, remainder = divmod(10, 3) # returns (3, 1) because 10 divided by 3 is 3 with a remainder of 1
#bin/oct/hex functions are used to convert an integer to its binary, octal, or hexadecimal representation. For example:
binary_representation = bin(10) # returns '0b1010' because 10 in binary is 1010
octal_representation = oct(10) # returns '0o12' because 10 in octal is 12
hexadecimal_representation = hex(10) # returns '0xa' because 10 in hexadecimal is a
#id function is used to get the memory address of an object. For example:
x = 10
id(x) # this will return the memory address of the integer object 10 in Python, which is a unique identifier for that object in memory. The id() function can be useful for understanding how objects are stored and referenced in Python, especially when working with mutable and immutable data types.
#ord function is used to get the ASCII value of a character. For example:
ascii_value = ord('A') # returns 65 because the ASCII value of 'A' is 65
#sum function is used to get the sum of a sequence of numbers. For example:
total = sum([1, 2, 3, 4, 5]) # returns 15 because the sum of the numbers in the list is 15
# help function is used to get the documentation of a function, class, or module. For example:
help(len) # this will display the documentation for the len() function in the console
#built in modules in python
#Modules are pre-written code that you can use in your Python programs to perform specific tasks. They are organized into libraries and can be imported into your code using the import statement. Some commonly used built-in modules in Python include:
# math module: provides mathematical functions and constants
import math
print(math.sqrt(16)) # this will print 4.0 to the console because the square root of 16 is 4
# random module: provides functions for generating random numbers and performing random operations
import random
print(random.randint(1, 10)) # this will print a random integer between 1 and 10 to the console
random.shuffle([1, 2, 3, 4, 5]) # this will shuffle the list [1, 2, 3, 4, 5] in place and return None 
# time module: provides functions for working with time and dates
import time
print(time.time()) # this will print the current time in seconds since the epoch (January 1, 1970) to the console
#os module: provides functions for interacting with the operating system
import os
print(os.getcwd()) # this will print the current working directory to the console
#string in python
# A string in Python is a sequence of Unicode characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """). Strings are immutable, which means that once a string is created, it cannot be modified. You can perform various operations on strings, such as concatenation, slicing, and formatting.
# creating strings in python
string1 = 'Hello, World!' # using single quotes
string2 = "Hello, World!" # using double quotes
string3 = '''Hello, World!''' # using triple quotes, for multi-line strings
string4 = """Hello, World!""" # using triple quotes, for multi-line strings
#accessing characters in a string
print(string1[0]) # this will print the first character of string1, which is 'H'
print(string1[-1]) # this will print the last character of string1, which is '!'
#slicing strings in python
print(string1[0:5]) # this will print the substring 'Hello' from string1
print(string1[0:12:2]) # this will print the substring 'Hlo ol' from string1 by slicing every second character
print(string1[::-1]) # this will print the reverse of string1, which is '!dlroW ,olleH'
#editing and deleting strings in python
# since strings are immutable in Python, you cannot edit or delete individual characters in a string. However, you can create a new string by concatenating parts of the original string or by using string methods to modify the string. For example:
string1 = "Hello, World!"
string2 = string1[:5] + " Python!" # this will create a new string 'Hello Python!' by concatenating the first 5 characters of string1 with the new substring ' Python!'
del string1 # this will delete the string1 variable from memory
# operations on strings in python
string1 = "Hello, World!"
string2 = "Python is great!"
#arithmetic operations on strings
concatenated_string = string1 + " " + string2 # this will concatenate string1 and string2 with a space in between
print(concatenated_string) # this will print 'Hello, World! Python is great!' to the console
print(string1 * 3) # this will print 'Hello, World!Hello, World!Hello, World!' to the console by repeating string1 three times
#relational operations on strings
print(string1 == string2) # this will print False because string1 and string2 are not equal
print(string1 != string2) # this will print True because string1 and string2 are not equal
print(string1 > string2) # this will print False because string1 is not greater than string2 based on lexicographical order
print(string1 < string2) # this will print True because string1 is less than string2 based on lexicographical order
#membership operations on strings
print("Hello" in string1) # this will print True because the substring "Hello" is present in string1
print("Python" in string1) # this will print False because the substring "Python" is not present in string1
#logical operations on strings
"hello" and "world" # this will not work because "hello" and "world" are not boolean values, they are strings. Logical operations like 'and' and 'or' are used with boolean values (True or False) to perform logical operations. For example:
"" or "world" # this will return "world" because the empty string "" is considered False in a boolean context, so the 'or' operator returns the second operand "world" which is considered True
"hello" or "" # this will return "hello" because the 'or' operator returns the first operand "hello" which is considered True, and it does not evaluate the second operand "" since the first operand is already True
not "hello" # this will return False because the 'not' operator negates the truth value of the operand, and since "hello" is considered True in a boolean context, 'not "hello"' will return False
not "" # this will return True because the 'not' operator negates the truth value of the operand, and since the empty string "" is considered False in a boolean context, 'not ""' will return True
#loops with strings in python
string1 = "Hello, World!"
for char in string1:
    print(char) # this will print each character in string1 on a new line
#string methods in python
string1 = "Hello, World!"
#common functions
print(len(string1)) # this will print the length of string1, which is 13
max(string1) # this will print the maximum character in string1 based on ASCII values, which is 'r'
min(string1) # this will print the minimum character in string1 based on ASCII values, which is ' '
sorted_string = sorted(string1) # this will return a list of characters in string1 sorted in ascending order based on ASCII values
print(sorted_string) # this will print the sorted list of characters to the console

#string methods
print(string1.upper()) # this will print 'HELLO, WORLD!' to the console by converting all characters in string1 to uppercase
print(string1.lower()) # this will print 'hello, world!' to the console by converting   all characters in string1 to lowercase
print(string1.title()) # this will print 'Hello, World!' to the console by converting the first character of each word in string1 to uppercase and the rest to lowercase
print(string1.capitalize()) # this will print 'Hello, world!' to the console by converting the first character of string1 to uppercase and the rest to lowercase
print(string1.strip()) # this will print 'Hello, World!' to the console by removing any leading and trailing whitespace from string1
print(string1.replace("Hello", "Hi")) # this will print 'Hi, World!' to the console by replacing the substring "Hello" with "Hi" in string1
print(string1.split(", ")) # this will print ['Hello', 'World!'] to the console by splitting string1 into a list of substrings based on the delimiter ", "
print(string1.join(["Hello", "World"])) # this will print 'HelloHello, World!World' to the console by joining the list of strings ["Hello", "World"] with string1 as the separator
print(string1.find("World")) # this will print 7 to the console because the substring "World" starts at index 7 in string1
print(string1.index("World")) # this will also print 7 to the console because the substring "World" starts at index 7 in string1, but it will raise a ValueError if the substring is not found, while find() will return -1
print(string1.count("o")) # this will print 2 to the console because the character "o" appears twice in string1
print(string1.startswith("Hello")) # this will print True because string1 starts with the substring "Hello"
print(string1.endswith("!")) # this will print True because string1 ends with the character "!"
#format method in python
name = "Alice"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.") # this will print 'Hello, my name is Alice and I am 30 years old.' to the console by using f-string formatting to insert the values of name and age into the string
print(string1.isalpha()) # this will print False because string1 contains characters that are not alphabetic (such as the comma and space)
print(string1.isdigit()) # this will print False because string1 contains characters that are not digits (such as the letters and punctuation)
print(string1.isalnum()) # this will print False because string1 contains characters that are not alphanumeric (such as the comma and space)
print(string1.isspace()) # this will print False because string1 contains characters that are not whitespace (such as the letters and punctuation)
print(string1.islower()) # this will print False because string1 contains characters that are not lowercase (such as the uppercase letters)
print(string1.isupper()) # this will print False because string1 contains characters that are not uppercase (such as the lowercase letters)
print(string1.istitle()) # this will print False because string1 does not have the first character of each word in uppercase and the rest in lowercase (the comma and space are not considered as part of the words)
#lists in python
# A list in Python is a mutable, ordered collection of items that can contain elements of different data types. Lists are defined using square brackets [] and can be modified after creation.
#1. array homogenous, list heterogenous
#2. Array stores data
# list 
#  For example:
my_list = [1, 2, 3, "hello", True] # this creates a list with the elements 1, 2, 3, "hello", and True
print(my_list) # this will print the entire list to the console
my_list[0] # this will print the first element of the list, which is 1
my_list[-1] # this will print the last element of the list, which is True
my_list[1:4] # this will print the sublist [2, 3, "hello"] from the list by slicing it from index 1 to index 3 (index 4 is not included)
my_list[::-1] # this will print the reverse of the list, which is [True, "hello", 3, 2, 1]
L=[1,2,"lol",[4,5]]
x=L[3][0] # this will print 4 because L[3] is the sublist [4, 5] and L[3][0] is the first element of that sublist, which is 4
L1=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
x=L1[0][1][0] # this will print 4 because L1[0] is the first element of L1, which is [[1, 2, 3], [4, 5, 6]], L1[0][1] is the second element of that sublist, which is [4, 5, 6], and L1[0][1][0] is the first element of that sublist, which is 4
#lists are mutable, which means you can change their content after they have been created. For example:
my_list = [1, 2, 3]
my_list[0] = 10 # this will change the first element of the list to 10
print(my_list) # this will print [10, 2, 3] to the console
my_list[1:4] = [20, 30, 40] # this will change the sublist from index 1 to index 3 to [20, 30, 40]
print(my_list) # this will print [10, 20, 30, 40] to the console
my_list.append(50) # this will add the element 50 to the end of the list, it adds only 1 item to the list
print(my_list) # this will print [10, 20, 30, 40, 50] to the console
my_list.extend([60, 70]) # this will add the elements 60 and 70 to the end of the list by extending the list with another iterable, it adds multiple items to the list
print(my_list) # this will print [10, 20, 30, 40, 50] to the console
my_list.insert(1, 15) # this will insert the element 15 at index 1 in the list
print(my_list) # this will print [10, 15, 20, 30, 40, 50] to the console
my_list.remove(20) # this will remove the first occurrence of the element 20 from the list
print(my_list) # this will print [10, 15, 30, 40, 50] to the console
my_list.pop() # this will remove and return the last element of the list, which is 50
print(my_list) # this will print [10, 15, 30, 40] to the console
my_list.pop(1) # this will remove and return the element at index 1 of the list, which is 15
print(my_list) # this will print [10, 30, 40] to the console
print(my_list) # this will print [] to the console
del my_list[0] # this will delete the element at index 0 of the list, which is 10
print(my_list) # this will print [30, 40] to the console
del my_list # this will delete the list variable from memory
my_list = [1, 2, 3]
my_list.clear() # this will remove all elements from the list, leaving it empty
print(my_list) # this will print [] to the console
# operations on lists in python
my_list = [1, 2, 3]
my_list + [4, 5] # this will return a new list [1, 2, 3, 4, 5] by concatenating my_list with another list [4, 5]
my_list * 2 # this will return a new list [1, 2, 3, 1, 2, 3] by repeating my_list twice
for item in my_list:
    print(item) # this will print each item in my_list on a new line
4 in my_list # this will return True because the element 4 is present in my_list
5 not in my_list # this will return True because the element 5 is not present in my_list
# functions on lists in python
len(my_list) # this will return the length of my_list, which is 3
max(my_list) # this will return the maximum element in my_list, which is 3
min(my_list) # this will return the minimum element in my_list, which is 1
sorted_list = sorted(my_list) # this will return a new list [1, 2, 3] which is the sorted version of my_list
sorted_list_descending = sorted(my_list, reverse=True) # this will return a new list [3, 2, 1] which is the sorted version of my_list in descending order   
my_list.sort() # this will sort my_list in place, changing it to [1, 2, 3]
my_list.sort(reverse=True) # this will sort my_list in place in descending order, changing it to [3, 2, 1]
my_list.reverse() # this will reverse the order of the elements in my_list in place, changing it to [1, 2, 3]
my_list.index(2) # this will return the index of the first occurrence of the element 2 in my_list, which is 1
my_list.count(2) # this will return the number of occurrences of the element 2





# sets in python
my_set = {1, 2, 3} # this creates a set with the elements 1, 2, and 3
cities={"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","madrid","kabul","seoul"}
cities3=cities.union(cities2) #union of 2 sets
cities4=cities.intersection(cities2) #intersection of a set
cities6=cities.symmetric_difference_update(cities2) # update a set with the symmetric difference of itself and another
cities7=cities.difference(cities2) # difference of 2 sets 
cities8=cities.difference_update(cities2) # update a set with the difference of itself and another
#set methods
cities.add("paris") # add an element to a set
cities.remove("paris") # remove an element from a set
cities.discard("paris") # remove an element from a set if it is a member and it raises a error if not present
del cities # delete a set
try:
    cities.pop() # remove and return an arbitrary set element
except KeyError:
    print("the set is empty")
cities.clear() # remove all elements from a set
cities.isdisjoint(cities2) # return True if two sets have a null intersection
cities.issubset(cities2) # return True if another set contains this set
cities.issuperset(cities2) # return True if this set contains another set
cities.copy() # return a shallow copy of a set
cities.update(cities2) # update a set with the union of itself and another
cities5=cities.intersection_update(cities2) # update a set with the intersection of itself and another 
#dictionaries are unordered, changeable and indexed collections. They are written with curly brackets, and they have keys and values.
person={"name":"john","age":30,"city":"new york"}
print(person) # print the entire dictionary
print(person["name"]) # print the value of a specific key
print(person.get("age")) # print the value of a specific key using get method
print(person["age1"])# it throws a KeyError because the key "age1" does not exist in the dictionary
#acessing values in a dictionary using get method does not throw an error if the key does not exist, it returns None instead
print(person.get("age1")) # it returns None because the key "age1" does
print(person.keys()) # print all the keys in the dictionary
print(person.values()) # print all the values in the dictionary
for key in person.keys(): # iterate through the keys in the dictionary using keys method
    print(key)
    print(f"the value of {key} is {person[key]}") # print the value of each key
#for and while loop with else
for i in range(5):
    print(i)
else:
    print("loop is finished")
while i < 5:
    print(i)
    i += 1  
else:
    print("while loop is finished")
# exception handling
try:
    print(10/0) # this will raise a ZeroDivisionError   
except ZeroDivisionError: # zerodivisionerror is the type of error that we want to handle
    print("you cannot divide by zero") # this will be executed if a ZeroDivisionError is raised
#finally block is used to execute code regardless of whether an exception is raised or not
finally:
    print("this will be executed regardless of whether an exception is raised or not") # this will be executed regardless of whether an exception is raised or not
 
# we can directly execute code without using using finally block but we use it because during using functions we want to execute some code after the function is executed regardless of whether an exception is raised or not and it can only be done by finally block
# Raising exceptions
def divide(a,b):
    if b == 0:
        raise ValueError("you cannot divide by zero") # this will raise a ValueError if b is zero
    return a/b
#error types
#SyntaxError: this error occurs when there is a syntax error in the code
#NameError: this error occurs when a variable is not defined  
#TypeError: this error occurs when an operation is performed on a wrong data type
#IndexError: this error occurs when an index is out of range
#KeyError: this error occurs when a key is not found in a dictionary
#AttributeError: this error occurs when an attribute is not found in an object
#ValueError: this error occurs when a function receives an argument of the correct type but an inappropriate value
#FileNotFoundError: this error occurs when a file is not found
#ZeroDivisionError: this error occurs when a number is divided by zero
#ImportError: this error occurs when a module is not found
#ModuleNotFoundError: this error occurs when a module is not found
#IndentationError: this error occurs when there is an indentation error in the code
#TabError: this error occurs when there is a tab error in the code
#StopIteration: this error occurs when there are no more items to iterate over
#GeneratorExit: this error occurs when a generator is closed
#KeyboardInterrupt: this error occurs when the user interrupts the program by pressing Ctrl+C
#SystemExit: this error occurs when the program is exited
#MemoryError: this error occurs when there is not enough memory to perform an operation
#OverflowError: this error occurs when the result of an arithmetic operation is too large to be represented
#RecursionError: this error occurs when the maximum recursion depth is exceeded
#AssertionError: this error occurs when an assert statement fails
#StopAsyncIteration: this error occurs when there are no more items to iterate over in an asynchronous iterator
#Warning: this is not an error but a warning that something might be wrong in the code
#DeprecationWarning: this warning is raised when a feature is deprecated and will be removed
#SyntaxWarning: this warning is raised when there is a syntax warning in the code
#RuntimeWarning: this warning is raised when there is a runtime warning in the code
#FutureWarning: this warning is raised when a feature will be changed in the future
#ImportWarning: this warning is raised when there is an import warning in the code
#UnicodeWarning: this warning is raised when there is a unicode warning in the code
#BytesWarning: this warning is raised when there is a bytes warning in the code
#ResourceWarning: this warning is raised when there is a resource warning in the code
#DeprecationWarning: this warning is raised when a feature is deprecated and will be removed in the future
#custom exceptions
class CustomError(Exception):
    pass
# we can raise a custom exception by creating a class that inherits from the Exception class and then raising an instance of that class
def custom_function():
    raise CustomError("this is a custom error") # this will raise a CustomError with the message "this is a custom error"
#short hand if else
x=10
y=20
z = x if x > y else y
print(z)
# we use short hand if else to assign a value to a variable based on a condition in a single line of code. In this example, z will be assigned the value of x if x is greater than y, otherwise it will be assigned the value of y.
# we use to assign a value to a variable based on a condition in a single line of code. In this example, z will be assigned the value of x if x is greater than y, otherwise it will be assigned the value of y.
# but it is not recommended to use short hand if else for complex conditions as it can make the code less readable. It is better to use regular if else statements for complex conditions to improve readability.
#enumerate function
fruits=["apple","banana","cherry"]
for index, fruit in enumerate(fruits):
    print(f"the index of {fruit} is {index}")
# we use the enumerate function to get the index and value of each item in a list. In this example, the index of "apple" is 0, the index of "banana" is 1, and the index of "cherry" is 2. The enumerate function returns a tuple containing the index and value of each item in the list, which we can unpack into the variables index and fruit in the for loop.
for index, fruit in enumerate(fruits, start=1):
    print(f"the index of {fruit} is {index}")
# we can also specify a starting index for the enumerate function using the start parameter. In this example, the index of "apple" is 1, the index of "banana" is 2, and the index of "cherry" is 3. The start parameter allows us to specify a different starting index for the enumeration, which can be useful in certain situations where we want to start counting from a different number.
# virtual environments
# a virtual environment is a self-contained directory that contains a Python installation for a particular version of
#Python, plus a number of additional packages. It allows you to create an isolated environment for your Python projects, which can help to avoid conflicts between different projects and their dependencies. You can create a virtual environment using the venv module in Python 3, or using third-party tools like virtualenv or conda. Once you have created a virtual environment, you can activate it and install packages specific to that environment without affecting other projects on your system.
#how to create a virtual environment using venv module
#1. Open a terminal and navigate to the directory where you want to create the virtual environment
#2. Run the command: python -m venv myenv (replace "myenv" with the name you want to give to your virtual environment)
#3. Activate the virtual environment:
# On Windows: myenv\Scripts\activate
#how to create a virtual environment using venv module in vscode
#1. Open a terminal in VS Code and navigate to the directory where you want to create the virtual environment
#2. Run the command: python -m venv myenv (replace "myenv" with the name you want to give to your virtual environment)
#3. Activate the virtual environment:
# On Windows: myenv\Scripts\activate
# On macOS/Linux: source myenv/bin/activate
# Once the virtual environment is activated, you can install packages using pip and they will be installed in the virtual environment rather than globally on your system. This allows you to manage dependencies for each project separately and avoid conflicts between different projects.
# To deactivate the virtual environment, simply run the command: deactivate
# In summary, virtual environments are a powerful tool for managing dependencies and creating isolated environments for your Python projects. They allow you to avoid conflicts between different projects and their dependencies, and make it easier to manage your Python environment. By using virtual environments, you can ensure that your projects are reproducible and that you can easily share them with others without worrying about dependency issues.
#(venv) C:\Users\username\project> python -m venv myenv
#(venv) C:\Users\username\project> myenv\Scripts\activate
#(myenv) C:\Users\username\project> pip install package_name
#requirements.txt
# A requirements.txt file is a text file that lists the dependencies for a Python project. It typically contains a list of package names and their corresponding versions, which can be installed using pip. The requirements.txt file is commonly used to manage dependencies for a project and ensure that all necessary packages are installed when setting up the project on a new environment or sharing it with others. To create a requirements.txt file, you can use the command: pip freeze > requirements.txt, which will generate a list of all installed packages and their versions in the current environment. To install the dependencies listed in a requirements.txt file, you can use the command: pip install -r requirements.txt. This will read the file and install all the packages specified in it.
#Example of a requirements.txt file:
#numpy==1.21.0
#pandas==1.3.0
#scikit-learn==0.24.2
#In this example, the requirements.txt file lists three packages: numpy, pandas, and scikit-learn, along with their specific versions. When you run the command pip install -r requirements.txt, it will install these packages with the specified versions in your environment. This helps to ensure that your project has the correct dependencies and can be easily set up on different machines or environments.
# In summary, a requirements.txt file is a crucial part of managing dependencies for a Python project. It allows you to specify the packages and their versions that your project relies on, making it easier to set up the project in different environments and share it with others without worrying about missing dependencies or version conflicts.
#pip freeze > requirements.txt
#pip install -r requirements.txt
#it is important to note that when you use pip freeze to generate a requirements.txt file, it will include all the packages installed in your current environment, including those that may not be necessary for your project. Therefore, it is a good practice to review the generated requirements.txt file and remove any unnecessary packages before sharing it or using it to set up a new environment. This helps to keep the dependencies for your project clean and focused on what is actually needed for the project to run successfully.
#how importing modules works in python
# In Python, you can import modules using the import statement. When you import a module, Python searches for the module in a specific order:
#1. The current directory: Python first looks for the module in the current working directory.  
#2. The standard library: If the module is not found in the current directory, Python looks for it in the standard library, which is a collection of modules that come with Python.
#3. The site-packages directory: If the module is not found in the standard library, Python looks for it in the site-packages directory, which is where third-party packages are installed.
#4. The PYTHONPATH environment variable: If the module is not found in the site-packages directory, Python looks for it in the directories specified in the PYTHONPATH environment variable.
#5. The built-in modules: If the module is not found in any of the above locations, Python looks for it in the built-in modules, which are modules that are compiled into the Python interpreter.
# If the module is not found in any of these locations, Python raises a ModuleNotFoundError. To avoid this error, you can ensure that the module you want to import is in one of the locations mentioned above or that the PYTHONPATH environment variable is set correctly to include the directory where the module is located. Additionally, you can use virtual environments to manage your dependencies and ensure that the necessary modules are available for your project.
# from module_name import function_name
# import module_name as alias
# from math import *
#but it is not recommended to use from module_name import * as it can lead to namespace pollution and make it difficult to identify where a particular function or variable is coming from. It is better to import only the specific functions or variables that you need from a module, or to use an alias for the module to avoid conflicts with other modules or variables in your code. This helps to improve code readability and maintainability.
#import math
#print(Dir(math)) # this will print all the attributes and methods of the math module
#In kratim.py
def greet(name):
    return f"Hello, {name}!"
#in main.py
#from kratim import greet
#if__name__=="__main__":
#when we import a module, the code in that module is executed. However, if we want to prevent certain code from being executed when the module is imported, we can use the if __name__ == "__main__": condition. This condition checks if the module is being run directly (as the main program) or if it is being imported as a module in another script. If the module is being run directly, the code inside the if block will be executed. If the module is being imported, the code inside the if block will not be executed. This allows us to include test code or code that should only be executed when the script is run directly without affecting other scripts that import the module.                             
    # this code will only be executed if the script is run directly, and not imported as a module
    # it is a common practice to use this condition to include code that should only be executed when the script is run directly, such as test code or code that should not be executed when the script is imported as a module in another script. This helps to prevent unintended side effects when importing the script as a module and allows for better organization of code.
#in kratim,py 
def greet(name):
    return f"Hello, {name}!"
#in main.py
from kratim import greet # type: ignore # this will import the greet function from the kratim module and it will be executed when main.py is run directly, but it will not be executed when main.py is imported as a module in another script. This allows us to use the greet function in other scripts without executing the code that is meant to be run only when main.py is executed directly.
if __name__ == "__main__":
    name = "Alice"
    print(greet(name)) # this will print "Hello, Alice!" when main.py is run directly
#os module
# The os module in Python provides a way to interact with the operating system. It allows you to perform various operations such as creating, deleting, and manipulating files and directories, as well as accessing environment variables and executing system commands. Some common functions in the os module include:
#os.getcwd(): returns the current working directory
#os.listdir(path): returns a list of files and directories in the specified path
#os.mkdir(path): creates a new directory at the specified path
#os.remove(path): removes the file at the specified path
#os.rmdir(path): removes the directory at the specified path (only if it is empty
#os.path.join(path1, path2): joins two paths together
#os.path.exists(path): returns True if the specified path exists, False otherwise
#os.path.isfile(path): returns True if the specified path is a file, False otherwise
#os.path.isdir(path): returns True if the specified path is a directory, False otherwise
#os.environ: a dictionary containing the environment variables
#os.system(command): executes the specified system command
#os.path: a module that provides functions for working with file paths
#os.path.basename(path): returns the base name of the specified path
#os.path.dirname(path): returns the directory name of the specified path
#os.path.splitext(path): splits the specified path into a tuple containing the root and extension
#os.path.abspath(path): returns the absolute path of the specified path
#os.path.relpath(path, start): returns the relative path from the start directory to the specified path
#os.path.normpath(path): normalizes the specified path by collapsing redundant separators and up-level references
#os.rename(src, dst): renames the file or directory from src to dst
#os.walk(top, topdown=True, onerror=None, followlinks=False): generates the file names in a directory tree by walking the tree either top-down or bottom-up
# The os module is a powerful tool for working with the operating system and can be used to perform a wide range of tasks related to file and directory management, environment variables, and system commands. It is an essential module for any Python programmer who needs to interact with the operating system in their code.
#read more about os module in python documentation: https://docs.python.org/3/library/os.html
import os
if (not os.path.exists("data")): # this will check if the data directory exists or not
    os.mkdir("data") # this will create a data directory if it does not exist
for i in range(0,100):
    os.mkdir(f"data/day{i+1}") # this will create directories named day1, day2, day3, day4, and day5 in the data directory
#local variables and global variables
#Local variables are variables that are defined inside a function and can only be accessed within that function. They are created when the function is called and destroyed when the function returns.
#Global variables, on the other hand, are variables that are defined outside of any function and can be accessed from anywhere in the code. They are created when the program starts and exist until the program ends. It is generally recommended to use local variables whenever possible to avoid unintended side effects and improve code readability, while global variables should be used sparingly and with caution to prevent conflicts and maintainability issues in larger codebases.
# In Python, you can use the global keyword to indicate that a variable is global and should be accessed from the global scope. This allows you to modify the value of a global variable from within a function. However, it is important to use the global keyword judiciously, as it can lead to code that is difficult to understand and maintain if overused. It is generally better to pass variables as arguments to functions or return values from functions rather than relying on global variables, as this promotes better encapsulation and makes the code more modular and easier to test.
# example of using global variables
# global_variable = "I am a global variable"
# def my_function():
#   global global_variable
#  global_variable = "I have been modified inside the function"
# print(global_variable) # this will print "I am a global variable"
# my_function()
# print(global_variable) # this will print "I have been modified inside the function" because we modified the global variable inside the function using the global keyword.
# it is important to note that while global variables can be useful in certain situations, they can also lead to code that is difficult to understand and maintain if overused. It is generally better to use local variables and pass them as arguments to functions or return values from functions rather than relying on global variables, as this promotes better encapsulation and makes the code more modular and easier to test.
# In summary, local variables are defined within a function and can only be accessed within that function, while global variables are defined outside of any function and can be accessed from anywhere in the code. It is generally recommended to use local variables whenever possible to avoid unintended side effects and improve code readability, while global variables should be used sparingly and with caution to prevent conflicts and maintainability issues in larger codebases.
# global variables can be useful for storing values that need to be accessed across multiple functions or modules, but they should be used with care to avoid unintended consequences and maintain code clarity. It is important to consider the scope and lifetime of variables when designing your code and to use global variables only when necessary, while favoring local variables and function parameters for better encapsulation and modularity.
# In conclusion, understanding the difference between local and global variables is crucial for writing clean and maintainable code in Python. Local variables are confined to the scope of a function, while global variables can be accessed from anywhere in the code. It is generally recommended to use local variables whenever possible to avoid unintended side effects and improve code readability, while global variables should be used sparingly and with caution to prevent conflicts and maintainability issues in larger codebases. By following these best practices, you can create code that is easier to understand, test, and maintain over time.
# we cant use local variables outside of the function they are defined in, while global variables can be accessed from anywhere in the code. It is important to use local variables for temporary data that is only needed within a specific function, while global variables should be reserved for data that needs to be shared across multiple functions or modules. By following these guidelines, you can create code that is more organized, easier to understand, and less prone to bugs and unintended side effects.
# how to change the value of a global variable inside a function
# To change the value of a global variable inside a function, you can use the global keyword to indicate that you want to access the global variable instead of creating a new local variable. Here is an example:
global_variable = "I am a global variable"
def my_function():
    global global_variable  # This tells Python that we want to use the global variable
    global_variable = "I have been modified inside the function"  # This modifies the global variable
print(global_variable)  # This will print "I am a global variable"
my_function()
print(global_variable)  # This will print "I have been modified inside the function" because we modified the global variable inside the function using the global keyword.
# It is important to use the global keyword judiciously, as it can lead to code that is difficult to understand and maintain if overused. It is generally better to pass variables as arguments to functions or return values from functions rather than relying on global variables, as this promotes better encapsulation and makes the code more modular and easier to test.
# In summary, to change the value of a global variable inside a function, you can use the global keyword to indicate that you want to access the global variable. However, it is important to use this feature with caution and consider alternative approaches such as passing variables as arguments or returning values from functions to promote better code organization and maintainability.
# file io in python
# File I/O (Input/Output) in Python allows you to read from and write to files on your computer. Python provides built-in functions and methods for working with files, making it easy to perform various file operations. Here are some common file I/O operations in Python:
#1. Opening a file: You can use the open() function to open a file in a specific mode (e.g., read, write, append). The syntax is: file = open('filename', 'mode').
#2. Reading from a file: You can use methods like read(), readline(), or readlines() to read the contents of a file. For example, file.read() reads the entire contents of the file as a string.
#3. Writing to a file: You can use the write() method to write data to  a file. For example, file.write('Hello, World!') writes the string 'Hello, World!' to the file.
#4. Closing a file: It is important to close a file after you are done working with it to free up system resources. You can use the close() method to close a file. For example, file.close() closes the file.
#5. Using with statement: It is recommended to use the with statement when working with files, as it automatically takes care of closing the file for you, even if an error occurs. The syntax is: with open('filename', 'mode') as file: followed by the block of code that works with the file.
# Example of file I/O in Python:
# Writing to a file
# with open('example.txt', 'w') as file:
#     file.write('Hello, World!')   
# Reading from a file
# with open('example.txt', 'r') as file:
#    content = file.read()
#   print(content)  # This will print 'Hello, World!' to the console
# In summary, file I/O in Python allows you to read from and write to files using built-in functions and methods. It is important to properly open, read/write, and close files to ensure efficient use of system resources and to prevent data loss. Using the with statement is a best practice for working with files, as it ensures that files are properly closed even in the event of an error.
# using append mode to write to a file without overwriting existing content
# with open('example.txt', 'a') as file:
#   file.write('This is an additional line.')  # This will append the string 'This is an additional line.' to the existing content of the file without overwriting it.
# In this example, the 'a' mode is used to open the file in append mode, which allows you to add new content to the end of the file without overwriting the existing content. Each time you run this code, it will append the specified string to the file, preserving any previous content that was already there. This is useful when you want to keep a log of events or add new data to a file without losing what was previously stored.
# using the with statement to read from a file and automatically close it
# read is default mode for opening a file, so we can omit the 'r' mode when using the with statement to read from a file
# with open('example.txt') as file:
#   content = file.read()
#   print(content)  # This will read the contents of 'example.txt' and print
# In this example, we use the with statement to open the file 'example.txt' for reading. The with statement ensures that the file is properly closed after we are done working with it, even if an error occurs. We read the contents of the file using the read() method and print it to the console. This is a best practice for working with files in Python, as it helps to prevent resource leaks and ensures that files are always properly closed.   
# if we try to open a non existent file for reading, it will raise a FileNotFoundError. To handle this error, we can use a try-except block to catch the exception and provide a user-friendly message or take appropriate action. For example:
# if we try to open a non-existent file for writing, it will create a new file with the specified name. However, if we try to open a non-existent file for reading, it will raise a FileNotFoundError. To handle this error, we can use a try-except block to catch the exception and provide a user-friendly message or take appropriate action. For example:
# try:
#     with open('non_existent_file.txt', 'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("The file you are trying to read does not exist. Please check the file name and try again.")
# In this example, we attempt to open a file that does not exist for reading. When the FileNotFoundError is raised, we catch it in the except block and print a user-friendly message to inform the user about the issue. This helps to improve the user experience and allows for graceful handling of errors when working with files in Python.   
# rb mode is used to open a file in binary mode for reading, while wb mode is used to open a file in binary mode for writing. When you open a file in binary mode, you are working with bytes rather than strings, which is important when dealing with non-text files such as images or audio files. In binary mode, you can read and write data in its raw byte form, which allows for more efficient handling of large files and ensures that the data is not modified or corrupted during the read/write process. It is important to use the appropriate mode when working with files to ensure that you are handling the data correctly and avoiding potential issues with encoding or data corruption.
# rt mode is used to open a file in text mode for reading, while wt mode is used to open a file in text mode for writing. When you open a file in text mode, you are working with strings rather than bytes, which is suitable for handling text files. In text mode, Python will automatically handle encoding and decoding of the data based on the specified encoding (e.g., UTF-8), which allows for easier manipulation of text data. It is important to use the appropriate mode when working with files to ensure that you are handling the data correctly and avoiding potential issues with encoding or data corruption.
# In summary, when working with files in Python, it is important to choose the appropriate mode (binary or text) based on the type of data you are working with. Binary mode is suitable for non-text files such as images or audio files, while text mode is suitable for handling text files. Using the correct mode ensures that you are handling the data correctly and helps to prevent issues with encoding or data corruption.
# read(), readline(), and readlines() are methods used to read data from a file in Python. The read() method reads the entire contents of the file as a single string, while readline() reads one line at a time and returns it as a string. The readlines() method reads all the lines in the file and returns them as a list of strings, where each string represents a line in the file. These methods provide different ways to access the contents of a file based on your needs, allowing you to read the entire file at once or process it line by line. It is important to choose the appropriate method based on the size of the file and how you want to handle the data in your program. 
f=open('example.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line.strip())  # This will read the file line by line and print each line without leading/trailing whitespace
f.close()  # Don't forget to close the file after you're done
# In this example, we open the file 'example.txt' for reading and use a while loop to read the file line by line using the readline() method. We check if the line is empty (which indicates the end of the file) and break the loop if it is. We also use the strip() method to remove any leading or trailing whitespace from each line before printing it. Finally, we close the file after we are done to free up system resources. This approach allows us to efficiently read large files without loading the entire contents into memory at once.        
# writelines() is a method used to write a list of strings to a file in Python. It takes a list of strings as an argument and writes each string to the file on a new line. This method is useful when you have multiple lines of text that you want to write to a file at once, as it allows you to write them all in one operation rather than writing each line individually. It is important to ensure that the list of strings you pass to writelines() includes newline characters ('\n') at the end of each string if you want them to be written on separate lines in the file. Otherwise, the strings will be concatenated together without any line breaks.
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('example.txt', 'w') as file:
    file.writelines(lines)  # This will write the list of strings to 'example.txt', with each string on a new line due to the newline characters included in the list.  
# seek() is a method used to change the current position of the file pointer in a file. It takes an offset and a whence argument to specify how the offset should be interpreted. The offset is the number of bytes to move the file pointer, while the whence argument specifies the reference point for the offset. The possible values for whence are:
#0: The offset is relative to the beginning of the file (default).
#1: The offset is relative to the current position of the file pointer.
#2: The offset is relative to the end of the file.
# For example, file.seek(0) will move the file pointer to the beginning of the file, while file.seek(10, 1) will move the file pointer 10 bytes forward from its current position. The seek() method is useful for navigating through a file and allows you to read or write data at specific positions within the file. It is important to use seek() in conjunction with the appropriate mode (binary or text) when working with files to ensure that you are handling the data correctly.
with open('example.txt', 'r') as file:
    print(type(file))  # This will print the type of the file object, which is <class '_io.TextIOWrapper'> for text files
    file.seek(0)  # Move the file pointer to the beginning of the file
    print(file.tell())  # This will print the current position of the file pointer, which should be 0 after seeking to the beginning of the file 
    data=file.read(5)  # Read the first 5 characters of the file
    print(data)  # This will print the first 5 characters of 'example.txt'
#tell() is a method used to get the current position of the file pointer in a file. It returns the number of bytes from the beginning of the file to the current position of the file pointer. This method is useful for tracking where you are in the file and can be used in conjunction with the seek() method to navigate through a file. For example, after reading some data from a file, you can use tell() to find out how many bytes have been read and where the file pointer is currently located. This information can be helpful for managing file operations and ensuring that you are working with the correct portion of the file when reading or writing data.
#truncate() is a method used to resize a file to a specified size. It takes an optional size argument that specifies the new size of the file in bytes. If the size argument is not provided, the file will be truncated to the current position of the file pointer. When a file is truncated, any data beyond the specified size will be removed from the file. This method is useful for managing file sizes and can be used to reduce the size of a file by removing unnecessary data or to create a new file with a specific size. It is important to use truncate() with caution, as it can lead to data loss if used incorrectly, especially if you truncate a file to a smaller size than its current content without properly handling the data that will be removed.
with open('example.txt', 'r+') as file:
    file.seek(0)  # Move the file pointer to the beginning of the file
    file.truncate()  # This will truncate the file to the current position of the file pointer, effectively clearing the contents of the file
# higher order functions
# Higher-order functions are functions that can take other functions as arguments or return functions as their result. They are a fundamental concept in functional programming and allow for more flexible and reusable code. In Python, functions are first-class citizens, which means that they can be treated like any other object, such as being passed as arguments to other functions or returned from functions. Higher-order functions enable you to create more abstract and powerful code by allowing you to manipulate functions as data. Examples of higher-order functions in Python include map(), filter(), reduce(), and sorted(), among others. These functions can take other functions as arguments to perform operations on iterables, making it easier to write concise and efficient code for data processing and transformation tasks.
# lambda functions
# Lambda functions, also known as anonymous functions, are small, unnamed functions that can be defined in a single line of code. They are often used for short, simple functions that are not intended to be reused elsewhere in the code. The syntax for a lambda function is: lambda arguments: expression. For example, lambda x: x * 2 defines a lambda function that takes one argument x and returns its value multiplied by 2. Lambda functions can be used in various contexts, such as with the map(), filter(), and reduce() functions, or as key functions for sorting. They provide a convenient way to create small, throwaway functions without the need for a formal function definition using def. However, it is important to use lambda functions judiciously, as they can make code less readable if overused or used for complex operations. In general, it is best to use lambda functions for simple operations and to define regular functions using def for more complex logic or when the function needs to be reused in multiple places in the code. 
def double(x):
    return x * 2
print(double(5))  # This will print 10
# Using a lambda function to achieve the same result
double_lambda = lambda x: x * 2
print(double_lambda(5))  # This will also print 10
cube_lambda = lambda x: x ** 3
print(cube_lambda(3))  # This will print 27
avg_lambda = lambda x, y: (x + y) / 2
print(avg_lambda(10, 20))  # This will print 15.0
# we can define a function that takes a lambda function as an argument and applies it to a list of values. For example:
def apply_function(func, values):
    return [func(x) for x in values]
# Example usage:
numbers = [1, 2, 3, 4, 5]
doubled = apply_function(lambda x: x * 2, numbers)
print(doubled)  # This will print [2, 4, 6, 8, 10]  
squared = apply_function(lambda x: x ** 2, numbers)
print(squared)  # This will print [1, 4, 9, 16, 25]
# In this example, the apply_function() function takes a lambda function (func) and a list of values (values) as arguments. It uses a list comprehension to apply the lambda function to each element in the list of values and returns a new list with the results. This allows us to easily apply different operations to the same set of values by simply passing different lambda functions as arguments to the apply_function() function.
# map, filter, and reduce functions
# The map(), filter(), and reduce() functions are built-in functions in Python that allow you to perform operations on iterables such as lists, tuples, or sets.    
# The map() function applies a given function to each item of an iterable and returns a new iterable with the results. For example, map(lambda x: x * 2, [1, 2, 3]) will return an iterable that produces the values 2, 4, and 6 when iterated over.
# The filter() function constructs an iterable from elements of an iterable for which a given function returns true. For example, filter(lambda x: x % 2 == 0, [1, 2, 3, 4]) will return an iterable that produces the values 2 and 4 when iterated over.
# The reduce() function is part of the functools module and applies a rolling computation to sequential pairs of values in an iterable. For example, reduce(lambda x, y: x + y, [1, 2, 3, 4]) will return the value 10, which is the result of adding all the numbers together.
# These functions are powerful tools for functional programming in Python and can help you write more concise and efficient code when working with iterables. They allow you to apply transformations, filter data, and perform reductions on collections of data in a clean and readable way. It is important to use these functions appropriately and to consider readability when using them, as they can sometimes make code less clear if overused or used for complex operations. 
# In summary, the map(), filter(), and reduce() functions are essential tools for working with iterables in Python. They provide a functional programming approach to processing data and can help you write more concise and efficient code. By understanding how to use these functions effectively, you can enhance your ability to manipulate and analyze data in Python.   
# example of using map(), filter(), and reduce() functions
from functools import reduce    
numbers = [1, 2, 3, 4, 5]
# Using map() to double each number in the list
# This will return an iterable that produces the values 2, 4, 6, 8, and 10 when iterated over
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))  # This will print [2, 4, 6, 8, 10]
# Using filter() to get only the even numbers from the list
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # This will print [2, 4]
# Using reduce() to calculate the sum of all numbers in the list
total = reduce(lambda x, y: x + y, numbers)
print(total)  # This will print 15
#is vs == in python
# In Python, the is operator checks for identity, meaning it checks whether two variables refer to the same object in memory. On the other hand, the == operator checks for equality, meaning it checks whether the values of the objects being compared are equal. For example, if you have two variables a and b that both refer to the same list object in memory, a is b will return True because they are the same object, while a == b will also return True because their values are equal. However, if you have two separate list objects with the same contents, a is b will return False because they are different objects in memory, while a == b will return True because their values are equal. It is important to understand the difference between these two operators to avoid confusion when comparing objects in Python.
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is b)  # This will print False,exact location of a and b in memory are different
print(a == b)  # This will print True,because the values of a and b are equal
print(a is c)  # This will print True
print(a == c)  # This will print True
x=3
y=3
print(x is y)  # This will print True, because small integers are cached by Python
print(x == y)  # This will also print True, because the values of x and y are equal
p=(1, 2, 3)
q=(1, 2, 3)
print(p is q)  # This will print False, because tuples with the same contents are not guaranteed to be the same object in memory
print(p == q)  # This will print True, because the values of p and q are equal
# rock paper scissors game
choice=["stone","scissors","paper"]
import random
player_choice=str(input("Enter your choice (stone, scissors, paper): ")).lower()
computer_choice=random.choice(choice)
print(f"Computer chose: {computer_choice}")
if (player_choice == computer_choice):
    print("It's a tie!")
elif (player_choice =="stone" and computer_choice=="paper") or(player_choice=="paper"and computer_choice=="scissors") or(player_choice=="scissors" and computer_choice=="stone"):
    print("Computer wins!")
else:
    print("You win!")

# now using matrix to determine the winner
outcome_matrix = {
    ("stone", "scissors"): "You win!",
    ("scissors", "paper"): "You win!",
    ("paper", "stone"): "You win!",
    ("scissors", "stone"): "Computer wins!",
    ("paper", "scissors"): "Computer wins!",
    ("stone", "paper"): "Computer wins!",
    ("stone", "stone"): "It's a tie!",
    ("scissors", "scissors"): "It's a tie!",
    ("paper", "paper"): "It's a tie!"
}   
print(outcome_matrix.get((player_choice, computer_choice), "Invalid choice! Please choose stone, scissors, or paper.")) 
# OOPs concepts in python
# why OOPs concepts are important in python
# procedural programming focuses on writing procedures or routines that operate on data, while Object-Oriented Programming (OOP) focuses on creating objects that encapsulate both data and behavior. OOP allows for better organization of code, promotes code reusability through inheritance, and provides a way to model real-world entities more effectively. In Python, OOP is important because it helps developers create modular and maintainable code, making it easier to manage complex projects and collaborate with other developers. OOP concepts such as classes, objects, inheritance, polymorphism, and encapsulation are fundamental to Python programming and are widely used in various applications, from web development to data science. By understanding and applying OOP principles in Python, developers can create more efficient and scalable software solutions.
# Object-Oriented Programming (OOP) is important in Python because it provides a structured and modular approach to programming, allowing developers to create reusable and maintainable code. OOP allows you to model real-world entities as objects, which can have attributes (data) and methods (functions) that operate on that data. This promotes encapsulation, where the internal state of an object is hidden from the outside world and can only be accessed through defined interfaces. OOP also supports inheritance, which allows you to create new classes based on existing ones, promoting code reuse and reducing redundancy. Additionally, OOP enables polymorphism, allowing objects of different classes to be treated as instances of a common superclass, making it easier to write flexible and extensible code. Overall, OOP concepts help to improve code organization, readability, and maintainability in Python programming.
# Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, which are instances of classes. In Python, OOP is supported through the use of classes and objects. A class is a blueprint for creating objects, while an object is an instance of a class that can have its own attributes and methods. OOP allows for encapsulation, inheritance, and polymorphism, which are key principles that help to promote code reusability, modularity, and maintainability. By using OOP concepts in Python, you can create more organized and structured code that is easier to understand and maintain over time.
# In Python, you can define a class using the class keyword, followed by the name of the class and a colon. Inside the class, you can define attributes (variables) and methods (functions) that belong to the class. For example:
class definitions:
    def person(name, age):
        print(f"Name: {name}, Age: {age}")
definitions.person("Alice", 30)  # This will print "Name: Alice, Age: 30"
# In this example, we define a class called definitions with a method called person that takes two parameters, name and age. We then call the person method with the arguments "Alice" and 30, which prints the name and age to the console. This is a simple example of how to define a class and a method in Python. You can create more complex classes with multiple attributes and methods to model real-world entities and behaviors in your code.
class Person:
    def __init__(self, name, age):
        self.name = name  # This is an attribute of the class
        self.age = age    # This is another attribute of the class

    def greet(self):  # This is a method of the class
        return f"Hello, my name is {self.name} and I am {self.age} years old."
# In this example, we define a class called Person with an __init__ method that initializes the name and age attributes, and a greet method that returns a greeting message. We can create instances of the Person class and call the greet method to see how it works:
person1 = Person("Alice", 30)
print(person1.greet())  # This will print "Hello, my name is Alice and I am 30 years old."
person2 = Person("Bob", 25)
print(person2.greet())  # This will print "Hello, my name is Bob and I am 25 years old."
# In this example, we create two instances of the Person class, person1 and person2, with different names and ages. We then call the greet method on each instance to see the personalized greeting message based on the attributes of each object. This demonstrates how OOP allows us to create objects with their own state and behavior, making our code more organized and reusable.
alice.changeName("malice") # type: ignore
# here we are trying to change the name of alice object to malice, but we have not defined a method called changeName in the Person class. To fix this, we can add a method to the Person class that allows us to change the name attribute. For example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def changeName(self, new_name):  # This method allows us to change the name attribute
        self.name = new_name    
# Now we can create an instance of the Person class and use the changeName method to change the name attribute:
alice = Person("Alice", 30)
print(alice.greet())  # This will print "Hello, my name is Alice and I am 30 years old."
alice.changeName("Malice")  # This will change the name attribute of the alice object to "Malice"
print(alice.greet())  # This will print "Hello, my name is Malice and I am 30 years old."   
# self is a reference to the current instance of the class and is used to access the attributes and methods of the class within its own definition. It is a convention in Python to use self as the first parameter of instance methods, although you can technically use any name for this parameter. The self parameter allows you to refer to the instance of the class that is calling the method, enabling you to access and modify its attributes and call other methods on that instance. For example, in the changeName method we defined earlier, we use self.name to access and modify the name attribute of the specific instance of the Person class that is calling the method. This allows us to change the name of that particular object without affecting other instances of the class.        
# self ka matlab wo object hai jispe method call ho rha hai, aur self ke through hum us object ke attributes aur methods ko access kar sakte hain. Jab hum kisi method ko call karte hain, to Python automatically us method ke first parameter (jo conventionally self hota hai) ko us object se bind kar deta hai jiske upar method call ho rha hai. Isliye, self ka use karke hum apne class ke andar us specific instance ke data ko manipulate kar sakte hain aur uske behavior ko define kar sakte hain.      
#contructors in python
# In Python, a constructor is a special method that is automatically called when an object of a class is created. The constructor method is defined using the __init__() method within the class. It is used to initialize the attributes of the class when an object is instantiated. The __init__() method takes self as the first parameter, which refers to the instance of the class being created, and can also take additional parameters to set the initial values of the object's attributes. For example:
class Car:
    def __init__(self, make, model, year):
        self.make = make  # This is an attribute of the class
        self.model = model  # This is another attribute of the class
        self.year = year  # This is yet another attribute of the class
        print(f"Car created: {self.make} {self.model} ({self.year})")  # This will print a message when a Car object is created
# In this example, we define a class called Car with an __init__() method that initializes the make, model, and year attributes of the class. When we create an instance of the Car class, the __init__() method is automatically called, and we can pass the values for make, model, and year to initialize the attributes of the car object. The constructor allows us to set up our objects with specific initial values when they are created, making it easier to work with them in our code.
a=Car("Toyota", "Camry", 2020)
print(a.make)  # This will print "Toyota"
print(a.model)  # This will print "Camry"
print(a.year)  # This will print 2020
# In this example, we define a class called Car with an __init__() method that initializes the make, model, and year attributes of the class. When we create an instance of the Car class (a), the __init__() method is automatically called, and we pass the values "Toyota", "Camry", and 2020 to initialize the attributes of the car object. We can then access these attributes using dot notation (a.make, a.model, a.year) to retrieve their values. The constructor allows us to set up our objects with specific initial values when they are created, making it easier to work with them in our code. 
# types of constructors in python
# In Python, there are three types of constructors: default constructor, parameterized constructor, and copy constructor.
#1. Default Constructor: A default constructor is a constructor that takes no parameters and initializes the attributes of the class with default values. If you do not define an __init__() method in your class, Python will automatically provide a default constructor that does nothing. For example:
class DefaultConstructorExample:
    def __init__(self):
        self.message = "This is a default constructor"
# In this example, we define a class called DefaultConstructorExample with a default constructor that initializes the message attribute with a default value. When we create an instance of this class, the __init__() method is automatically called, and the message attribute is set to "This is a default constructor".
#2. Parameterized Constructor: A parameterized constructor is a constructor that takes parameters and initializes the attributes of the class with the values passed as arguments. This allows you to create objects with specific initial values. For example:
class ParameterizedConstructorExample:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# In this example, we define a class called ParameterizedConstructorExample with a parameterized constructor that takes name and age as parameters and initializes the corresponding attributes. When we create an instance of this class, we pass the values for name and age to the constructor, which then initializes the attributes with those values. 
#3. Copy Constructor: A copy constructor is a constructor that creates a new object as a copy of an existing object. In Python, you can create a copy constructor by defining an __init__() method that takes an instance of the same class as a parameter and copies its attributes to the new object. For example:
class CopyConstructorExample:
    def __init__(self, other):
        self.name = other.name
        self.age = other.age
# In this example, we define a class called CopyConstructorExample with a copy constructor that takes another instance of the same class (other) as a parameter and copies its name and age attributes to the new object. When we create an instance of this class using another instance, it will create a new object with the same attribute values as the original object.
original = CopyConstructorExample(ParameterizedConstructorExample("Alice", 30))
copy = CopyConstructorExample(original)
print(copy.name)  # This will print "Alice" 
print(copy.age)  # This will print 30
# In this example, we first create an instance of the ParameterizedConstructorExample class with the name "Alice" and age 30. We then create a new instance of the CopyConstructorExample class by passing the original instance as an argument to the copy constructor. The copy constructor initializes the name and age attributes of the new object with the values from the original object. As a result, when we print copy.name and copy.age, we get "Alice" and 30, respectively, demonstrating that the copy constructor successfully created a new object with the same attribute values as the original object.
# decorators in python
# In Python, a decorator is a design pattern that allows you to modify the behavior of a function or a class method without changing its source code. A decorator is a higher-order function that takes another function as an argument and returns a new function that typically extends the behavior of the original function. Decorators are often used for logging, access control, memoization, and other cross-cutting concerns in programming. They are defined using the @ symbol followed by the name of the decorator function above the function definition that you want to decorate. For example:
def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
# In this example, we define a decorator function called my_decorator that takes a function (func) as an argument and defines a wrapper function that adds some behavior before and after calling the original function. We then use the @my_decorator syntax to decorate the say_hello function. When we call say_hello(), it will execute the wrapper function defined in the decorator, which will print messages before and after calling the original say_hello function, resulting in the following output:
say_hello()
# Output:
# Before the function is called.    
# Hello!
# After the function is called.
# In this example, the my_decorator function modifies the behavior of the say_hello function by adding additional functionality before and after the original function is executed. This allows us to enhance the functionality of say_hello without modifying its source code, demonstrating the power and flexibility of decorators in Python.
#using *args and **kwargs in python
# In Python, *args and **kwargs are used to allow a function to accept an arbitrary number of positional and keyword arguments, respectively. The *args syntax allows you to pass a variable number of positional arguments to a function, which are then accessible as a tuple within the function. For example:
def my_function(*args):
    for arg in args:
        print(arg)
my_function(1, 2, 3)  # This will print 1, 2, and 3 on separate lines
# In this example, the my_function takes *args as a parameter, which allows it to accept any number of positional arguments. When we call my_function(1, 2, 3), it prints each argument on a separate line.
# The **kwargs syntax allows you to pass a variable number of keyword arguments to a function, which are then accessible as a dictionary within the function. For example:
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_function(name="Alice", age=30, city="New York")  # This will print the key-value pairs of the keyword arguments
# In this example, the my_function takes **kwargs as a parameter, which allows it to accept any number of keyword arguments. When we call my_function(name="Alice", age=30, city="New York"), it prints each key-value pair of the keyword arguments on a separate line. This allows us to create flexible functions that can handle varying numbers of arguments without needing to define them explicitly in the function signature.
# In summary, *args and **kwargs are powerful tools in Python that allow you to create functions that can accept a variable number of arguments, making your code more flexible and adaptable to different use cases. By using *args for positional arguments and **kwargs for keyword arguments, you can design functions that can handle a wide range of input without needing to specify every possible argument in advance.
# Now using these with decorators
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)  # Pass the arguments to the original function
        print("After the function is called.")
        return result  # Return the result of the original function
    return wrapper
@my_decorator
def greet(name):
    return f"Hello, {name}!"
# In this example, we define a decorator function called my_decorator that takes a function (func) as an argument and defines a wrapper function that accepts any number of positional and keyword arguments using *args and **kwargs. The wrapper function adds some behavior before and after calling the original function, and it also returns the result of the original function. We then use the @my_decorator syntax to decorate the greet function. When we call greet("Alice"), it will execute the wrapper function defined in the decorator, which will print messages before and after calling the original greet function, and it will return the greeting message as well:
print(greet("Alice"))
# Output:
# Before the function is called.
# After the function is called.
# Hello, Alice!
# In this example, the my_decorator function modifies the behavior of the greet function by adding additional functionality before and after the original function is executed, while also allowing us to pass arguments to the original function and return its result. This demonstrates how *args and **kwargs can be used in conjunction with decorators to create flexible and powerful functions in Python.
#getter and setter in python
# In Python, getters and setters are methods that allow you to access and modify the attributes of a class in a controlled manner. They are typically used to encapsulate the internal state of an object and provide a way to validate or manipulate the data before it is accessed or modified. Getters are methods that retrieve the value of an attribute, while setters are methods that set the value of an attribute. In Python, you can use the @property decorator to define a getter method and the @<attribute_name>.setter decorator to define a setter method for a specific attribute. For example:
class Person:
    def __init__(self, name):
        self._name = name  # The underscore indicates that this attribute is intended to be private

    @property
    def name(self):  # This is the getter method for the name attribute
        return self._name

    @name.setter
    def name(self, new_name):  # This is the setter method for the name attribute
        if isinstance(new_name, str) and new_name:  # Validate that the new name is a non-empty string
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string.")
# In this example, we define a class called Person with a private attribute _name. We use the @property decorator to define a getter method for the name attribute, which allows us to access the value of _name in a controlled way. We also use the @name.setter decorator to define a setter method for the name attribute, which allows us to set the value of _name while also validating that the new name is a non-empty string. This approach helps to encapsulate the internal state of the object and provides a way to ensure that the data is valid when it is modified.
















