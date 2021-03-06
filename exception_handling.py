# Exception handling and assertions in Python

# User defined exception
class SecretFileException(BaseException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def readfile(filename):
    try:
        file = open(filename, "r")
        if(filename == "collection_types.py"):
            raise SecretFileException(
                "Collection types is a secret file, cannot be read from!")
        print(file.read())
        # j = 5/0  # Will throw ZeroDivisionError
        # print(jam)  # Will throw NameError
    except FileNotFoundError as fnfe:  # Catching FileNotFoundError
        print(fnfe.strerror)
        if(input("Would you like to try again? (yes/no) :").lower() == "yes"):
            readfile(input("File to read from :"))
        else:
            print("Exiting routing based on user choice.")
    except (IOError, ZeroDivisionError) as e:  # Catching IOError or Arith
        print(e)
        print("IOError or ZeroDivisionError, exiting the routine now.")
    except SecretFileException as e:
        print("User tried accessing a secret file. Must report the incident!")
        print(e)
    except Exception as e:  # Catching any other error
        print(e)
        print("Some unknown error occurred!")
    else:
        print("\n\n[NO EXCEPTION]File read successfully...............")
    finally:
        print("Finally trying to close the file %s." % filename)
        try:
            file.close()
        except Exception as e:
            print("Error closing the file %s : " % filename, e)


readfile(input("File to read from :"))
