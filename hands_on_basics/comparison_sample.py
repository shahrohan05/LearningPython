

def custom_compare(input1):
    try:
        input1 = int(input1)
        output = "Input 1 is "
        if input1 < 0 or input1 > 1000:
            output += "INVALID"
        elif input1 < 10:
            output += "SMALL"
        elif input1 < 100:
            output += "MEDIUM"
        else:
            output += "LARGE"
        print(output)
    except Exception as e:
        print(e)


def print_larger(input1, input2):
    try:
        input1 = int(input1)
        input2 = int(input2)
        print("Input 1 is larger" if input1 > input2 else "Input 2 is larger" if input1 <
                                                                                 input2 else "Both inputs are same.")
    except Exception as e:
        print(e)


def comparision_operator():
    input1 = input("Input 1:")
    input2 = input("Input 2:")
    custom_compare(input1)
    print_larger(input1, input2)


def swap_integers(input1, input2):
    # This approach should have the same performance as in the case of temp variable, considering the fact that
    # number types are immutable in Python and each assignment creates a new integer in object space.

    try:
        input1 = int(input1)
        input2 = int(input2)
        input1 = input1 + input2
        input2 = input1 - input2
        input1 = input1 - input2
        print("[SWAPPED] Input 1 : %d, Input 2: %d" % (input1, input2))
    except Exception as e:
        print(e)


def number_swap():
    input1 = input("Input 1:")
    input2 = input("Input 2:")
    print("Input 1 : %s, Input 2: %s" % (input1, input2))
    swap_integers(input1, input2)

