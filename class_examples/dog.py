# Sample class to check distinction between class and instance variables for both mutable and immutable tyeps

# A name in global scope of the dog module, i.e. dog.py
dog_class = "For all Dogs"


class Dog:

    type = "canine"  # Class level immutable member
    tricks = []  # Class level mutable member

    def __init__(self,name):
        self.name = name  # Instance level member
        self.tricks = []  # This ensures the mutable member tricks is referring to a separate
        # list object for each instance of Dog class.
        # Commenting this would result in all instances referring to the class level "tricks" member

    # The first parameter "self" for class's member functions is a convention and has no other special meaning.
    # Changing the name of this parameter does not break the program, but following the convention of naming
    # the first parameter self is a good idea, since this makes the program more readable for other programmers
    # and the client program using the class may be written in such a way, that it relies upon such convention.
    def add_trick(self1,trick):
        self1.tricks.append(trick)

    # Methods can call other methods by using method attributes of the self argument.
    # i.e. add_trick method attribute can be called upon by other methods of the self argument.
    def add_two_tricks(self,trick1,trick2):
        self.add_trick(trick1)
        self.add_trick(trick2)

    # global scope associated with method members of the class is the module containing its definition
    def __call__(self, *args, **kwargs):
        print(dog_class)
        print("Dog name : %s, Type: %s, Tricks: %s" % (self.name,self.type,self.tricks))


if __name__=="__main__":
    madmax = Dog("Madmax")
    tucker = Dog("Tucker")

    Dog.tricks.append("Smile")

    madmax.type = "fluffy"  # This means the madmax instance of Dog class now has instance member type
    # if such instance member with the same name is not provided for any instance it will
    # point/look up to the class member type i.e instance tucker still points to class member type

    madmax.add_trick("Fetch bear")
    tucker.add_trick("Hand shake")
    tucker.add_two_tricks("Puppy eyes","Goofy face")

    print("For Dog class : type : %s, tricks: %s" % (Dog.type,Dog.tricks))

    madmax()
    tucker()

    # Each value is an object and therefore has a class(also called its type), which can be accessed as object.__class__

    print(tucker.__class__)

    # Abstraction or encapsulation, i.e. enforcing no instantiation and hiding implementation details
    # is not possible in pure python, but the same is achievable in Python implementation written in C.
    # e.g. you cannot bind random members / attributes to an objects of builtin type list.

    list1 = [1,2,3]
    #list1.x = "test"  # This will result in an AttributeError


