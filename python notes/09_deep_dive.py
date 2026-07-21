# call by object reference is a method of passing arguments to a function in which the reference (or memory) address of the object is passed to the function, rather than a copy of the object itself. This means that if the object is mutable (like a list or dictionary), any changes made to the object within the function will affect the original object outside the function. However, if the object is immutable (like a string or tuple), any changes made within the function will not affect the original object.
# getref() is a built-in function in python that returns the reference count of an object.
# Garbage collection is a process in which the interpreter automatically manages memory by reclaiming memory occupied by objects that are no longer in use. Python uses reference counting and a cyclic garbage collector to manage memory. When an object's reference count drops to zero, it is considered unreachable and can be collected by the garbage collector. The garbage collector can also detect and collect cyclic references, where objects reference each other in a cycle, preventing their reference counts from reaching zero.
#weird behaviour:
"""
import sys
 weird behaviour:
 a=2
 b=a
 c=b
print(sys.getrefcount(a))
output= 3221225472 """
# so this weird behaviour happens because 2 is a very common object and it is assigned to various objects in the system thats why the reference count is very high. The reference count of an object is the number of references that point to that object. In this case, the integer 2 is a commonly used object in Python, and it is assigned to multiple variables (a, b, c) in the code. Therefore, the reference count of 2 is very high, which is why sys.getrefcount(a) returns a large number (3221225472).
# -5 to -256 are considered very commonly used so python automatically creates these objects and assign them to a memory. But, if we assign values other than this then each variable will create a new object at a new memory location or address.
# if a same string is assigned to different variable and it is a valid identifier then all variables point to that object but if it is not then new memory addresses are created
#mutability of objects: in mutable objects a change in one variable will affect the other variable but in immutable objects a change in one variable will not affect the other variable. It is because mutable objects can be changed in place, while immutable objects cannot be changed once they are created. Therefore, when a mutable object is assigned to multiple variables, all variables point to the same object in memory, and any changes made to the object through one variable will be reflected in all other variables that reference the same object. In contrast, when an immutable object is assigned to multiple variables, each variable points to a separate copy of the object in memory, and any changes made to one variable will not affect the other variables.
#b=a[:]  # this is a shallow copy of the list a. It creates a new list object b that contains references to the same elements as the original list a. Therefore, if we modify an element in the original list a, it will also affect the corresponding element in the copied list b, and vice versa. However, if we modify the copied list b by adding or removing elements, it will not affect the original list a.



