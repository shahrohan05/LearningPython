# If condition
a, b = 15, 20
if(a > b):
    if_loop_test = 55
    print("a is greater than b")
else:
    print("b is greater than a")

print("both a and b are equal" if a == b
      else "a is greater than b" if a > b else "b is greater than a")

# While loop
print("\n\nWhile loop :")
while True:
    b -= 1          # Decrement b by 1 with each iteration
    if(b < -20):    # Break loop upon reaching -20
        break
    if(b > -18):
        continue    # Move to next iteration, withour executing following code, until -18
    print(b)
print("While loop over")


# For loop
names = ["John", "Doe", "Sam", "Mark", "Peter", "Harry", "Kane", "Jeff"]
print("\n\nFor loop: ")
for name in names:
    if name == "Mark":
        continue  # Skip printing Mark
    print(name)
print("For loop over")

# Range
print("\n\nRange based for loop")
for i in range(len(names)):
    print(names[i])

# Else in for loop, routine to print prime numbers between given range
for i in range(10, 20):
    for j_test in range(2, i):
        if i % j_test == 0:
            print("For %d, %d %% %d == 0" % (i, i, j_test))
            break
    else:  # This is executed when for loop is exausted and not when broken using break statement
        print("%d is prime." % i)

# In Python, loop variables are available after exiting the loop code block
print(j_test)
# But, the same is not true for other code block variables, e.g. if_loop_test is not accessible outside the code block
# print(if_loop_test)  This will result in a NameError

# Else in while loop
while(i > 0):
    i -= 15
else:  # This is executed when the while loop condition becomes false
    print("While over with i = %d" % i)


# Pass in loop, doea nothing but useful as a syntactical placeholder for future code
for letter in "PYTHON":
    if(letter == "H"):
        pass  # Will implement this feature in future.
    print(letter)
