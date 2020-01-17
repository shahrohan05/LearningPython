"""Create a python class named Algorithms. It should have following sorting algorithms:
        Quick sort
        Bubble sort
        BFS (I/P Graph)
        DFS (I/P Graph)
        Merge Sort
Create a class Sorting which should sort the list provided as input parameter using the algorithm which is also provided as input parameter. Create a main class which inherits the Sorting class and calls sort method with list and algorithm to use."""
import sys
# This is main class which contains all sorting algorithms


class Algorithms:
    def __init__(self):
        pass

    # this function uses bubble sort algorithm.
    def bubble_sort(self, list):
        n = len(list)
        for i in range(n):
            flag = 0
            for j in range(0, n-i-1):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]
                    flag = 1
            if flag == 0:
                break
        return list

    # this function will partition the list.
    def partition(self, list, left, right):
        pivot = list[right]
        i = left - 1
        for j in range(left, right):
            if list[j] < pivot:
                i += 1
                list[i], list[j] = list[j], list[i]
        list[i+1], list[right] = list[right], list[i+1]
        return (i+1)

    # This function uses quick_sort
    def quick_sort(self, list, left, right):
        left, right = int(left), int(right)
        if left < right:
            q = self.partition(list, left, right)
            self.quick_sort(list, left, q-1)
            self.quick_sort(list, q+1, right)
        return list

    # This function merges parts
    def merge(self, list, left, middle, right):
        # First subarray is arr[left..middle]
        # Second subarray is arr[middle+1..right]
        size_of_first_list = middle - left + 1
        size_of_second_list = right - middle

        # create temp arrays
        L = [0] * size_of_first_list
        R = [0] * size_of_second_list

        # Copy data to temp arrays L[] and R[]
        for i in range(0, size_of_first_list):
            L[i] = list[left + i]

        for j in range(0, size_of_second_list):
            R[j] = list[middle + 1 + j]

        # Merge the temp arrays back into arr[left..right]
        i = 0	 # Initial index of first list
        j = 0	 # Initial index of second list
        k = left	 # Initial index of merged list

        while i < size_of_first_list and j < size_of_second_list:
            if L[i] <= R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there are any
        while i < size_of_first_list:
            list[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there are any
        while j < size_of_second_list:
            list[k] = R[j]
            j += 1
            k += 1

    # This function uses merge sort
    def mergeSort(self, list, left, right):
        if left < right:

            # Same as (left + right )/2, but avoids overflow for   large left and right
            middle = (left + (right - 1)) // 2
            self.mergeSort(list, left, middle)
            self.mergeSort(list, middle+1, right)
            self.merge(list, left, middle, right)
        return list

    # This function uses breadth first search for graph traversal
    def bfs(self, graph, initial):
        visited = []
        queue = [initial]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                neighbours = graph[node]

                for neighbour in neighbours:
                    queue.append(neighbour)
        return visited
    # This function uses depth first search for graph traversal

    def dfs(self, graph, initial):
        visited = []
        print("Order:")

        def dfs_new(visited, graph, node):
            if node not in visited:
                print(node)
                visited.append(node)
                for neighbour in graph[node]:
                    dfs_new(visited, graph, neighbour)
        dfs_new(visited, graph, initial)
        return "DFS Travarsal is Done"


class Sorting:
    def __init__(self):
        self.algorithm = Algorithms()

    def sort(self, list, algorithm, initial):
        if algorithm == 1:
            print("After Sorting using quick-sort :" +
                  str(self.algorithm.quick_sort(list, 0, len(list)-1)))
        elif algorithm == 2:
            print("After Sorting using bubble-sort:" +
                  str(self.algorithm.bubble_sort(list)))
        elif algorithm == 3:
            print(self.algorithm.bfs(list, initial))
        elif algorithm == 4:
            print(self.algorithm.dfs(list, initial))
        elif algorithm == 5:
            print("After Sorting using merge-sort:" +
                  str(self.algorithm.mergeSort(list, 0, len(list) - 1)))


class Main(Sorting):
    def __init__(self):
        super().__init__()

    def main(self):
        try:
            choice = int(input(
                "Choose algorithm :\n1.Quick Sort\n2.Bubble Sort\n3.BFS\n4.DFS\n5.Merge Sort\n"))
            if choice == 3 or choice == 4:
                graph = {}
                enter_input = input(
                    "Enter dictionary input (i.e. Parent_node : Child_nodes(space seperated))")
                initial = input("Choose initial vertex:")
                for i in enter_input.split(','):
                    parent, child = i.split(':')
                    graph[parent] = child.split()
                self.sort(graph, choice, initial)
            else:
                ip = int(input("Enter size of list : "))
                list1 = []
                for i in range(ip):
                    given_input = int(input("Enter element ({})".format(i+1)))
                    list1.append(given_input)
                print("Your list is : {}".format(list1))
                self.sort(list1, choice, '')
            print("Do you want to continue? (Y/N)")
            answer = input().upper()
            if answer == 'Y':
                self.main()
            else:
                sys.exit()
        except ValueError:
            print("Enter Valid Input.")
        except Exception as e:
            print("Error ocuured is: " + e)


if __name__ == "__main__":
    Main().main()

