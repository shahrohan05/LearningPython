'''
"Create a python class named Algorithms. It should have following sorting algorithms:
        Quick sort
        Bubble sort
        BFS (I/P Graph)
        DFS (I/P Graph)
        Merge Sort
Create a class Sorting which should sort the list provided as input parameter using the algorithm which is also provided as input 
parameter. 
Create a main class which inherits the Sorting class and calls sort method with list and algorithm to use."

'''
from collections import deque
class Algorithm:
    def __init__(self):
        pass

    def quick_sort(self, Elements):
        self.quicksort(Elements, 0, len(Elements) - 1)
        return Elements

    def quicksort(self, data, left, right):      
        if left >= right:
            return
        pivot = left
        low, high = left + 1, right
        while True:
            while low <= high and data[low] <= data[pivot]:
                low += 1
            while low <= high and data[high] >= data[pivot]:
                high -= 1
            if low <= high:
                data[low], data[high] = data[high], data[low]
            else:
                break
        data[pivot], data[high] = data[high], data[pivot]
        self.quicksort(data, left, high - 1)
        self.quicksort(data, high + 1, right)

    def bubble_sort(self, Elements):
        flag = True
        for i in range(len(Elements)):
            flag = True
            for j in range(len(Elements) - i - 1):
                if Elements[j] > Elements[j + 1]:
                    flag = False
                    Elements[j], Elements[j + 1] = Elements[j + 1], Elements[j]
            if flag:
                break
        return Elements
    def bfs(self,graph, start):
        explored = []
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in explored:
                explored.append(node)
                neighbours = graph[node]    
                for neighbour in neighbours:
                    queue.append(neighbour)
        return explored
    
    def dfs(self, graph, source):
        visited = [] 
        print("The order of DFS traversal:")
        def Dfs(visited, graph, node):
            if node not in visited:
                print(node)
                visited.append(node)
                for neighbour in graph[node]:
                    Dfs(visited, graph, neighbour)
        Dfs(visited,graph,source)
            

    def merge_sort(self,Elements):
        self.mergesort(Elements, 0, len(Elements) - 1)
        return Elements

    def merge(self, data, left, middle, right):
        left_elements = [data[l] for l in range(left, middle + 1)]
        right_elements= [data[r] for r in range(middle + 1, right + 1)]
        i = 0
        j = 0
        k = left
        while i < (middle - left + 1) and j < (right - middle):
            if left_elements[i] <= right_elements[j]:
                data[k] = left_elements[i]
                i += 1
            else:
                data[k] = right_elements[j]
                j += 1
            k += 1

        while i < (middle - left + 1):
            data[k] = left_elements[i]
            k += 1
            i += 1

        while j < (right - middle):
            data[k] = right_elements[j]
            k += 1
            j += 1
    
    def mergesort(self, data, left, right):
        if left < right:
            middle = (left + right) // 2
            self.mergesort(data, left, middle)
            self.mergesort(data, middle + 1, right)
            self.merge(data, left, middle, right)

class Sorting:
    def __init__(self):
        self.algorithm = Algorithm()

    def sort(self,Elements, algo, source):
        if algo == 1:
            print('Sorted elements are : ' + str(self.algorithm.quick_sort(Elements)))
        elif algo == 2:
            print('Sorted elements are: ' + str(self.algorithm.bubble_sort(Elements)))
        elif algo == 3:
           print(self.algorithm.bfs(Elements,source))
        elif algo == 4:
            self.algorithm.dfs(Elements,source)
        elif algo == 5:
            print('Sorted elements are : ' + str(self.algorithm.merge_sort(Elements)))

class Main(Sorting):
    def __init__(self):
        super().__init__()

    def main(self):
        try:
            algo= int(input('Chosoe the algorithm you want to use for sorting :\nEnter 1 for Quick Sort\n2 for Bubble Sort\n3 for BFS\n4 for DFS\n5 for Merge Sort\n: '))
            if algo in [3, 4]:
                graph = {}
                graph_string = input('Enter the graph in form of\nparent:child_space_separated\n: ')
                source = int(input('Choose the source vertex: '))
                for i in graph_string.split(','):
                    parent, child = i.split(':')
                    graph[parent] = child.split()
                self.sort(graph, algo, source)
            else:
                Elements=list(map(int, input("Enter the elements : ").split()))
                self.sort(Elements,algo, '')
        except ValueError:
            print('enter the int only...')
        except Exception as e:
           print("Error: ",e)
       
if __name__ == "__main__":
    Main().main()
