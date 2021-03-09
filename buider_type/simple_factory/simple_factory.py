
__Auther__ = "lennon"

class Shape(object):

    def __init__(self):
        pass

    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    'this is a Circle class'
    def __init__(self):
        super(Circle, self).__init__()
        self.a =1

    def draw(self):
        print "circle"


class Rectangle(Shape):

    def __init__(self):
        super(Rectangle, self).__init__()

    def draw(self):
        print "rectangle"



class factory(object):

    def __init__(self):
        pass

    def get_shape(self,name):
        if name ==None:
            raise ValueError
        if name == "circle":
            return Circle()
        elif name == "rectangle":
            return Rectangle()



f = factory()
s = f.get_shape("circle")
s.draw()
print dir(s)
print "rfewafawe"