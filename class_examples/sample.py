import pickle


# Sample class definitions
class SampleClass:
    """A Sample class"""
    def __init__(self):
        self.x = 15

    x = 20
    y = 30

    def print_sample(self):
        print("X : %d, Y: %d, Z: %d" % (self.x,self.y, self.z))


# Class object use 1. Attribute Reference
SampleClass.z = 60
print("Sample Class - X : %d, Y : %d, Z : %d " % (SampleClass.x,SampleClass.y,SampleClass.z))
print(SampleClass.print_sample) # prints info, as SampleClass.print_sample is a function object of
# the Object Class SampleClass and defines corresponding methods for its instances.
# So, essentially, SampleClass.print_sample is a function object defining method print_sample()
# for instance objects of SampleClass
# i.e. Method is a function that belongs to an object


# Class object use 2. Instantiation: ClassName() + __init__()
# sample1 is an instance object of class SampleClass
sample1 = SampleClass()

# Data  attributes for class and instance objects spring into action when they are first assigned.
# *** This applies to objects of type class and instance only, this does not apply to objects of built in types.
sample1.z = 66  # If this line were to be commented, the print_sample would print the value of the class object's data
# member z, which is 60.

sample1.print_sample()
print(sample1.print_sample)  # A bound method of function object SampleClass.print_sample

SampleClass.print_sample(sample1)  # This is same as calling sample1.print_sample()


# So, difference between method object and function object?
def test_function():
    print("Test!")


print(test_function)

# 1. Functions - functions in python are first class objects, following definition of test_function,
# we create an object of type function in object space and map it with name "test_function" in the global
# name space of this sample module. For further samples - check : function_samples.py

# 2. Method - methods are essentially functions with first argument pre-filled with instance (self). This pre-filling
# makes it a bound method. This is evident in SampleClass.print_sample(sample1) == sample1.print_sample()

