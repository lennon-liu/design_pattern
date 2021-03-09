__Auther__ = "lennon"
class Shape(object):

    def __init__(self):
        pass

    def draw(self):
        raise NotImplementedError

class Circle(Shape):

    def __init__(self):
        super(Circle, self).__init__()

    def draw(self):
        print "circle"


class Rectangle(Shape):

    def __init__(self):
        super(Rectangle, self).__init__()

    def draw(self):
        print "rectangle"



class ShapeCreate(object):

    def __init__(self):
        pass

    def create(self):
        raise NotImplementedError

class CircleCreate(ShapeCreate):

    def create(self):
        return  Circle()

class RectrangleCreate(ShapeCreate):

    def create(self):
        return  Rectangle()

rectangle = RectrangleCreate().create()
rectangle.draw()