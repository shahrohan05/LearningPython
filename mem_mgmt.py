# Memory Mgmt in Python
import sys


def mem_test():
    x = 500
    y = 500
    print(id(x))
    print(id(y))
    print(x == y)
    print(x is y)

    print(sys.getsizeof(float))
    print(sys.getsizeof(int))
    print(sys.getsizeof(dict))
    print(sys.getsizeof(set))
    print(sys.getsizeof(tuple))
    # The above code prints 416, for all types.
    # Does all object take up the same amount of size in Python?

    # It seems sizes are allocated for objects based on the content they hold. Will look at it later.
    print("Float size - ", sys.getsizeof(4000.50))
    print("Int size - ", sys.getsizeof(6000000))
    print("dict size - ", sys.getsizeof({15: "sam", 16: "jack"}))
    print("set size - ", sys.getsizeof({"one", "two"}))
    print("tuple size - ", sys.getsizeof((1, "sam", 2, "jack")))


mem_test()
