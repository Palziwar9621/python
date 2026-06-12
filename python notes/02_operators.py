# ============================================================
# OPERATORS IN PYTHON
# ============================================================

# arithmetic operators: +, -, *, /, %, **, //
x, y = 2, 3
z = x ** y   # 8 - exponentiation (left operand to power of right)
z = 7 // 3   # 2 - floor division (largest integer <= result)

# comparison operators: ==, !=, >, <, >=, <=
# logical operators: and, or, not
# assignment operators: =, +=, -=, *=, /=, %=, **=, //=

# ============================================================
# BITWISE OPERATORS: &, |, ^, ~, <<, >>
# used to perform bitwise operations on integers
# ============================================================
x = 5  # binary: 0101
y = 3  # binary: 0011

z = x & y   # 1  - AND:        0101 & 0011 = 0001
z = x | y   # 7  - OR:         0101 | 0011 = 0111
z = x ^ y   # 6  - XOR:        0101 ^ 0011 = 0110
z = ~x      # -6 - NOT:        ~0101 = 1010 in two's complement = -6
z = x << 1  # 10 - left shift: 0101 << 1 = 1010
z = x >> 1  # 2  - right shift:0101 >> 1 = 0010

# ============================================================
# MEMBERSHIP OPERATORS: in, not in
# test if a value is present in a sequence (list, tuple, string)
# ============================================================
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)   # True
print("grape" in fruits)    # False

# ============================================================
# IDENTITY OPERATORS: is, is not
# compare memory locations of two objects
# is     -> True if both operands refer to same object in memory
# is not -> True if both operands do NOT refer to same object
# ============================================================
a = [1, 2, 3]
b = a           # b points to same object as a
c = [1, 2, 3]  # c is different object with same values

print(a is b)      # True  - same object in memory
print(a is not b)  # False - same object in memory
print(a is c)      # False - different objects in memory
print(a == c)      # True  - same values

# ============================================================
# OPERATOR PRECEDENCE (highest to lowest)
# 1.  ()                   - parentheses
# 2.  **                   - exponentiation
# 3.  +x, -x              - unary plus/minus
# 4.  *, /, //, %         - multiplication, division
# 5.  +, -                - addition, subtraction
# 6.  <<, >>              - bitwise shift
# 7.  &                   - bitwise AND
# 8.  ^                   - bitwise XOR
# 9.  |                   - bitwise OR
# 10. comparison operators - ==, !=, >, <, >=, <=
# 11. not                 - logical NOT
# 12. and                 - logical AND
# 13. or                  - logical OR
# ============================================================
