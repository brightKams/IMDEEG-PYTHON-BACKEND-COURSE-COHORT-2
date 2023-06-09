


# PYTHON TUPLES
'''
    Tuple is used to create a sequence of characters that are immutable. They can either be separated by commas inside a parenthesis "()" or just separeted by commas without a parenthesis.
'''
tupleExample1 = "one", "two", "three"
print(type(tupleExample1))
print("\n")
# OR
tupleExample2 = "four", "five", "six"
print(type(tupleExample2))


# PYTHON LIST
"""
    Lists are used to store multiple items in a single variable. Lists are ine of 4 built-in data types used to store collections of fata, the other 3 are "Tuple", "Set", and "Dictionary", all with different qualities and usage.
    Lists are created using square brackets:
    EG:
"""

list1 = ["alpha, beta, charlie"]
print(list1)
# List Items - List items are ordered, changeable, and allow duplicate values. List items are indexed, the first item is indexed [0], the second item has index [1] etc.

# Ordered - When we say that lists are ordered, it means that the items have a defined order, and that ordeer will not change. If you add new items to a list, the new item will be placed at the end of the list.

# LOOPING THROUGH A LIST

thislist = ["apple", "mango", "orange"]

# "for loop" :
for eachItem in thislist:
    print(eachItem)

print()
for item in range(len(thislist)):
    print(thislist[item])
print("\nHello You")
# using "while loop"

loopCount = 0

while loopCount < len(thislist):
    print( str(loopCount) +":" + thislist[loopCount] )
    loopCount +=1
print("\n")

# Using Loop Comprehension:
'''
    List Comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
    In using "loop Comprehension, the result is printed inside a square bracket. EG:
'''
[print(y) for y in thislist]
# List Comprehension Example 2:

# using a normal for loop and if conditional statement to filter items and create a new list
fruitList = ["apple", "Mango", "orange", "star-apple", "cherry", "pawpaw", "guava"]
newFruitList = []
for item in fruitList:
    if "a" in item and len(item) == 5:
        newFruitList.append(item)
print(newFruitList)
print("\n")



# Using a List comprehension to create a new List based on certain conditions
'''
    Example 1:
'''
fruitList = ["apple", "Mango", "orange", "star-apple", "cherry", "pawpaw", "guava"]
newFruitList = [eachItem for eachItem in fruitList if "a" in eachItem and len(eachItem) != 6]

print(newFruitList)

'''
    Example 2:
'''
ranges = range(0, 10)
squares = [eachNumber **2 for eachNumber in (ranges)]
print(squares)




print("\n")

range1 = 8
print(range(range1))

for item in range(range1):
    print(item)



'''
    Maniputing a List of Items
'''

listItems = list(("Bright", "Ohakam", "Chidozie", "item1" ))
'''OR'''
listItems1 = ["Bright", "Ohakam", "Chidozie", "item1"]

#  1. Removing an Item from a List
# list.remove("item to be removed")
listItems.remove("item1")
print(listItems)



#  2. Adding and replacing an Item into a position in the List
# list.insert("index position number", "item to be added")
listItems.insert(4, "item2")

# OR
    # list.replace("item to be replaced", "substitute item")

print(listItems)

#  3. Adding an item at the end of a list
#  list.append("item to be added at the end of the list")


#  4. Changing the item in a list to another value
#  list[index number of Item] = "new value for the item at the index number"

#  5. Printing a specific item at a position in the list object
#  print(list[index number])
print(listItems[2])

#  6. Joining two different lists to forma single list
#  print(list1.exxtend(list2))
#  EXAMPLE:

print()
print()


list1 = ["Chidozie", "Ohakam", "Bright"]
print(list1)
list2 = ["Charlie", "Oscar", "Bravo"]
print(list2)
list1.extend(list2)
print(list1)





