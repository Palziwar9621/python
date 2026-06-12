# ============================================================
# EXCEPTION HANDLING
# ============================================================

# basic try / except / finally
try:
    print(10 / 0)                    # raises ZeroDivisionError
except ZeroDivisionError:
    print("you cannot divide by zero")
finally:
    # finally runs regardless of whether exception was raised or not
    # useful in functions - ensures cleanup code always runs
    print("this will execute regardless of whether an error occurred")

# we can directly execute code without finally block
# but we use finally because during functions we want some code
# to execute after the function regardless of exceptions
# and that can only be done reliably with finally

# ============================================================
# RAISING EXCEPTIONS
# ============================================================
def divide(a, b):
    if b == 0:
        raise ValueError("you cannot divide by zero")
    return a / b

# ============================================================
# CUSTOM EXCEPTIONS
# ============================================================
# create by inheriting from the Exception class
class CustomError(Exception):
    pass

def custom_function():
    raise CustomError("this is a custom error")

# ============================================================
# ERROR TYPES
# ============================================================
# SyntaxError        - syntax error in code
# NameError          - variable not defined
# TypeError          - operation on wrong data type
# IndexError         - index out of range
# KeyError           - key not found in dictionary
# AttributeError     - attribute not found in object
# ValueError         - correct type but inappropriate value
# FileNotFoundError  - file not found
# ZeroDivisionError  - division by zero
# ImportError        - module not found
# ModuleNotFoundError- module not found
# IndentationError   - indentation error in code
# TabError           - tab error in code
# StopIteration      - no more items to iterate over
# GeneratorExit      - generator is closed
# KeyboardInterrupt  - user pressed Ctrl+C
# SystemExit         - program is exited
# MemoryError        - not enough memory
# OverflowError      - arithmetic result too large to represent
# RecursionError     - maximum recursion depth exceeded
# AssertionError     - assert statement failed
# StopAsyncIteration - no more items in async iterator

# ============================================================
# WARNINGS (not errors - just alerts)
# ============================================================
# Warning            - something might be wrong
# DeprecationWarning - feature is deprecated, will be removed
# SyntaxWarning      - syntax warning
# RuntimeWarning     - runtime warning
# FutureWarning      - feature will change in future
# ImportWarning      - import warning
# UnicodeWarning     - unicode warning
# BytesWarning       - bytes warning
# ResourceWarning    - resource warning
