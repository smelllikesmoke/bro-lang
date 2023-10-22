from tokens import *

class Lexar:
    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    operations = "+-/*{}="
    declarations = ["bro"]
    stopwords = [" "]
    boolean = ["and", "or", "not"]
    
    
    def __init__(self, text):    
        self.text = text
        self.idx = 0
        self.tokens = []
        self.char = self.text[self.idx]
        self.token = None

    def tokenize(self):
        while self.idx < len(self.text):
            if self.char in Lexar.digits:
                self.token = self.extract_number()

            elif self.char in Lexar.operations:
                self.token = Operation(self.char)   
                self.move()

            elif self.char in Lexar.stopwords:
                self.move()
                continue

            elif self.char in Lexar.letters:
                word = self.extract_word()
                if word in Lexar.declarations:
                    self.token = Declaration(word)

                elif word in Lexar.boolean:
                    self.token = Boolean(word)
                else:
                    self.token = Variable(word)

            self.tokens.append(self.token)    


        return self.tokens


    def extract_number(self):
        number = ""
        isFloat = False
        while ((self.char in Lexar.digits or self.char == ".") and (self.idx < len(self.text))):
            if self.char == ".":
                isFloat = True
            number += self.char
            self.move()

        return Integer(number) if not isFloat else Float(number)

    def extract_word(self):
        word = ""
        while self.char in Lexar.letters and self.idx < len(self.text):
            word += self.char
            self.move()

        return word
    
    def move(self):
        self.idx += 1
        if self.idx < len(self.text):
            self.char = self.text[self.idx]
                






















































