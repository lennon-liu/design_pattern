

def wrappers(cls):
    _singleton = dict()

    def inner(*args,**kwargs):
        if cls not in _singleton:
            _singleton.setdefault((cls,args,tuple(kwargs.items())),cls(*args,**kwargs))
        return _singleton[(cls,args,tuple(kwargs.items()))]
    return inner


def flyweight(cls):
    instances = dict()
    return lambda *args, **kargs: instances.setdefault(
                                            (cls,args, tuple(kargs.items())),
                                            cls(*args, **kargs))


@wrappers
class A():

    def __init__(self,a,b):
        self.a = a
        self.b = b


@wrappers
class B():

    def __init__(self, a, b):
        self.a = a
        self.b = b


print (A(1,2) is A(1,2))
print (A(1,2) is B(1,3))