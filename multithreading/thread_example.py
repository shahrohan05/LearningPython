# _thread module, which was deprecated and renamed to _thread from thead in python 3 onwards, this module provides a
# way to spawn threads using function
import _thread
import time


# Recursive factorial function
def factorial(n):
    rc = 0
    if n < 1:
        print("Factorials :")
        rc = 1
    else:
        rc = n * factorial(n-1)  # Recursive call
        print('{}: {}'.format(str(n),str(rc)))

    return rc


if __name__ == "__main__":
    _thread.start_new_thread(factorial, (5,))
    _thread.start_new_thread(factorial, (4,))

    # These threads do not run in parallel to each other, only one thread can execute on
    # the python interpreter due to GIL(Global Interpreter Lock)
    
    time.sleep(2)  # Waiting for a while for above two threads to finish
