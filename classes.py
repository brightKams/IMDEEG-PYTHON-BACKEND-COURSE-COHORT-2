    # CLASSES:

    # 1.  A class defines the behavious of an object and the kind   of information an object can store. 

    # 2. The information in a class is stored in attributes, and functions that belong to a class are called methods. 
    
    # 3. A child class inherits the attributes and methods from its parent class.

# EXAMPLE:
class Dog():
    ''' Represent a dog. '''
    def __init__(self, name) :
        """ Initialize dog object."""
        self.name = name
    def sit(self):
        """ Simulate sitting. """
        print(self.name + " is sitting.")
my_dog = Dog("Peso")
print(my_dog.name + " is a great dog!")
my_dog.sit()