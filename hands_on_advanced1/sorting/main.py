from algorithm import Algorithm
from sorting import Sorting

algorithm_choices = """
Please choose an algorithm to sort with:
1. Quick Sort
2. Bubble Sort
3. BFS
4. DFS
5. Merge Sort
-----------------------------
Your Choice:
"""

algorithm = Algorithm()
algorithm_map = {
    "1": algorithm.quick_sort,
    "2": algorithm.bubble_sort,
    "3": algorithm.bfs,
    "4": algorithm.dfs,
    "5": algorithm.merge_sort
}


class Main(Sorting):
    def __init__(self, data_list, algorithm_method):
        super().__init__(data_list, algorithm_method)

    def sort(self):
        return super().sort()


if __name__ == "__main__":
    input_list = [int(i) for i in input("List values(csv) :").split(",")]
    choice = input(algorithm_choices)
    if choice in algorithm_map.keys():
        main = Main(input_list, algorithm_map[choice])
        main.sort()
        print("Sorted List : {}".format(input_list))
    else:
        print("Invalid choice!")
