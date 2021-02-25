import operator
from typing import List

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


def evaluate(expression: List[str], eval_stack=None):
    if eval_stack is None:
        eval_stack = []
    total = 0
    eval_stack += expression
    print(eval_stack)
    op = operator.add
    while op:
        current = eval_stack.pop(0)
        print(f'current: {current}')

        print(eval_stack)
        if current == '(':
            current = evaluate([], eval_stack)

        total = op(total, int(current))
        print(f'total: {total}')
        if eval_stack:
            op = OPS[eval_stack.pop(0)]
        else:
            op = None
        print(eval_stack)
        print('------------------')

    return total


def solution_2(problem):

    return NotImplemented


if __name__ == '__main__':
    with open('inputs/day18.txt', 'r') as f:
        _input = [line.strip() for line in f.readlines()]
        print(solution_linear(_input))


