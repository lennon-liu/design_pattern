

class Behave(object):

    def whatto(self):
        raise NotImplementedError


class Run(Behave):

    def whatto(self):
        print "running"

class Walk(Behave):

    def whatto(self):
        print "walking"

class Swam(Behave):

    def whatto(self):
        print "swamming"


class Work(Behave):

    def whatto(self):
        print "working"


class Strategy():
    def __init__(self,behave):
        self.behave = behave

    def set_behave(self,behave):
        self.behave= behave

    def whatdo(self):
        self.behave.whatto()

if __name__ == "__main__":
    w = Work()
    sw = Swam()
    r = Run()
    wk = Walk()
    s = Strategy(w)
    s.whatdo()
    s.set_behave(sw)
    s.whatdo()
    s.set_behave(wk)
    s.whatdo()