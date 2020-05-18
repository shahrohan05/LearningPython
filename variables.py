# Numbers and string data types examples
mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

print()
print()

print("Escaped String : \n \"Monty Python's Flying Circus\" \n\n")
print('One more: \n "Monty Python\'s Flying Circus"\n\n')

# A raw string, not treating \n as special.
print(r"a row string  - \n \"Monty Python\'s Flying Circus")


# Multiline string, can also be created using single quotes, but double quotes are recommended.
print(""" a
multi line
string in python """)

"""  Useful as Documentation String or docstring for documenting method contracts/purpose
This is a 
multiline
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

# Deleting variables: when you are sure you will never need the variable again in the program, or in situations where you can predict you may run out of memory.
del a, b, c
# This will throw NameError, since variables are deleted and no longer defined.
print(a, b, c)
