from State import *
from token1 import *
from Transition import *
class DFA:
    def __init__(self, rank):
        self.transition_list = []
        self.state_list = []
        self.rank = rank#int
    def addTransition(self, pTransition):
        self.transition_list.append(pTransition)
    def addState(self, pState):
        self.state_list.append(pState)
    #check the longest accepted prefix of an input
    def longest_prefix(self, input):
        longest_accepted_prefix = ""
        scanned_prefix = ""
        current_state = self.state_list[0]
        while(len(input)>0):
            c = input[0]
            tran_exists = False
            for x in self.transition_list:
                if x.getStart() == current_state and x.getInput() == c:
                    current_state = x.getEnd()
                    tran_exists = True
            if(tran_exists == False):
                break
            scanned_prefix += c
            if current_state.getIsAccepting() == True:
                longest_accepted_prefix = scanned_prefix
            input = input[1:]
        return longest_accepted_prefix
    
def generate_DFAs():
    DFA_list = []
    #-DFA
    minus = DFA(0)
    minus.addState(State("q0", False))
    minus.addState(State("q1", True))
    minus.addTransition(Transition(minus.state_list[0], "-", minus.state_list[1]))
    DFA_list.append(minus)
    #+DFA
    plus = DFA(1)
    plus.addState(State("q0", False))
    plus.addState(State("q1", True))
    plus.addTransition(Transition(plus.state_list[0], "+", plus.state_list[1]))
    DFA_list.append(plus)
    #*DFA
    mult = DFA(2)
    mult.addState(State("q0", False))
    mult.addState(State("q1", True))
    mult.addTransition(Transition(mult.state_list[0], "*", mult.state_list[1]))
    DFA_list.append(mult)
    #-DFA
    div = DFA(3)
    div.addState(State("q0", False))
    div.addState(State("q1", True))
    div.addTransition(Transition(div.state_list[0], "/", div.state_list[1]))
    DFA_list.append(div)
    #(DFA
    o_brack = DFA(4)
    o_brack.addState(State("q0", False))
    o_brack.addState(State("q1", True))
    o_brack.addTransition(Transition(o_brack.state_list[0], "(", o_brack.state_list[1]))
    DFA_list.append(o_brack)
    #)DFA
    c_brack = DFA(5)
    c_brack.addState(State("q0", False))
    c_brack.addState(State("q1", True))
    c_brack.addTransition(Transition(c_brack.state_list[0], ")", c_brack.state_list[1]))
    DFA_list.append(c_brack)
    #DFA for negative number
    #for negativ numbers
    number = DFA(6)
    number.addState(State("q0", False))
    number.addState(State("q1", True))
    number.addState(State("q2", False))
    number.addState(State("q3", False))
    number.addState(State("q4", True))
    number.addTransition(Transition(number.state_list[0], "~", number.state_list[2]))
    number.addTransition(Transition(number.state_list[1], ".", number.state_list[3]))
    x = 0
    while x < 10:
        
        number.addTransition(Transition(number.state_list[2], str(x), number.state_list[1]))
        number.addTransition(Transition(number.state_list[1], str(x), number.state_list[1]))
        number.addTransition(Transition(number.state_list[3], str(x), number.state_list[4]))
        number.addTransition(Transition(number.state_list[4], str(x), number.state_list[4]))
        x = x+1
    DFA_list.append(number)
    #pos. numbers
    number1 = DFA(7)
    number1.addState(State("q0", False))
    number1.addState(State("q1", True))
    number1.addState(State("q2", False))
    number1.addState(State("q3", True))
    number1.addTransition(Transition(number1.state_list[1], ".", number1.state_list[2]))
    x = 0
    while x < 10:
        
        number1.addTransition(Transition(number1.state_list[0], str(x), number1.state_list[1]))
        number1.addTransition(Transition(number1.state_list[1], str(x), number1.state_list[1]))
        number1.addTransition(Transition(number1.state_list[2], str(x), number1.state_list[3]))
        number1.addTransition(Transition(number1.state_list[3], str(x), number1.state_list[3]))
        x = x+1
    DFA_list.append(number1)

    return DFA_list