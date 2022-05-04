from lark import Lark

my_grammar = """
?start: _greeting codeblock _closing
_greeting: "Dear " _WORD ","
        | "Hello " _WORD ","
        | "Greetings " _WORD ","

codeblock: statement+
_bulletcodeblock: ("~" statement)+
?statement: print
        | forloop
        //| whileloop
        //| if
        | assignment
        | math
print: "Tell me '" expression+ "'."
        | "Tell me" var "."
forloop: "Do this" INT "times:" _bulletcodeblock
//whileloop: "As long as" expression ":"  _bulletcodeblock
//if: "If" expression ":" _bulletcodeblock "If not:" _bulletcodeblock
assignment: var "is" expression "."
?expression: CNAME
        | string
        | literal
        //| expression "is greater than" expression -> gt
        //| expression "is less than" expression -> lt
        //| expression "is less than or equal to" expression -> le
        //| expression "is greater than or equal to" expression -> ge
        //| expression "is equal to" expression -> eq
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

parser = Lark(my_grammar)
program= """
Dear MailCode,
Tell me 'Hello World'.
x is 0.
Do this 5 times:
~Tell me 'Increasing x by one'.
~Increase x by 1.
Tell me x.
Thanks,
Drew
"""

parse_tree = parser.parse(program)

env = {
}

#print(parse_tree.pretty())
eval_tree(parse_tree, env)

