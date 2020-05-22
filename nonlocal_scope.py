x = "global"
global_y = "global y"


def outer():
    # global x # This results in an error at line # 10, stating that there is no binding found for nonlocal x,
    # since the x in enclosing/outer function is actually in global namespace and not in nonlocal/enclosing
    # function's namespace.
    x = "local"

    # global name "global_y" can be accessed in inner scopes, being globally accessible, but trying to reassign
    # this without global statement would result in new variable creation in the local or this name space.
    print("global y(outer):"+global_y)

    def inner():
        # to access variable in the outer function's scope, neither global nor local.
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
        print("global y(inner):" + global_y)

    inner()
    print("outer:", x)


outer()

print(" global one : ", x)
print("global y(outside):"+global_y)