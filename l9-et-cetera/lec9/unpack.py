def f(*args, **kwargs):
    print("Positional:", args)


f(100, 50, 25)
f(100, 50, 25, 5)
f(100)