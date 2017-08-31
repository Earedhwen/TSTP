class Rectangle():
    def __init__(self,w,l):
        self.width = w
        self.length = l

    def area(self):
        return self.width*self.length

class Data():
    def __init__(self):
        self.nums = [1,2,3,4,5]

    def change_data(self,index,n):
        self.nums[index] = n

class Square(Rectangle):
    def __init__(self,w,l):
        if w != l:
            print("This is not a square!")
        else:
            self.length, self.width = l,l

class Dog():
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self,name):
        self.name = name

if __name__ == "__main__":
    data_one = Data()
    data_one.nums[0] = 100
    print(data_one.nums)

    data_two = Data()
    data_two.change_data(0,100)
    print(data_two.nums)

    mysquare = Square(15,15)
    print(mysquare.area())

    mick = Person("Mick Jagger")
    stan = Dog("Stanley","Bulldog",mick)
    print(stan.owner.name)








    
