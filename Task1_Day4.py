"""
Create a python class Author. Create a python class for Programming languages which must inherite Author class. 
Create a class which should print the details of given programming language as input.

"""
class Author:
    def __init__(self, language):
        if language == "Python":
            self.auth_name = "Malav"
        elif language == "Java":
            self.auth_name = "Rahul"

    def Auth_Name(self):
        return self.auth_name
            
class ProgrammingLanguage(Author):
    def __init__(self, language):
        super().__init__(language)
        if language == "Python":
            self.detail = "It uses Interpreter"
        elif language == "Java":
            self.detail = "It uses Compiler"

    def Detail(self):
        return self.detail

class PrintDetails:
    def print_details(self, language):
        pl = ProgrammingLanguage(language)
        try:
            print(pl.Auth_Name())
            print(pl.Detail())
        except AttributeError:
            print("Please enter a valid language")
        
try: 
    language = input("Enter Programming Language:")
    pd  = PrintDetails()
    pd.print_details(language)

except ValueError:
    print("Please enter string only")