# List data type examples
numbers = [1, 2, 3, 4, 5, 6]
strings = ['hello', 'world']
names = ["John", "Eric", "Jessica", 15]

second_name = names[1]


print(numbers)
print(strings)
print(names)
print("The second name on the names list is %s" % second_name)

print("hello in strings? - %s" %
      str("hello" in strings))  # in operator for list type

print("\n The slice operator ([ ] and [:]) : ")
print(numbers[3])
print(numbers[0:5])
print(numbers[:3])
print(numbers[3:])


print("\n Concatenation and repetition operators : ")
print(numbers+strings)
print(numbers*5)


# Tuples - read-only lists, enclosed in parantheses instead of square brackets:
member1 = (1, "Monty Python", "Main Comedian",
           "104K, Python Test Center, Python land-19")
temp_member2 = (2, "Jordan Belfort")

print(member1)
print(member1[1:])
print(member1[1:3])
print(temp_member2 + member1)
print(temp_member2*3)

# Dictionary - a hash table like data structure
map = {}
map[1] = 'test'
map['test'] = 1

map2 = {15: 'test 15', 16: 'test 16', 'test 17': 17}

print(map)
print(map2)
print(map2.keys())
print(map2.values())
print(map2[16])

# List Comprehension
l1 = [2, 2, 2, 2]
l2 = [i*2 for i in l1]
print(l2)

# Dictionary Comprehension
d1 = {1: "sam", 2: "sam 2"}
d2 = {k: d1[k].upper() for k in d1.keys()}
print(d2)

# Sets in Python
thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "banana"])

# Set Comprehension
uppercase_set = {i.upper() for i in thisset}
print(thisset)
print(uppercase_set)
