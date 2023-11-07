import sys

from antlr4 import *

from gen.LPPLexer import LPPLexer
from gen.LPPParser import LPPParser
from Translate import Translate


def read_input(arg):
    if len(sys.argv) > 1:
        file_input = open(sys.argv[1], "r", encoding="utf8")
        code = file_input.readlines()
        return InputStream(''.join(code))
    else:
        code = sys.stdin.readlines()
        return InputStream(''.join(code))

def main():
    data = read_input(sys.argv)
    lexer = LPPLexer(data)
    tokens = CommonTokenStream(lexer)
    parser = LPPParser(tokens)
    tree = parser.programa()
    lis = Translate()

    walker = ParseTreeWalker()
    walker.walk(lis, tree)

if __name__ == '__main__':
    main()