# SETS: 
'''
    sets are used to store multiple items in a single variable.
    Set is one of 4 built-in data types in Python used to store collections of data, the othr 3 are List, Tuple, and Dictionary, all with different qualities and usage.

    A set is a collection which is unordered, unchangeable and unindexed.
    Set items are unchangeable, but you can add or remove items from a set.
    Set items do not also allow duplicate characters or items inside it too.

    Set collections can appear in any order or arrangement anytime you use them.
    Example:
'''

thisset = {"set1", "set2", "set3", "mango"}
print(thisset)
print(type(thisset))
print()

# ADDING ITEMS INTO A SET USING THE "add()" method

thisset.add("set4")
print(thisset)
print()




# REMOVING A SET ITEM WITH "remove()" or "discard()" methods
# Using the "remove()" method
thisset.remove("mango")
print(thisset)
print()

# Using the "discard()" method
thisset.discard("papaya")
print(thisset)
print()

# REMOVING A RANDOM ITEM FROM THE SET USING "pop()" method
removedItem = thisset.pop()
print(removedItem)
print(thisset)



# JOINING TWO SETS TOGETHER WITH THE "update()" and "union()" methods
# NB: "update()" method can be used to join the "set" collection with any other collection datat type like "list", "tuples" or even a "dictionary".

# The "update()" method inserts all the items from one set into another.
# EXAMPLE:
tropical = set(("pineaple", "mango", "papaya"))
print(tropical)
thisset.update(tropical)
print(thisset)
print()

# The "union()" method returns a new set with all itens from both sets:

set1 = {"a", "b", "c", "d"}
set2 = {1, 2, 3, 4}
set3 = set1.union(set2)
print(set3)
print()


# KEEPING ONLY DUPLICATES IN SETS USING THE "intersection_update()"
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)
y.intersection_update(x)
print(y)
print()


# "intersection()" method will return a new set, that only contains the items that are present in both sets.

newX = {"apple", "banana", "cherry"}
newY = {"google", "microsoft", "apple"}
newZ = newX.intersection(newY)
print(newZ)
print()


# "symmetric_difference_update()" method will keep only the elements that are NOT present in both sets.
# EXAMPLE:
newX.symmetric_difference_update(newY)
print(newX)
print(newY)

# The "symmetric_difference()" method returns a new set, that contains only the elements that are NOT present in both sets.

anotherSet = newX.symmetric_difference(newY)
print("Hello, these sets are \"symmetric differences\" ", anotherSet)
print()

# NB: In a set "True" and the number "1" are considered to be the same value; hence they cannot be inserted in the same set.
checkForDuplicate = set(("Bright", "Ohakam", True, 1))
print(checkForDuplicate)





# EMPTING THE SET WITH THE "clear()" method

thisset.clear()
print(thisset)
print()


# DELETING AN ENTIRE SET WITH THE "del" keyword
del thisset
# print(thisset)




