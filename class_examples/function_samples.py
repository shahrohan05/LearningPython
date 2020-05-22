# Samples demonstrating the benefits of functions being high level objects in Python


# 1. Passing functions as argument to other functions, routine to apply any function to a list
def apply(list_obj, func):
    applied_list = []
    for i in list_obj:
        applied_list.append(func(i))
    return applied_list


list1 = [1, 2.5, 3.3, 4.7, 5.9]
print(apply(list1, int))  # applying int() function to each element of the list
print(apply(list1, str))  # applying str() function to each element of the list

# 2. Functions as elements of list or other collection types - see basics.py

# 3. Functions can be assigned to other variables
apply_fun = apply
print(apply_fun(list1,str))  # Works the same as calling apply directly


# 4. Objects as Functions: Objects can be called upon just like functions by defining a __call__ method inside it
class Student:
    def __init__(self,name):
        self.name = name

    def __call__(self):
        print("Student : "+self.name)


s1 = Student("Samir Bhatt")
s1()
