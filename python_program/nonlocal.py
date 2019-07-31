#use of nonlocal variable
def outer():
    x= "local"

    def inner():
        nonlocal x
        x= "nonlocal"
        print("inner function : ",x)

    inner()
    print("outer function :",x)
outer()
