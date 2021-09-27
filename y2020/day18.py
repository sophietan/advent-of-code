import operator
from typing import List, Any

OPS = {
    '+': operator.add,
    '*': operator.mul,
    ')': 0
}


def solution(expressions: List[str]):
    total = 0

    for ex in expressions:
        ex = ex.replace('(', ' ( ')
        ex = ex.replace(')', ' ) ')
        e = ex.split()
        total += evaluate(e)
    return total


def evaluate(expression: List[str]):
    total = 0
    op = operator.add

    while expression:
        token = expression.pop(0)

        if token.isdigit():
            value = int(token)
            total = op(total, value)
        elif token == '+':
            op = operator.add
        elif token == '*':
            op = operator.mul
        elif token == '(':
            val = evaluate_expression(expression)
            total = op(total, val)
        elif token == ')':
            break
    return total


def evaluate_expression(expression: list[str]):
    """Multiplication is distributive! DUH!"""
    total = 0
    multiplier = 1
    while expression:
        token = expression.pop(0) # can also used a dequeue as well.
        if token.isdigit():
            value = int(token)
            total += multiplier * value
        elif token == '*':
            multiplier = total
            total = 0
        elif token == '(':
            val = evaluate_expression(expression)
            total += multiplier * val
        elif token == ')':
            break
    return total


def solution_2(expressions: list[str]):
    total = 0
    for ex in expressions:
        tokens = ex.replace('(', '( ').replace(')', ' )')
        total += evaluate_expression(tokens.split())

    return total


if __name__ == '__main__':
    with open('inputs/day18.txt', 'r') as f:
        _input = [line.strip() for line in f.readlines()]
        print(solution_2(_input))


