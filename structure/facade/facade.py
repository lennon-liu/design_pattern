


class Apple():
    name = "apple"
    def buy(self):
        print "buy:"+self.name

    def sell(self):
        print "sell"+self.name


class Orange():
    name = "orange"

    def buy(self):
        print "buy:"+self.name

    def sell(self):
        print "sell"+self.name


class Fruit():
    name = "fruit"

    def buy(self):
        print "buy:"+self.name

    def sell(self):
        print "sell"+self.name


class Manage():
    def __init__(self,appele,orange,frite):
        self.apple = appele
        self.orange = orange
        self.frite = frite

    def buy(self):
        self.apple.buy()
        self.orange.buy()
        self.frite.buy()

    def sell(self):
        self.apple.sell()
        self.orange.sell()
        self.frite.sell()


if __name__=="__main__":
    apple = Apple()
    orange = Orange()
    frite =Fruit()
    m = Manage(apple,orange,frite)
    m.buy()
    m.sell()
