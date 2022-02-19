

class StringReader:
    def __init__(self, string):
        self.string = string
        self.i = 0
    
    def readChar(self):
        if self.i >= len(self.string):
            return None
        else:
            c = self.string[self.i]
            self.i += 1
            return c

    def readChars(self, charcount):
        return [self.readChar() for i in range(charcount)]
    
    def readTo(self, char):
        result = ""

        ch = self.readChar()
        while ch != None and ch != char:
            result += ch
            ch = self.readChar()
        
        return result