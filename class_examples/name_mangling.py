# Class name mangling and iterator

class Person:

    def __init__(self,name):
        self.name = name

    def __walk(self):
        print("Person walks!")


class Student(Person):

    def __call__(self, *args, **kwargs):
        print("Student Name : %s " % self.name)

    def __walk(self):
        print("Student walks!")


class StudentList:

    def __init__(self,data):
        self.data = data

    # To make the class iterable we can define the __iter__() method such that it returns the
    # object with __next__() function defined in it
    def __iter__(self):
        return StudentIterator(self)


# The __next__() function could also be defined in the student class, but by defining this separately
# we can keep the iteration logic separate from the list class and can be used with some other
# similar collection type object.
class StudentIterator:

    def __init__(self,studentList):
        self.studentList = studentList
        self.index = 0

    def __next__(self):
        if self.index == len(studentList.data):
            raise StopIteration
        self.index = self.index + 1
        return self.studentList.data[self.index-1]


# Generators : student list reverse generator, a way to implement iterator.
def student_list_reverse_generator(studentList):
    for i in range(len(studentList)-1,-1, -1):
        yield studentList[i]

if __name__ == "__main__":
    ramesh = Student("Ramesh")

    ramesh._Person__walk()
    ramesh._Student__walk()

    print(ramesh._Person__walk.__self__) # Instance object associated with ramesh._Person__walk
    print(ramesh._Person__walk.__func__) # Function object associated with bound method ramesh._Person__walk

    # ramesh.__walk() # Throws AttributeError
    ramesh()

    print("-------------------------------------------")
    studentList = StudentList([Student("Samir"),Student("Sanjay"), Student("Soham"),Student("Samir"), Student("Dhwanil")])

    for student in studentList:
        student()
    print("-------------------------------------------")
    for student in student_list_reverse_generator(studentList.data):
        student()

    # Generator Expression, similar to list comprehension
    unique_student_names = set( student.name for student in studentList)

    # This is exactly similar to set comprehension
    unique_student_names1= {student.name for student in studentList}

    print(unique_student_names)
    print(unique_student_names1)


