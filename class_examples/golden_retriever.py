# Inheritance in python classes
from dog import Dog


class GoldenRetriever(Dog):
    fur_color = "golden"

    # Base class(Dog) method can be called from child class methods, by either 1. BaseClassName.methodName(provided
    # BaseClassName is accessible in global scope of the module in which the child class is defined) or 2.
    # self.methodName, in case the method is not overridden in the child class
    def __init__(self, name, highlight_feature):
        Dog.__init__(self, name)
        self.highlight_feature = highlight_feature # Instance memeber of the GoldenRetriever child class instances
        Dog.add_trick(self, "Retrieve shot game")  # Calls add_trick from base class dog
        self.add_trick("Zoomies")  # Calls add_trick from child class GoldenRetriever

    # overriding of method simply occurs when we difine a method with the same name as that of the base class.
    def add_trick(self,trick):
        trick = "GOLDEN : "+trick
        Dog.add_trick(self,trick)

    def __call__(self, *args, **kwargs):
        Dog.__call__(self)
        print("GOLDEN R. Fur color : %s, Highlight Feature : %s" % (self.fur_color, self.highlight_feature))


if __name__ == "__main__":
    marlin = GoldenRetriever("Marlin", "Friendly and confident");
    marlin()
