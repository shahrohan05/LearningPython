def print_steps(func):
    def helper(*args,**kwargs):
        print("Calling {}".format(func.__name__))
        print(func(*args,**kwargs))
        print("Done calling {}".format(func.__name__))
    return helper

@print_steps
def add_numbers(a,b):
    return a+b

@print_steps
def multiply_numbers(a,b):
    return a*b

add_numbers(5,6)
multiply_numbers(5,6)



