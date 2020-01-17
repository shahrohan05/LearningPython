""" 
Create a python class Author. Create a python class for Programming languages which must inherite Author class. Create a class which should print the details of given programming language as input.

"""
class Author:
    def setAuthor(self,name):
        self.name=name
    def getAuthor(self):
        return self.name
class ProgrammingLanguage(Author):
    def python(self):
        return self.getAuthor()+" has written book for python"
    def java(self):
        return self.getAuthor()+" has written book for java"
class PrintProgrammingLanguage(ProgrammingLanguage):
    def printDetails(self,language):
        if language=="python":
            print(self.python())
        elif language=="java":
            print(self.java())    
def main():
    print=PrintProgrammingLanguage()
    print.setAuthor("admin")
    input_language=input("Enter the programming language:")
    print.printDetails(input_language)
main()    
