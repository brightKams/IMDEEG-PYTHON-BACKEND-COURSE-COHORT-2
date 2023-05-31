'''
    FUNCTIONS:
    Functions are named blocks of code, designed to do one specific job. Information passed to a function is called an argument, and information received by a function is called a parameter.
'''
# Parts of a function :
# "def" keyword
# name of the function
# bracket "()"
# Parameters
# Arguments
# colon ":"
# NB: Arguments and parameters are used interchangeably. Parameter is the variable that collects an argument.

# A simple Function:

def greetUser():
    print("Hello!")
greetUser()

# Passing an Argument in a function
def userGreet(username):
    print("Hello", username)
userGreet("Bright")


# A Default Parameter Function:
def makePizza(topping = "bacon"):
    print("Have a " + topping + " pizza" ) 

makePizza()
makePizza("Peperroni")
print()
# Returning a value

def add_numbers(x, y):
    return x + y
sum = add_numbers(3, 5)
print(add_numbers(3, 5))

