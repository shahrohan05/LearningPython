
class Sorting:

    def __init__(self,data_list,algorithm_method):
        self.list = data_list
        self.sort_method = algorithm_method

    def sort(self):
        print(self.sort_method)
        return self.sort_method(self.list)

