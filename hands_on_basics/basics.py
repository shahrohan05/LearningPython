# Python script containing hands on sample code for some basic Python concepts
import os
from io_sample import io_example
from comparison_sample import comparision_operator
from comparison_sample import number_swap
from arithmatic_sample import arithmetic_operations
from shipping import shipping_problem

choices = """
============== Python Hands On ==============
1. IO Example
2. Comparison Operators
3. Arithmetic Operations
4. Number Swap
5. Boat Capacity Problem
6. Exit
=============================================
"""

choice_routines = {
    1: io_example,
    2: comparision_operator,
    3: arithmetic_operations,
    4: number_swap,
    5: shipping_problem
}


def pick_routine():
    os.system("cls" if os.name == "nt" else "clear")  # Clear console
    print(choices)
    choice = input("Your Choice :")
    if int(choice) in range(1, 6):
        choice_routines[int(choice)]()
        if input("Continue? (yes/no) :").lower() == "yes":
            pick_routine()

    elif int(choice) == 6:
        pass

    else:
        if input("Invalid Choice! Continue? (yes/no) :").lower() == "yes":
            pick_routine()


print("calling pick routine from basics - ")
pick_routine()
