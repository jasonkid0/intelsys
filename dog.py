# class Dog:
#     ## this is a method that a dog is able to do.
#     ## a method is a function of a class
#     def bark(self):
#         return "bark"

# ## here im Instantiating like creating a new Instance of the class Dog() 
# ## d is now going to be an Object of type dog
# d = Dog()
# print(d.bark())

## -------------------------------------------------------------------

# class Dog:
#     def __init__(self, name, age): ## inside the parenthesis is called (parameters)
#         ## everytime whenever self is called in the paramater kindly invisibly reference to the Dog() object
#         self.name = name  
#         self.age = age ## self.age age in self.age is an ATTRIBUTE/properties
#         print(name, age)

# ## here im Instantiating like creating a new Instance of the class Dog() 
# ## d is now going to be an Object of type dog
# d = Dog("Brownie", 2)
# d = Dog("Whitie", 5) 

## -------------------------------------------------------------------

class Guitar:
    def __init__(self):
        self.n_strings = 6
        self.play()
        
    def play(self):
        print ("pam pam pam pam pam pam")

my_guitar = Guitar()
print(my_guitar.n_strings)