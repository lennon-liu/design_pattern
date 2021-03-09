


class State(object):

    def __init__(self):
        self.pos = 0

    def scan(self):

        if self.pos == len(self.stations):
            self.pos = 0
        print "Scanning... Station is", self.name,self.stations[self.pos]
        self.pos+=1

    def change(self):
        pass


class StateAM(State):
    def __init__(self,state):
        super(StateAM, self).__init__()
        self.stations = [1,2,3,4,5,6]
        self.name= "am"
        self.state = state
        self.pos=0

    def change(self):
        self.state.state = self.state.redio_fm
        print "change to fm"


class StateFM(State):
    def __init__(self, state):
        super(StateFM, self).__init__()
        self.stations = [7,8,9,10]
        self.name = "fm"
        self.state = state
        self.pos=0

    def change(self):
        self.state.state = self.state.redio_am
        print "change to am"

class Redio():
    def __init__(self):
        self.redio_am = StateAM(self)
        self.redio_fm = StateFM(self)
        self.state = self.redio_am

    def change(self):
        self.state.pos = 0
        self.state.change()

    def scan(self):
        self.state.scan()


if __name__ == "__main__":
    redio = Redio()
    cmds = [redio.scan]*10 + [redio.change]+[redio.scan]*5
    cmds = cmds+cmds

    for func in cmds:
        func()

