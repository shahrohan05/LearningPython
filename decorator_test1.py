def multiply_with(multiplier):
    def multiplier_decorator(func):
        def multiplier_function(*args):
            print("Returning value returned from {} multiplied by {}".format(func.__name__,multiplier))
            return func(*args)*multiplier
        return multiplier_function
    return multiplier_decorator

@multiply_with(2)
def add_numbers(x,y):
    return x+y

@multiply_with(4)
def multiply_numbers(x,y):
    return x*y

print(add_numbers(5,5))
print(multiply_numbers(4,2))