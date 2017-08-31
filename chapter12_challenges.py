import math

#Challege 1

class Apple():
    def __init__(self,colour,weight,diameter,variety):
        self.colour = colour
        self.weight = weight
        self.diameter = diameter
        self.variety = variety
        print("Created!")

#Challenge 2

class Circle():
    def __init__(self,radius):
        self.radius = radius
        print("Created!")

    def area(self):
        return math.pi*self.radius**2

#Challenge 3

class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        t = True
        if (a+b < c or a+c < b or b+c < a):
            t = False
            print("This is not a valid triangle. " +\
                  "Please change the side lengths.")
        else:
            print("Created!")

    def change_a(self,a):
        self.a = a

    def change_b(self,b):
        self.b = b

    def change_c(self,c):
        self.c = c

    def check_triangle(self):
        if (a+b < c or a+c < b or b+c < a):
            t = False
            print("This is not a valid triangle. " +\
                  "Please change the side lengths.")
        else:
            t = True
            print("This is a valid triangle.")

    def area(self):
        A = math.acos((self.b**2+self.c**2-self.a**2)/(2*self.b*self.c))
        area = 0.5*self.b*self.c*math.sin(A)
        return area

#Challenge 4

class Hexagon():
    def __init__(self,a,b,c,d,e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        print("Created!")

    def calculate_perimeter(self):
        return self.a + self.b + self.c + self.d + self.e + self.f













