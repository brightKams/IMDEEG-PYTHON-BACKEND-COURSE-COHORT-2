'''
    Your programs can prompt the user for input. All inputs are stored as a string, except you decide to change it data-type by casting the value into an, integer or float, ddepending on what you have programmed the user to enter.
'''
# Example:
# Prompting for a value:
fname = input("What is your First Name? ")
lname = input("What is your Last Name? ")
ask_Age = "Hello", lname, fname + ", How old are you?"
print(ask_Age)
age = int(input("Enter age Here: "))
message = "Hello " + lname + " " + fname + ", you are " + str(age) + " years old."
print(message)


# Exaple 2:
# Prompting for numerical input
'''
    To prompt for a numerical input, you can use the "int()" method, "float() method or any other numerical data-type to "cast the value into a numerical data-type.
'''
pi = float(input("what is the value of pi: "))
print(pi)

