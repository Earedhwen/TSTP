try:
    a = int(input("type a number: "))
    b = int(input("type another: "))
    print(a/b)
except (ZeroDivisionError,ValueError):
    print("invalid input")
