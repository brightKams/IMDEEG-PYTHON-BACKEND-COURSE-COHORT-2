# PYTHON DATA TYPES
'''
    Text Type: str
    Numeric Types: int, float, complex
    Sequence Types: list, tuple, range
    Mapping Typs: dict
    Set Types: set, frozenset
    Boolean Type: bool
    Binary Types: bytes, bytearray, memoryview
    None Type: NoneType
'''
'''
    Text Type: str
    EG:
'''

x = str(5)
print(x)
x = range(6)
print(x)
x = bytearray(6)
print(x)

import random
print(random.randrange(1, 10))

# Looping Through a string
'''
    To loop through a string, the 'for loop is used"  
'''
for x in "banana":
    print(x)

# The "len()" method
    # To get the length of a string, the "len()" method is used

a = "Hello, World!"
print(len(a))


# Checking if an item exists in a string or sequence of character, the "in" keyword is used. This will always return a boolean of either "True" or "False"
# EG:
txt = "The best thing in life are free!"
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is present")

txt = "The best things in life are expensive"
if 'expensive' not in txt:
    print("'expensve is not in the sentence")
else:
    print("expensive is in the sentence")


# slicing
'''
    you can return aa range of characters by using the slice syntax.
    Specify the start index and the end index, separated by a colon, to return a part of the string.
    EG:
'''
print()
b = "Hello, World!"
print(b[2:5])

# Slicing from the beginning to a certian index number 
# EG:
c = "My name is Bright"
print(c[:10] + "....")

# Slicing from a point to the end of a sequence of characters
d = "here, characters are missing from the beginning"
print("...." + d[6:])

# NEGATIVE INDEXING
# Negative indexes are used to start the slice from the end and then moves backwards
# EG:

e = "BRIGHT"
print( e[0:1] + e[-5:])

# PYTHON - Modify Strings
# Python has a built-in method that you can use on strings

# 1. upper() method
# This returns the string in upper case.
b = "Hi there!"
print(b.upper())

# 2. lower() method
# This returns the string in a lower case.
c = "HELLO THERE!"
print(c.lower())

# 3. strip() method
# This is used to remove whitespace from the beginning or end of a text.

d = "   How are you   "
print(d.strip())

# 4. replace() method
# This replaces a string with another string
# EG:

e = "Hello, World!"
print(e.replace("World", "Bright"))

# 5. split() method
# This method splits the string into substrings if it finds the character or instances entered in the method to form a new string in a list.
# EG:
f = "My name is, Bright, Chidozie, Ohakam"
print(f.split(","))


# STRING CONCATENATION: To concatenate a string, you use the "+" sign.
# EG:

x = "Hello"
y = "World"
z = x + " " + y
print(z)


# PYTHON -Format - Strings
# format() method is used to combine both strings and number or any other data types together. to use the format() method, a placehoder "{}" (curly brace) is passed in the string where the placeholders are. It can take as many arguments or placeholders as possible.
# EG:

age = 36
txt = "My name is John, I am {}" 
print(txt.format(age))

# OR

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))

# PYTHON - Escape Characters
# Escape Character is used to insert an illegal character inside a string. The back slash "\" is used to insert an illegal charcater inside a string.
# For example when you want to insert a character with a double quote inside a string that has a character that has a double quote, you first of all insert the back slash "\" character. EG:
text = "I am \"Bright\" Ohakam" 
print(text)

# PYTHON - Booleans
# Booleans represents one of two values: "True" or "False"
# NB: "bool()" method is used to return a boolean value of either "True" or "False"
# Almost any value is evaluated to "True" if it has a content.
# Any nstring is "True", except empty strings.
# Any number is "True", except 0.
# The value "None" also returns a "False" value
# Any list, tuple, set, and dictionary are "True", except empty ones. 

# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
# EG;

x = 300
print(isinstance(x, int))

n = 3.5
print(type(n))

h = str(n)
print(type(h))
print(float(h))
i = float(h)
print(int(i))

# CONVERTING DATA TYPES 

user_grades = ["54", "84", "90", "67"]
grades = [int(g) for g in user_grades]
print(grades)
