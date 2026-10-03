class Transition:
    def __init__(self, start, pinput, end):
        self.start = start#state
        self.tinput = pinput#char
        self.end = end#state
    def getStart(self):
        return self.start
    def getEnd(self):
        return self.end
    def getInput(self):
        return self.tinput