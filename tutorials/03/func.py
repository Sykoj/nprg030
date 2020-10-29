b = 19

first(4)
second(4)

def first(x):
    global b
    b = 1   
    print(x)

def second(x):
    print(b)
    print(x ** 2)
