

class Food(object):

    def __init__(self):
        pass

    def eat(self):
        raise NotImplementedError

class Rice(Food):

    def eat(self):
        print "eat rice"


class Dumpling(Food):

    def eat(self):
        print "eat dumpling"


class Tools(object):

    food = None

    def eat(self):
        raise NotImplementedError


class Fox(Tools):

    def eat(self):
        self.food.eat()
        print "use fox"


class Chopstick (Tools):


    def eat(self):
        self.food.eat()
        print "use chopstick"

if __name__== "__main__":
    rice = Rice()
    dumpling = Dumpling()
    fox=Fox()
    chopstick=  Chopstick()
    fox.food = rice
    fox.eat()
    chopstick.food= dumpling
    chopstick.eat()