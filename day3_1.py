'''"Write a function that given a string it returns true if the string is a number. As there might be several definitions of what is the number create several solutions one for each definition:
   Non negative integer.
   Integer.
   Real number.
   In scientific notation. (something like this: 2.123e4 )"'''

import re
number=input("Enter a number")
if re.fullmatch(r"[0-9]*",number):
    print("Non negative integer")
elif re.fullmatch(r"[\-][0-9]*",number):
    print("Integer")
elif re.fullmatch(r"[-\][0-9]*.[0-9]*",number):
    print("Real number")
elif re.fullmatch(r"[0-9]*[\.][0-9]*[e,E][-]?[0-9][\.]?[0-9]*",number):
    print("Scientific notation")
else:
    print("It is not valid number")