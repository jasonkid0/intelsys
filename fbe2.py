class Dog:
    ## this is a method that a dog is able to do.
    ## a method is a function of a class
    
    def __init__(self, name, age): ## inside the parenthesis is called (parameters)
        self.name = name  ## everytime whenever self is called in the paramater kindly invisibly reference to the Dog() object
        self.age = age ## self.age age in self.age is an ATTRIBUTE
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        return self.age