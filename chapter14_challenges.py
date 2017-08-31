#Challenge 1,2

class Square():
    square_list = []

    def __init__(self,l):
        self.length = l
        self.square_list.append(self.length)
        print("{} by {} by {} by {}".format(self.length,self.length,\
                                            self.length,self.length))

#Challenge 3

def is_same(x,y):
    if type(x) is type(y):
        return True
    else:
        return False
