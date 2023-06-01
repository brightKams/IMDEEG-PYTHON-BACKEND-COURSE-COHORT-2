# PYTHON - SORT LISTS


# sort List Alphanumerically:
'''
    list objects have a "sort()" method that will sort the list alphanumerically, ascending, by default. It is also case sensitive as capital letters are sorted before lower case characters:
'''
# 1. Sorting in Ascending Order

# a. sorting alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
print()

# b. sorting numerically
thisList = [100, 50, 65, 82, 23]
thisList.sort()
print(thisList)
print()

# 2. Sorting in Descending Order

# To sort descending, use the keyword argument "reverse = True"

# a. sorting alphabetically
thislist.sort(reverse = True)
print(thislist)
print()


# b. sorting numerically

thisList.sort(reverse = True)
print(thisList)
print()


# REVERSING THE POSITION ORDER OF A LIST ITEM BASED ON INDEX NUMBER
# "reverse()" method

thislist.reverse()
print(thislist)
print()

# Performing a case-insensitive sort for the list:
# "key = str.lower" built-in functions
thislist.sort(key = str.lower)
print(thislist)
print()
