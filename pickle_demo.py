# Python pickle module for serialization(pickling) and deserialization(unpickling) This module is different from json
# in the sense that, 1. It works faster as it serializes to and deserializes from binary format, which is not human
# readable as compared to human readable form of json serialization. 2. it is useful in serializing non built-in
# custom type objects, something json module is incapable of.

# ** There are several ways to serialize custom type object to and from json type, jsonpickle is one additional module,
# that one can download fot this purpose.

import pickle

class Student:

    def __init__(self,name,grade,address,friends,marks):
        self.name = name
        self.grade = grade
        self.address = address
        self.friends = friends
        self.marks = marks

    # Custom pickling
    def __getstate__(self):
        attributes = self.__dict__.copy()
        del attributes['grade']
        return attributes


s1 = Student(
    "Sanjay Thakur","B-",["44-Kamdar Street","Jambunagar","Nagpur","India"]
    ,{"Gopinath Bhalla":"A+","Bhaginath Aluvaliya":"C-"},{"Maths":55,"Science":89,"History":"70"})

print(s1.__dict__)

print("Default pickle protocol - ",pickle.DEFAULT_PROTOCOL)
print("Highest pickle protocol - ", pickle.HIGHEST_PROTOCOL)

my_pickled = pickle.dumps(s1,5)

print("\n Pickled: ",pickle.dumps(s1))

s2 = pickle.loads(my_pickled)

print("\n Unpickled : ",s2.__dict__)

# reading csv
import csv

items = csv.reader(open("test_file.txt","r"), delimiter = ';')
for item in items:
    print(item)

new_items = ["abc","xyz","ddd","some other data"]
to_file = open("test_file.txt","w")
item_writer= csv.writer(to_file, delimiter = ';')
item_writer.writerow(new_items)
item_writer.writerow(["new items","are new after all"])
to_file.close()
