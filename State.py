class State:
    def __init__(self, pName, pIsaccepting):
        self.name = pName#string
        self.isaccepting = pIsaccepting#bool
    def getName(self):
        return self.name
    def getIsAccepting(self):
        return self.isaccepting