def quick_sort_partition(data_list, start_index, end_index):
    pivot = data_list[end_index]
    i = start_index - 1
    for j in range(start_index, end_index):
        if data_list[j] <= pivot:
            i += 1
            if i != j:
                data_list[i], data_list[j] = data_list[j], data_list[i]

    data_list[i + 1], data_list[end_index] = data_list[end_index], data_list[i + 1]
    return i + 1


def quick_sort(data_list, start_index, end_index):
    if start_index < end_index:
        partition_index = quick_sort_partition(data_list, start_index, end_index)
        quick_sort(data_list, start_index, partition_index - 1)
        quick_sort(data_list, partition_index + 1, end_index)


class Algorithm:

    def quick_sort(self, data_list):
        end_index = len(data_list) - 1
        quick_sort(data_list, 0, end_index)

    def bubble_sort(self, data_list):
        pass

    def bfs(self, data_list):
        pass

    def dfs(self, data_list):
        pass

    def merge_sort(self, data_list):
        pass
