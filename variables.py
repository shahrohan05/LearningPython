mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
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

print(r"a row string  - \n \"Monty Python\'s Flying Circus") # raw string without treating \n as special.

print(''' a
multi line
string in python ''')

""" 
This is a 
multiline
comment.
"""

anotherString = "another" " string" # two or mote string literals next to each other are automatically concatenated.

print("\n Another String : "+anotherString)

print("\n 1st character of another string : "+anotherString[0])
print(" 1 to 5 character of another string : "+anotherString[0:5])
print(" 1 to 5 character of another string : "+anotherString[:5])

print(" characters from 5th character of another string : "+anotherString[5:])

