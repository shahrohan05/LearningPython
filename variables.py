# Numbers and string data types examples
my_string = "hello"
my_float = 10.0
my_int = 20

if my_string == "hello":
    print("String: %s" % my_string)
if isinstance(my_float, float) and my_float == 10.0:
    print("Float: %f" % my_float)
if isinstance(my_int, int) and my_int == 20:
    print("Integer: %d" % my_int)

print()
print()

print("Escaped String : \n \"Monty Python's Flying Circus\" \n\n")
print('One more: \n "Monty Python\'s Flying Circus"\n\n')

# A raw string, not treating \n as special.
print(r"a row string  - \n \"Monty Python\'s Flying Circus")


# Multi-line string, can also be created using single quotes, but double quotes are recommended.
print(""" a
multi line
string in python """)

"""  Useful as Documentation String or docstring for documenting method contracts/purpose
This is a 
multi-line
comment.
"""

# Two or mote string literals next to each other are automatically concatenated.
another_string = "another" " string"

print("\n Another String : "+another_string)

print("\n 1st character of another string : "+another_string[0])
print(" 1 to 5 character of another string : "+another_string[0:5])
print(" 1 to 5 character of another string : "+another_string[:5])

print(" characters from 5th character of another string : "+another_string[5:])

# Multiple assignment
a, b, c = 15, 15.5, "hello"
print(a, b, c)

# String repetition
print('Circus Clown, '*3)

# Deleting variables: when you are sure you will never need the variable again in the program, or in situations where
# you can predict you may run out of memory.
del a, b, c
# This will throw NameError, since variables are deleted and no longer defined.
print(a, b, c)
