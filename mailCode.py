import sys
from lark import Lark

def eval_tree(t, env):
    if t.data == 'codeblock':
        for child in t.children:
            eval_tree(child, env)

    elif t.data == 'print':
        if t.children[0].data == 'string':
            for words in t.children[0].children:
                print(words, end = "")
            print()
        elif t.children[0].data == 'var':
            print(env[t.children[0].children[0]])

    elif t.data == 'forloop':
        for x in range(int(t.children[0])):
            for child in t.children[1:]:
                eval_tree(child, env)

    elif t.data == 'assignment':
        env[t.children[0].children[0]] = int(t.children[1])

    elif t.data == 'add':
        env[t.children[0].children[0]] += int(t.children[1])

    elif t.data == 'sub':
        env[t.children[0].children[0]] -= int(t.children[1])

    elif t.data == 'div':
        env[t.children[0].children[0]] /= int(t.children[1])
        env[t.children[0].children[0]] = int(env[t.children[0].children[0]])

    elif t.data == 'mul':
        env[t.children[0].children[0]] *= int(t.children[1])

    else:
        raise SyntaxError('unrecongnized tree')

def getProgram(file):
    with open(file) as f:
        program = f.read()
        f.close()
    return program

if __name__ == '__main__':
    my_grammar = """
    ?start: _greeting codeblock _closing
    _greeting: "Dear " _WORD ","
            | "Hello " _WORD ","
            | "Greetings " _WORD ","

    codeblock: statement+
    _bulletcodeblock: ("~" statement)+
    ?statement: print
            | forloop
            | assignment
            | math
    print: "Tell me '" expression+ "'."
            | "Tell me" var "."
    forloop: "Do this" INT "times:" _bulletcodeblock
    assignment: var "is" expression "."
    ?expression: CNAME
            | string
            | literal
    math: "Increase" var "by" expression "." -> add
            | "Decrease" var "by" expression "." -> sub
            | "Divide" var "by" expression "." -> div
            | "Multiply" var "by" expression "." -> mul
    ?literal: INT
    var: CNAME
    _WORD: WORD
    string: WORD [WS WORD]+
    _closing: "Sincerely," _WORD
            | "Thanks," _WORD
    %import common.CNAME
    %import common.NEWLINE
    %import common.INT
    %import common.WORD
    %import common.WS
    %ignore WS
    """
    parser = Lark(my_grammar)
    program = getProgram(sys.argv[1])
    parse_tree = parser.parse(program)
    env = {
    }
    eval_tree(parse_tree, env)
