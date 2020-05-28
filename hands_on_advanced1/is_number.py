import re


def is_non_negative_int(num_str):
    try:
        int_num = int(num_str)
        return int_num > 0
    except ValueError as e:
        return False


def is_negative_int(num_str):
    try:
        int_num = int(num_str)
        return int_num < 0
    except ValueError as e:
        return False


def is_real_number(num_str):
    try:
        float_num = float(num_str)
        return True
    except ValueError as e:
        return False


def is_scientific_number(num_str):
    try:
        float_num = float(num_str)  # Numbers in scientific notations can be parsed to a floating point number.
        if re.search("[e|E]", num_str):  # Check if the exponent sign was present in the input string
            return True
        else:
            return False
    except ValueError as e:
        return False


def is_number(num_str):
    if not is_non_negative_int(num_str):
        if not is_negative_int(num_str):
            if not is_scientific_number(num_str):
                if not is_real_number(num_str):
                    print("{} is not a number!".format(num_str))
                else:
                    print("{} is a real number".format(num_str))
            else:
                print("{} is a scientific number".format(num_str))
        else:
            print("{} is a negative integer".format(num_str))
    else:
        print("{} is a positive integer".format(num_str))


if __name__ == "__main__":
    is_number(input("Input String : "))
