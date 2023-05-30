'''
    WHILELOOP:
    The while loop is used too repeat a block of code as long as a condition is met.

    EXAMPLES:
'''
# A simple while Loop:

count = 0
while count <=10:
    print(count)
    count += 1
    if count > 9:
        break

# Letting the user choose when to quit
msg = ""
while msg != "quit":
    msg = input("What is your message? ")
    
    print(msg + " is your message")
