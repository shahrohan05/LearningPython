# Python I/O
import os

# Console I/O
row_input = input("Your Name: ")
print("Hello World!" if row_input == "" else "Hello "+row_input)


# File I/O
test_file = open("test_file.txt", "wb")

print("file name : ", test_file.name)
print("closed? : ", test_file.closed)
print("file opening mode : ", test_file.mode)

test_file.write(
    b"Python is a fun to learn language!\n\n Uummm... one more thing, not having semicolons is a bit weird to be honest.")

test_file.close()


filename = input("Further read from(Enter filename) : ")

userfile = open(filename, "r+")

print("user file current position - ", userfile.tell())

position = input("Read from file until? - ")

print("Content from file ", userfile.read(int(position)))

print("current user file position - ", userfile.tell())

userfile.seek(0, 0)

print("all user file data - ", userfile.read())

userfile.close()

# OS module and directories

print("Current Working Directory : ", os.getcwd())

directory_to_create = input("Directory to create : ")

os.mkdir(directory_to_create)

tobe_renamed = input("Directory to be renamed to : ")

os.rename(directory_to_create, tobe_renamed)

filename_tocreate = input("File to create in the new directory : ")

os.chdir(tobe_renamed)

file_tocreate = open(filename_tocreate, "wb")

file_tocreate.write(b"A new file created for testing purpose!")
file_tocreate.close()

remove_directory = input("Clean up the mess? ")

if(remove_directory.lower() == "yes"):
    os.remove(filename_tocreate)  # Remove the created file
    os.chdir("..")  # go up a directory
    os.rmdir(tobe_renamed)  # remove the created directory
