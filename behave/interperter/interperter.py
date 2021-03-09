

class ExceptionBase(object):

    def interpret(self, content):
        raise NotImplementedError

class VulueException(ExceptionBase):

    def interpret(self,context):
        print "this is a vulue exception"

class NonterminalExpression(ExceptionBase):

    def interpret(self,context):
        print "this is a nonterminal exception"


class SoException(ExceptionBase):

    def interpret(self,context):
        print "this is a so exception"

class Context(object):
    def __init__(self):
        self.msg=""
        self.err= ""



if __name__ == "__main__":

    context = Context()
    exception_list = list()
    exception_list.append(VulueException())
    exception_list.append(NonterminalExpression())
    exception_list.append(SoException())

    for exception in exception_list:
        exception.interpret(context)