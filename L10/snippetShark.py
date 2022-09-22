class Shark:

    # Class variables
    animal_type = "fish"
    location = "Indian Ocean"

    # Constructor method with instance variables name and age
    def __init__(self, nameStr, ageNmbr):
        self.name = nameStr
        self.age = ageNmbr

    # Method with instance variable length in [meter]
    def set_length(self, length):
        print("This shark has a length of " + str(length) + " meter.")
        
        
# Create a instance, passing an instance variable to constructor method


# Print out instance variable name


# Print out the living location of the shark (maybe in a sentence?!)


# Create a second Shark instance


# Print out instance variable name


# Use set_length method and pass length instance variable


# Print out class variable animal_type


# After performing the previous tasks, doe your first shark have a length yet?


# You cannot call the length variable from outside the function, 
# because it is not defined as instance variable (referenced with self).
# Change the class code to be able to do that!