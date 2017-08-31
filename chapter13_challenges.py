class Shape():
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return 2*(self.length+self.width)

class Square(Rectangle):
    def __init__(self,l):
        self.length = l
        self.width = l

    def change_size(self,n):
        self.length += n
        self.width = self.length

class Horse():
    def __init__(self,name,rider):
        self.name = name
        self.rider = rider

class Person():
    def __init__(self,name):
        self.name = name

if __name__ == "__main__":
    my_rect = Rectangle(5,10)
    print(my_rect.calculate_perimeter())
    my_rect.what_am_i()

    my_square = Square(4)
    print(my_square.calculate_perimeter())
    my_square.change_size(5)
    print(my_square.calculate_perimeter())
    my_square.what_am_i()

    amy = Person("Amy")
    bella = Horse("Bella",amy)
    print(bella.rider.name)









