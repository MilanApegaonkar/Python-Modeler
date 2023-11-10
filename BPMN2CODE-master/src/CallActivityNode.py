from Node import Node


class CallActivityNode(Node):

    def __init__(self, node_id):
        super().__init__(node_id, 'task', False)
        self.__name = ''
        self.script=''

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
    def getScript(self):
        return self.script
    def setScript(self,script):
        self.script=script
