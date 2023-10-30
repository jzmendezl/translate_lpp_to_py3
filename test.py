import sys

from antlr4 import *

from LPPLexer import LPPLexer
from LPPParser import LPPParser


class Test():
    try:
        lexer = LPPLexer()

        def read_input(arg):
            if len(sys.argv) > 1:
                file_input = open(sys.argv[1], "r", encoding="utf8")
                code = file_input.readlines()
                return InputStream(''.join(code))
            else:
                return InputStream(input(">>> "))

        tokens = CommonTokenStream(lexer)
        parser = LPPParser(tokens)
        tree = parser.programa()

        print(str(tree(parser)))

    except Exception as err:
        print('Error (Test):' + err)
