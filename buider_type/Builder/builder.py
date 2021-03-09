
__Auther__ = "lennon"

class Builder(object):
    def __init__(self):
        pass

    def look(self):
        raise NotImplementedError

    def write(self):
        raise NotImplementedError

    def read(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError


class ManBuild(Builder):
    def look(self):
        return "man look around"

    def write(self):
        return "man write something"

    def read(self):
        return "man read something"

    def run(self):
        return "man i can run"


class WoManBuild(Builder):
    def look(self):
        return "woman look around"

    def write(self):
        return "woman write something"

    def read(self):
        return "woman read something"

    def run(self):
        return "woman i can run"

class Manage(object):
    def __init__(self,Build):
        self.build = Build

    def do(self):
        print self.build().write()
        print self.build().look()
        print self.build().read()
        print self.build().run()


if __name__=="__main__":
    Manage(ManBuild).do()