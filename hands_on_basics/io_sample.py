def io_example():
    try:
        param_count = input("Number of parameters :")
        if(int(param_count) < 1):
            if(input("Invalid Input! Try again? (yes/no) :").lower() == "yes"):
                io_example()
        for i in range(1, int(param_count)+1):
            input_str = input("Input %d :" % i)
            print(input_str)
        print("IO Example over----------")
    except Exception as e:
        print(e)
        if(input("Try again? (yes/no) :").lower() == "yes"):
            io_example()
