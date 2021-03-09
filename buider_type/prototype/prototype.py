__Auther__ = "lennon"
class Prototype(object):
    'this a a prototype example'
    def __init__(self):
        self.class_manager={}
        pass

    def regester(self,class_name,class_obj):
        self.class_manager[class_name] = class_obj

    def regester_out(self,class_name):
        del self.class_manager[class_name]

    def clone(self,class_name,**kwargs):
        if class_name in self.class_manager:
            obj = self.class_manager[class_name]
            obj.__dict__.update(kwargs)
            return obj



if __name__ == "__main__":
    prototype = Prototype()

    class Example():
        def __init__(self):
            pass

    e = Example()
    prototype.regester("example",Example())
    e1 = prototype.clone("example",argv1 = 1,argv2 = 2)
    print e1.__dict__