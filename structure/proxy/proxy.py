__Auther__ = "lennon"




class SendBase(object):

    def __init__(self):
        pass

    def send_msg(self,msg):
        raise NotImplementedError


class Sender(SendBase):
    def __init__(self,receive):
        super(Sender,self).__init__()
        self.receive = receive

    def send_msg(self,msg):
        return "To:"+self.receive.name+"--"+msg


class Proxy(SendBase):
    def __init__(self, name):
        super(Proxy, self).__init__()
        self.Sender = Sender(name)

    def send_msg(self,msg):
        return self.Sender.send_msg(msg)

class Receive(object):

    def __init__(self,name):
        self.name = name


if __name__ == "__main__":
    receive = Receive("receive")
    proxy = Proxy(receive)
    print proxy.send_msg("msg")