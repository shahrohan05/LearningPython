import pickle
from golden_retriever import GoldenRetriever
from poodle import Poodle
from dog import Dog


class GoldenDoodle(GoldenRetriever,Poodle):

    fur_color = "golden"

    def __init__(self,name,highlight_feature):
        GoldenRetriever.__init__(self,name,highlight_feature)
        Poodle.__init__(self, name, highlight_feature)


if __name__ == "__main__":
    ellie = GoldenDoodle("Ellie","Friendly, confident and alert")

    # There is a diamond relation here, the __call__() method is found in each of the base classes
    # inherited attributes are resolved as depth-first, left-to-right manner, meaning
    # it will find the attribute/method in the child class first and then search through
    # the base classes, starting from left (and its base class) to right (and its base class)
    # this is evident in the fact that following will end up calling the __call__() from GoldenRetriever class
    ellie()

    # Serializing and de-serializing a custom object
    ellieStr = pickle.dumps(ellie)
    print(ellieStr)
    ellie2 = pickle.loads(ellieStr)
    print("ellie id - {}".format(id(ellie)))
    print("ellie2 id - {}".format(id(ellie2)))

    print("calling on ellie 2 :")
    ellie2()
