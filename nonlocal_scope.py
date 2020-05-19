x = "global"


def outer():
    x = "local"

    def inner():
        # to access varialbe in the outer function's scope, neither global nor local.
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

print(" global one : ", x)
