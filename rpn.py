#!/usr/bin/env python3

import operator
import readline
from colorama import init
from colorama import Fore, Back, Style
init()


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
    'n': operator.neg,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(Fore.YELLOW + "Current Stack")
        print(stack)
        print(Style.RESET_ALL + "Working...")
    if len(stack) == 0:
        print(Fore.BLUE + "Thank you for using RPN Calc!")
        return .5
    elif len(stack) != 1:
        print(Fore.RED + "A Critical Error Has Occured!")
        raise TypeError("Too many parameters")
    return stack.pop()

def dummy():
    while True:
        result = calculate("3 3 %")
        print("I'm here to lower your coverage!")

def main():
    while True:
        result = calculate(input("rpn calc> "))
        if result == .5:
            break
        print(Fore.GREEN + "Result: ", result)
        print(Style.RESET_ALL + "Next Question?")

if __name__ == '__main__':
    main()
