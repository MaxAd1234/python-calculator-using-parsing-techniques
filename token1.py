class Token:
    
    def __init__(self, pValue, pType ):
        self.value = pValue #floating point number for number-Tokens
        self.token_type = pType #Token Type e.g. "+"-operator, number.... (String)

    def getType(self):
        return self.token_type
    def getValue(self):
        return self.value
    def __str__(self):
        return f"{self.value} ({self.token_type})"