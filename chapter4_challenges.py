def squarex(x):
    """
    Returns x squared.
    :param x: int.
    :return: int x*x.
    """
    return x**2

def string(x):
    """
    Print the variable.
    """
    print(x)

def f(x,y,z,a=1,b=1):
    """
    Find the sum of x,y,z; multiply by a; divide by b.
    """
    return a*(x+y+z)/b

#print(f(2,3,4,a=6,b=2))

def half(x):
    """
    Returns x/2.
    """
    return x/2

def quadruple(x):
    """
    Returns 4*x.
    """
    return 4*x

#var = half(8)
#print(quadruple(var))

def myfloat():
    """
    Converts a string to a float.
    """
    try:
        var = input("enter a number:")
        print(float(var))
    except ValueError:
        print("invalid input")

#myfloat()
        
