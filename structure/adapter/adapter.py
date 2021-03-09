
__Auther__ = "lennon"
class Kid(object):
    def __init__(self,name):
        self.name = name

    def cry(self):
        print self.name+":","I am crying"

class KidWang(Kid):
    def __init__(self,name):
        super(Kid,self).__init__()
        self.name = name

    def cry(self):
        print self.name + ":", "I am not crying anylonger"


class Manager(object):
    def __init__(self,name):
        self.kid = KidWang(name)

    def cry(self):
        self.kid.cry()



if __name__ == "__main__":
    Manager("lilisi").cry()