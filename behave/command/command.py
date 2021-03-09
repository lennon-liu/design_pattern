import os


class Command():

    def __init__(self,src,dest):
        self.src = src

        self.dest = dest

    def execute(self):
        self()

    def __call__(self):
        print "rename {a} ro {b}".format(a=self.src,b = self.dest )
        os.rename(self.src,self.dest)

    def undo(self):
        print "rename back {a} ro {b}".format(a=self.dest, b=self.src)
        os.rename(self.dest, self.src)


if __name__ == "__main__":
    commands=[]

    commands.append(Command("test1.txt","test2.txt"))

    for command in commands:
        command.execute()

    for command in commands:
        command.undo()