'''
    You cannot copy a list simplyby typing "list1" = "list2", because; "list2" will only be a reference to "list1", and changes made in "list1" will automatically also be made in "list2".

    There are two ways to make a copy, one is to use the built-in List method "copy()" and the other is using the "list()" method
'''

# 1. Making a copy with "copy()" method

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# 2. Making a coopy with the built-in "list()" method

newList = list(thislist)
print(newList)
print()


# JOINING LISTS TOGETHER 
'''
    There are several ways to joini, or concatenate two or more lists in Python.
    One of the easiest ways are by using th "+" operator.
    EXAMPLES:
'''
# a. Using the "+" Operator to concatenate two or more lists
list1 = ["alpha", "beta", "Charlie", "Delta"]
list2 = [1, 2, 3, 4,]

list1 =list1 + list2
print(list1)
print()

#  b. Using the "append()" method to join two or more lists together.

list3 = ["Hello", "I", "am", "Bright"]
for x in list3:
    list1.append(x)

print(list1)
print()


# c. Using the "extend()" method to join elements from one list to another

list4 = ["10", 11, 12, 15]

list1.extend(list4)
print(list1)
list1.clear()
print(list1)





