# PYTHON OPERATORS
# Python Operators are used to perform operations on variables and values. Python divides the operators into the following groups:
"""
    a. Arithmetic Operators - [ addition(+), subtraction(-), multiplication(*), division(/), modulus(%), exponential(**), flor division(//) ] 
    b. Assignment Operators 
    c. Comparison Operators
    d. Logical Operators
    e. Identity Operators
    f. Membership Operators
    g. Bitwise Operators
"""

# b. ASSIGNMENT OPERATORS: These are used to assign values to variables. EG:
'''
    =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
'''

# c. COMPARISON OPERATORS: Comparison operators are used to compare two values:
'''
    [ Equal(==), Not equal(!=), Greater than(>), Less than(<), Greater than or equal to(>=), Less than or equal to(<=) ]
'''

# d. PLOGICAL OPERATORS: Logical operators are used to combine conditional statements.
"""
    [ 
        "and" - Returns "True" if both statements are true
        "or"  - Returns "True" if one of the statements is true
        "not" - Reverse the result, returns "False" if the result is true 
    ]
"""

# e. IDENTITY OPERATORS: Identity operators are used to compare the objects, not if they are equal, but if they are the same object with the same memory location:
"""
    [
        "is"     - Returns "True" if bothe variables are the same object
        "is not" - Returns "True" id both variables are not the same object 
    ]
    EG:
"""

x = ["apple", "Mangoe", "Banana"]
y = ["apple", "Mangoe", "Banana"]
z = x

print(x is z) # This will Return True, because "Z" & "X" share the same object and memory location.

# f. PYTHON MEMEBERSHIP OPERATORS: Membership Operators are used to test if a sequence is presented in an object:
"""
    [
        "in"       - Returns "True" if a sequence with a specified value is present in the object
        "not in"   - Returns "True" if a sequence with a specified value is not present in the object
    ]
"""

# g. PYTHON BITWISE OPERATORS: Bitwise operators are used to compare (binary) numbers:
"""
    [
        AND ("&")  - sets each bit to 1 if both bits are 1 
        OR  ("|")  - sets each bit to 1 if two bits is 1 
        XOR  ("^")  - sets each bit to 1 if only one of two bits is 1 
        NOT  ("~")  - inverts all the bits
        Zero fill left shift ("<<") - Shift left by pushing zeros in from the right and let the leftmost bits fall off
        signed right shift (">>") - Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off 
    ]
"""


# OPERATOR PRECENDENCE: This describes the order in which operations are performed.
# Parenthesis has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

