from lexer import Lexer
from _parser import Parser
from evaluator import Evaluator


def main():
    filename = 'wowo.wo'
    file = open(filename, 'r')
    lexer = Lexer(file)
    _parser = Parser(lexer.tokens)

    lexer.tokenizer()
    print "TOKENS:"
    print lexer.tokens, "\n"

    _parser.build_AST()
    print "AST:"
    print _parser.AST, "\n"

    evaluator = Evaluator(_parser.AST)
    print "OUTPUT:"
    evaluator.run(_parser.AST)


if __name__ == "__main__":
    main()
