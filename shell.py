
from lexar import Lexar
from parse import Parser
from interpreter import Interpreter
from data import Data

base = Data()

while True:
    text = input("Shitbro: ")
    tokenizer = Lexar(text)
    tokens = tokenizer.tokenize()

    print(tokens)


    parser = Parser(tokens)
    tree = parser.parse()

    print(tree)


    inter = Interpreter(tree, base)
    omg = inter.interpret()

    print(omg)



















































