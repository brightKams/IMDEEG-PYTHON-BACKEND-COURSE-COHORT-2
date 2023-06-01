'''
    DICTIONARIES:
    "dictionaries" store connections between pieces of information. Each item in a dictionary is a key-value pair.
    Exampl:
'''
# A simple dictionary:
alien = {
    "color": "green", 
    "points": 5
    }
print("alien color is " + alien["color"])

# Adding a value to a dictionary

alien["name"] = "Bright"
print(alien)

# Traversing or Looping through a dictionary
'''
    Traversing or looping through a dictionary, can be done in three ways; either lopping through the "key-value pairs" or only the "Keys" or only the "Values"
    
    Looping through the value Pairs:
    two keys are used, one for the key and the other is for the value.
    Example1:
'''
fav_numbers = {"Eric": "17", "Ever": 4}
for name, number in fav_numbers.items():
    print(name + " is number " + str(number) )
print()

# Example 2:
# LOOPING THROUGH ONLY THE "KEYS" IN A "DICTIONARY"

for key in fav_numbers.keys():
    print( key, "is a key value")
print() 


# Example 3:
# LOOPING THROUGH ONLY THE "VALUE" IN A "DICTIONARY"

for value in fav_numbers.values():
    print(value, "is a value in the dictionary")
print()



