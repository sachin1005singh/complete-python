def f():
    global s
    print(s)
    s = "inside the function"

    print(s)

s = "it is global declared"
f()
print(s)
