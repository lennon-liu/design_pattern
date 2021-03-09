


class Example():
    def run(self):
        print "i am running"

    def jump(self):
        print "i am jumping"


class Example_Decorator():


    def __init__(self,example):
        self._example = example

    def run(self):
        self._example.run()

    def __getattr__(self, name):
        j =  getattr(self._example,name)
        return j

if __name__ == "__main__":
    example= Example()
    example.name = "aaa"
    ed = Example_Decorator(example)
    ed.run()
    ed.jump()
    print ed.name



