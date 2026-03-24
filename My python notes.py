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
from kratim import greet # this will import the greet function from the kratim module and it will be executed when main.py is run directly, but it will not be executed when main.py is imported as a module in another script. This allows us to use the greet function in other scripts without executing the code that is meant to be run only when main.py is executed directly.
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
alice.changeName("malice")
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




















