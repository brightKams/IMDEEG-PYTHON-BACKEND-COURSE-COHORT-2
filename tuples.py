'''
    TUPLES:
    Tuples are similar to lists but the items are not mutable. 
    Tuples can contain multiple data types in Python
    To create a tuple with only one item, you will have to add a comma after the item
    Example:
'''
tupleItems = ("Bright", "Ohakam", 5, True, False)

iteration = 0
for name in range(len(tupleItems)):
    print( str(iteration) + ":" + tupleItems[iteration])
    iteration = +1
print(type(iteration))


literalComment = '''newRange = range(8)
                    for item in newRange:
                        print(item)'''
print(literalComment)
print()

# Creating a single Tuple in Python

# a.  This is not a tuple object but a string
notASingleTuple = ("apple")
print(type(notASingleTuple))
print()

# b. This is a tuple object because it has a comma after the  
singleTuple = ("apple",)
print(type(singleTuple))
print()

# Using a Tuple Constructor to make a Tuple

# It is also possible to use the tuple() constructor to make a tuple.

tupleConstructor = tuple(("tuple1", "tuple2", "tuple3", "tuple4" ))
print(type(tupleConstructor))
print()

# Converting a Tuple into alist using the "list()" constructor
tupleToList = list(tupleConstructor)
print(tupleToList)
print(type(tupleToList))


