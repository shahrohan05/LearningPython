# Functions in python

# print_me("test"), being an interpreted language, in Python calling function before it is defined results in NameError


def print_me(msg):
    """Prints the provided msg parameter onto the console."""
    print(msg)


print_me("Hello World!")
print_me("Another string!")


# Python is pass-by-object-reference i.e. the references to the same objects in the memory are passed to the
# functions but the variables holding the reference are local to the function. Which means, mutating the passed
# object will be reflected in the outer reference(variable) as well but re-assigning the method local parameter
# variable will not be reflected in the outer(passed) variable.

# Python function parameters act like pass-by-value in case of immutable types.
def test(
        local_age):  # Age still points to the same integer type object in the memory, but the local reference for
    # this method "local_age" is different from outer reference "age".
    """Test function to update the age parameter to 15."""
    print("Age as passed - ", local_age)
    # This re-assignment is not mutation, it creates new integer object in memory and assigned it to local variable
    # "local_age", outer variable "age" is not affected by this.
    local_age = 15
    print("Age updated to - ", local_age)


age1 = 22
test(age1)
print("Age after function - ", age1)


# Python functions act like pass-by-reference in case of mutable objects
def test2(list2):
    """Test function to append 55 to the passed list type object."""
    list2.append(55)
    print("List inside the function - ", list2)


list1 = [1, "test"]
test2(list1)
print("List outside the function - ", list1)

"""Python function argument rules : 1. Required - all arguments are required by default, unless specified with 
default value or as variable length argument tuple 2. Keyword - passing arguments to a function with keywords(
argument names) to avoid passing in order 3. Default - declaring arguments with default values, these become optional 
to be passed while calling the function. 4. Variable length - declaring multiple variable length arguments to be 
accepted by a function as a tuple with *(asterisk) sign. 

** -  A variable length argument cannot be assigned default value, it remains an empty tuple if nothing is passed by 
the calling function. Also, all arguments post the variable length arguments, automatically become, keyword-only 
arguments, so the interpreter knows, when to stop the variable length arguments stop and when the next argument 
starts. """


def print_person(name, age=15, *hobbies, gender):
    print("----------PERSON-------------")
    print("Name : ", name)
    print("Age : ", age)
    print("Gender : " + gender)
    print("Hobbies : ", hobbies)


print_person("Sanjay Bhatia", 20, "Swimming", gender="Male")

# Function variable scopes

total = 15  # Global variable


def sum_test(i, j):
    # total is accessible here as a global variable
    print("Total before sum : ", total)
    # Changing this variable name to total, will result in creation of a local variable called "total",
    # for this method block.
    total2 = i + j
    # Which results in Error in previous statement, as in that case "total" is referenced before assignment.
    print("Total after sum : ", total2)


sum_test(15, 20)
print("[Sum Test] Total value - ", total)


# Return statement
def sum1(i, j):
    return i + j


print("[Sum] Total value - ", sum1(15, 20))

# Anonymous function, lambda keyword to create small anonymous functions
"""
1. Can take n number of arguments, but can only return one value in the form of an expression
2. Cannot be a direct call to print, must return from an expression
"""


def sum_operation(arg1, arg2): return arg1 + arg2


print("[Sum Lambda] Total value - ", sum_operation(15, 15))
