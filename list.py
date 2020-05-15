# list data type examples
numbers = [1, 2, 3, 4, 5, 6]
strings = ['hello', 'world']
names = ["John", "Eric", "Jessica", 15]

second_name = names[1]


print(numbers)
print(strings)
print(names)
print("The second name on the names list is %s" % second_name)

print("\n The slice operator ([ ] and [:]) : ")
print(numbers[3])
print(numbers[0:5])
print(numbers[:3])
print(numbers[3:])


print("\n Concatenation and repetition operators : ")
print(numbers+strings)
print(numbers*5)
