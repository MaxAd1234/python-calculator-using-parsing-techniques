
from State import *
import token1 as tkn
from Transition import *
from dfa import *
def scanning_alg(input):
    token_list = []
    dfas = generate_DFAs()
    while len(input) > 0:
        ith_lon_pre = []
        for i in range(len(dfas)):
            ith_lon_pre.append(dfas[i].longest_prefix(input))
        longest = ith_lon_pre[0]
        index = 0
        for i in range(len(ith_lon_pre)):
            if len(ith_lon_pre[i]) > len(longest):
                longest = ith_lon_pre[i]
                index = i
        if len(longest) > 0:
            input = input[len(longest):]
            if index == 0:
                token_list.append(tkn.Token("", "-"))
            elif index == 1:
                token_list.append(tkn.Token("","+"))
            elif index == 2:
                token_list.append(tkn.Token("","*"))
            elif index == 3:
                token_list.append(tkn.Token("","/"))
            elif index == 4:
                token_list.append(tkn.Token("","("))
            elif index == 5:
                token_list.append(tkn.Token("",")"))
            elif index == 6:
                token_list.append(tkn.Token(float(longest[1:])*-1,"number"))
            elif index == 7:
                token_list.append(tkn.Token(float(longest),"number"))
            else: 
                print("Tokenerror")
                return None
        else:
            print("Scanningerror")
            return None
        
    return token_list

# function to return precedence of operators
def precedence(c):
    if c == '^':
        return 3
    elif c in ('*', '/'):
        return 2
    elif c in ('+', '-'):
        return 1
    else:
        return -1
# function to check if operator is right-associative
def isRightAssociative(c):
    return c == '^'

# function to check if a character is an operator
def isOperator(c):
    return c in "+-*/^"
    
#from infix to prefix, needed for parsing(GeeksforGeeks)
def infix_to_prefix(tokens):
    st =[]
    result = []

    #scan from right to left

    for t in reversed(tokens):
        if(t.getType() == "number"):
            result.append(t)
        elif t.getType() == ")":
            st.append(t)
        elif t.getType() == '(':
            while st and st[-1].getType() != ')':
                result.append(st.pop())
            if st:
                st.pop()  # remove ')'
        elif isOperator(t.getType()):
            while (st and isOperator(st[-1].getType()) and
                  (precedence(st[-1].getType()) > precedence(t.getType()) or
                  (precedence(st[-1].getType()) == precedence(t.getType()) and isRightAssociative(t.getType())))):
                result.append(st.pop())
            st.append(t)
    # pop remaining operators
    while st:
        result.append(st.pop())

    # reverse at the end to get correct prefix
    endresult=[]
    for x in reversed(result):
        endresult.append(x)
    return endresult
#LL(1)-parsing with table

#dictonary as parsing table

parse_table = {
    ("E", "number"):["number"],
    ("E", "+"):["Op", "E","E"],
    ("E", "-"):["Op", "E","E"],
    ("E", "*"):["Op", "E","E"],
    ("E", "/"):["Op", "E","E"],
    ("Op", "+"):["+"],
    ("Op", "-"):["-"],
    ("Op", "*"):["*"],
    ("Op", "/"):["/"],


}

def parse_tokens(tokens):
    stack = ["$", "E"]
    tokens.append(tkn.Token("","$"))
    i=0
    while stack:
        top = stack[-1]
        current = tokens[i]

        if top == current.getType() == '$':
            return True
        elif top == current.getType():
            stack.pop()
            i += 1
        elif top in ["E", "Op"]:
            production = parse_table.get((top, current.getType()))
            if not production:   
                return False
            stack.pop()
            if production != ['ε']:
                for symbol in reversed(production):
                    stack.append(symbol)
        else:
            return False
    return False



def calculate(parsed_tokens):
    if len(parsed_tokens) == 1:
        return parsed_tokens[0].getValue()
    else:
        stack = []

        for x in reversed(parsed_tokens):
            if x.getType() == "number":
                stack.append(x.getValue())
            if x.getType() == "+":
                a = stack.pop()
                b = stack.pop()
                c = a + b
                stack.append(c)
            if x.getType() == "-":
                a = stack.pop()
                b = stack.pop()
                c = a - b
                stack.append(c)
            if x.getType() == "*":
                a = stack.pop()
                b = stack.pop()
                c = a * b
                stack.append(c)
            if x.getType() == "/":
                a = stack.pop()
                b = stack.pop()
                c = a / b
                stack.append(c)
        return stack[0]
    

def calculator(input):
    tokens = scanning_alg(input)
    if tokens == None:
        return "Eingabe Falsche"
    prefix_tokens = infix_to_prefix(tokens)
    if parse_tokens(prefix_tokens) == True:
        return calculate(prefix_tokens)
    else:
        return "Kein arithmetischer Ausdruck"



def main():
    expressions = [
    "(3+5)*(2-8)/4+7",
    "12*(6+(4-2)*3)-5",
    "((15/(7-(1+1)))*3)-(2+(1+1))",
    "4*(3+(2*(1+5)))/(7-2)",
    "((8+2)*(3-1))-(10/(5-3))",
    "(9+(3*(8-(4/2))))-(6/3)",
    "(7*(3+(2-(1+(4/2)))))+5",
    "((10-(2*3))*(6/3))+(8*(4-1))",
    "(5+3)*((2+8)/(3-1))-(7*2)",
    "(((4*3)+(2*(1+1)))-(8/(2+2)))*2",
    "2.3",
    
]
    
    i=1
    for x in expressions:
        print(calculator(x))

    

#main()
    

