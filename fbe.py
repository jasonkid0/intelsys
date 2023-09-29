
# def hello():
#     print("hello1")

# x=1
# name = "Jisun"
# print(type("hello"))
# print(type(x))
# print(type(hello))

# ## method "upper()" that is acting on a "name" object
# print (name.upper())

class Dog:
    ## this is a method that a dog is able to do.
    ## a method is a function of a class
    def bark(self):
        print("bark")
    
    def __init__(self, name, age): ## inside the parenthesis is called (parameters)
        ## everytime whenever self is called in the paramater kindly invisibly reference to the Dog() object
        self.names = name  
        self.age = age ## self.age age in self.age is an ATTRIBUTE/properties
        
    def get_name(self):
        return self.names
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        return self.age
        
    
    
        
    def add_one(self, x):  ## the x here is a PARAMETER
        return x+1


## here im Instantiating like creating a new Instance of the class Dog() 
## d is now going to be an Object of type dog
d = Dog("Brownie",2)
print(d.names) ## print the attribute in self names that we can call wahtever we want let say names
print(d.get_age())

d2 = Dog("Whitie", 4)
print(d2.names)
print(d2.get_age())
## this is how we call the method bark()
d.bark() ## how to output a method  bark() and partner with the instantiation d = Dog()
#print(type(d))

## how to output a method  add_one() nd partner with the instantiation d = Dog() 
# note this is the best practice to output a method
print(d.add_one(5))
