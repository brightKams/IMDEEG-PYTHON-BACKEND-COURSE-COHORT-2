"""
    Python is a popular programming language. It was created by Guido Van Rossum, and released in 1991.
    It is used for:
    1. Web Development (server-side)
    2. Software Development
    3. Mathematics
    4. System Scripting

"""

'''
    INDENTATION:
    Indentation refers to the spaces at the beginning of a code line.
    For other progrogramming languages, the indentation in code is for readability only, but indentation in Pythonis very important.

    Python uses Indentation to indicate a block code.
'''

num1 = input("Enter a number1: ")
num2 = input("Enter a number2: ")

# if type(num1) and type(num2) == int:
if num1 > num2:
    print(num1 + " is greater than " + num2 )
else:
    print(num2 + " is greater than " + num1)


'''
    CASTING:
    This is used to specify the data type of a variable.
    Eg;
'''

x = str(3) # here x will be '3' as a string
y = int(3) # here y will be 3 as a number or integer
z = float(3) # here z will be 3.0 as a float
print("\n")
print(x)
print(y)
print(z)


# ASSIGNING VARIABLES IN PYTHON

# 1. MANY VALUES TO MULTIPLE VARIABLES:

x, y, z = "Orange ", "Banana ", "Cherry "
print(x + y + z)
# NB: "+" operator works only when the two values are of the same data type. else it will return an error.
print(x)
print(y)
print(z)

# 2. ONE VALUE TO MULTIPLE VARIABLES
print()
x = y = z = "Orange"
print(x, y, z)

# 3. UNPACKING A COLLECTION
'''
    If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
'''
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# GLOBAL VARIABLES:
'''
    Global variables are variables created outside of function. They can be called and used anywhere, but once a variable is written inside a function, it only functions within the scope of that function.
    Eg:
'''

pythonExperience = "awesome"

def Myfunction(arg):
    message = "Python is " + arg
    return print(message)
Myfunction(pythonExperience)


# The "global" Key Word 
'''
    The "global" keyword is used to create a global variable inside a function. Ordinarily, when variables are created inside a function, they are local variables, but when they are declared with the "global" keyword, it becomes a global variable.

    Also, you can use the "global" keyword to change the value of a global variable inside a function
    EG:
 '''

def myFunc():
    global newX
    newX = "Fantastic"
    message = "Do you know that Python is " + newX +"!"
    return print(message)
myFunc()

print(newX)


# Changeing a global variable from inside a function scope or block

animal = "Elephant"

def animalName():
    global animal
    animal = "Goat"
animalName()

print("The new animal name is " + animal)

l = complex(5)
print(l)
