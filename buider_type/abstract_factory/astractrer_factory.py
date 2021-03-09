__Auther__ = "lennon"



class AbstractFactory(object):

    def __init__(self):
        pass

    def create_circle(self):
        pass

    def create_rectangle(self):
        pass

class ACreate(AbstractFactory):
    def __init__(self):
        super(ACreate, self).__init__()

    def create_circle(self):
        return CircleA("circlea")

    def create_rectangle(self):
        return RectangleA("RectangleA")

class BCreate(AbstractFactory):
    def __init__(self):
        super(BCreate, self).__init__()

    def create_circle(self):
        return CircleB("CircleB")

    def create_rectangle(self):
        return RectangleB("RectangleB")


class Circle(object):
    def __init__(self):
        pass

class CircleA(Circle):
    def __init__(self ,name):
        super(Circle, self).__init__()
        self.name = name

class CircleB(Circle):
    def __init__(self ,name):
        super(Circle, self).__init__()
        self.name = name

class Rectangle(object):
    def __init__(self):
        pass
class RectangleA(Rectangle):
    def __init__(self ,name):
        super(Rectangle, self).__init__()
        self.name = name

class RectangleB(Rectangle):
    def __init__(self ,name):
        super(Rectangle, self).__init__()
        self.name = name

class Manager(object):
    def __init__(self):
        self.circles = None
        self.rectangles = None

    def circle(self ,shape_obj):
        print shape_obj.create_circle()
        self.circles  = shape_obj.create_circle()

    def rectangle(self ,shape_obj):
        self.rectangles = shape_obj.create_rectangle()

    def echo_msg(self):
        print '''
            this is the msg 

        circle:%s
        rectangle:%s

        over
        ''' %(self.circles.name ,self.rectangles.name)

if __name__ == "__main__":
    m = Manager()
    circle = ACreate()
    rectangele = BCreate()
    m.circle(circle)
    m.rectangle(rectangele)
    m.echo_msg()