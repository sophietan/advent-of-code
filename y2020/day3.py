from pprint import pprint
from typing import List


def solution(problem: List[str], multiplier: int = 3, skip: int = 1):
    trees = 0
    for i, line in enumerate(problem[::skip]):
        line *= 100
        if line[i * multiplier] == '#':
            trees += 1
    return trees


def solution_2(problem: List[str]):
    args = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total = 1
    for a, b in args:
        total *= solution(problem, a, b)

    return total


if __name__ == '__main__':
    with open('inputs/day3.txt', 'r') as f:
        _input = [n.strip('\n') for n in f.readlines()]
        pprint(solution_2(_input))
