


class Observer(object):

    def __init__(self):
        self.observerd = list()

    def attach(self,viewer):
        self.observerd.append(viewer)
        print "add viewer"+viewer.name

    def dispitch(self,viewer):
        self.observerd.remove(viewer)

    def dispitchone(self):
        return self.observerd.pop()


    def notice(self):
        for observer in self.observerd:
            observer.update(self)

class OberverA(Observer):

    def __init__(self):
        super(OberverA,self).__init__()
        self.name = "observerA"
        self.newmsg=None

    @property
    def msg(self):
        return self.newmsg

    @msg.setter
    def msg(self,nmsg):
        self.newmsg = nmsg
        self.notice()

    # def setmsg(self,msg):
    #     self.newmsg = msg
    def display(self):
        return self.newmsg



class Viewer(object):

    def __init__(self,name):
        self.name = name

    def update(self,ob):
        print self.name,"-->",ob.display()



def example():
    ob = OberverA()
    v1 = Viewer("A")
    v2 = Viewer("B")
    ob.attach(v1)
    ob.attach(v2)
    ob.msg = "this is msg a"
    # ob.notice()
    print ob.dispitchone().name
    print ob.dispitchone().name
    ob.msg="this is msg b"
    # ob.notice()

if __name__ == "__main__":
    example()