def foo(arg):
    print("hi")
    return 

x = foo('yellow')
x = foo("blue")
y = foo("red")
print(f"x = {x}")
x = foo('green')
y = foo('orange')
print(f"y = {y}")