

class Composite(object):

    def __init__(self,composite_name):
        self.composite_name =composite_name

    def Add(self,node):
        raise NotImplementedError

    def display(self):
        raise NotImplementedError

class Leaf(Composite):

    def __init__(self,composite_name):
        super(Leaf, self).__init__(composite_name)


    def Add(self,node):
        print "could not add in leaf"


    def display(self):
        print "leaf:"+self.composite_name


class Node(Composite):

    def __init__(self,composite_name):
        super(Node, self).__init__(composite_name)
        self.nodelist = []


    def Add(self,node):
        self.nodelist.append(node)


    def display(self):
        print "node:" + self.composite_name
        for data in self.nodelist:
            data.display()


if __name__ == "__main__":
    node0 = Node("Zhang")
    node1 = Node("Li")
    node2 = Node("Zhao")
    node3 = Node("hu")


    leaf0 = Leaf("jiaxiao")
    leaf1 = Leaf("feiji")
    leaf2 = Leaf("huifei")
    leaf3 = Leaf("liedong")
    node0.Add(leaf0)
    node1.Add(leaf1)
    node1.Add(leaf2)
    node2.Add(leaf3)

    node0.Add(node1)
    node0.Add(node2)
    node1.Add(node3)

    node0.display()