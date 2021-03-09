

class Responsibility(object):

    def chain(self,handler):
        self._next_handler = handler


class Responsibility1(Responsibility):

    def __init__(self):
        super(Responsibility,self).__init__()
        self.name = "Responsibility1"

    def process(self,level,envent):
        if level<1:
            print self.name,":","is processing this envent:",envent()
        else:
            print self.name, ":", "have no qualification processing this envent"
            self._next_handler.process(level,envent)

class Responsibility2(Responsibility):

    def __init__(self):
        super(Responsibility,self).__init__()
        self.name = "Responsibility2"

    def process(self,level,envent):
        if level<2:
            print self.name,":","is processing this envent:",envent()
        else:
            print self.name, ":", "have no qualification processing this envent"
            self._next_handler.process(level,envent)


class Responsibility3(Responsibility):

    def __init__(self):
        super(Responsibility,self).__init__()
        self.name = "Responsibility3"

    def process(self,level,envent):
        if level<3:
            print self.name,":","is processing this envent:",envent()
        else:
            print self.name, ":", "have no qualification processing this envent"
            self._next_handler.process(level,envent)

class Responsibility4(Responsibility):

    def __init__(self):
        super(Responsibility,self).__init__()
        self.name = "Responsibility4"

    def process(self,level,envent):
        if level<4:
            print self.name,":","is processing this envent:",envent()
        else:
            print self.name, ":", "have no qualification processing this envent"
            # self._next_handler.process(self,level,envent)

def envent():
    return "use 5 dollar"


if __name__ == "__main__":
    r1 = Responsibility1()
    r2 = Responsibility2()
    r3 = Responsibility3()
    r4 = Responsibility4()
    r1.chain(r2)
    r2.chain(r3)
    r3.chain(r4)

    r1.process(3,envent)