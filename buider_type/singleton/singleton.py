__Auther__ = "lennon"

def wrappers(cls):
    _singleton ={}
    def inner(*args,**kwargs):
        if cls not in _singleton:
            _singleton[cls]  = cls(*args,**kwargs)
        return _singleton[cls]
    return inner

@wrappers
class ClassA():
    def __init__(self):
        print "init"



class Singleton(object):
    __singleton = None
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if cls.__singleton == None:
            cls.__singleton = object.__new__( cls)
        return cls.__singleton

class SingleA(Singleton):
    def __init__(self,a):
        super(SingleA, self).__init__()
        self.name = a

class SingleB(Singleton):
    def __init__(self,b):
        super(SingleB, self).__init__()
        self.name = a

if __name__ == "__main__":
    print ClassA() is ClassA()


    a=SingleA("a")
    b=SingleA("b")

    print a
    print b
    print a is b
