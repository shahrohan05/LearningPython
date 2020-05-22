
def arithmetic_operations():
    try:
        input1 = input("Input 1 :")
        input2 = input("Input 2 :")
        operation = input("Operation :")
        print("%d %s %d :" % (int(input1), operation,
                              int(input2)), eval(input1+operation+input2))
    except Exception as e:
        print(e)
        print("Error processing your request. Please ensure the provided inputs are valid integers and operation is a "
              "valid arithmatic sign character.")
