from typing import List


def solution(problem: List[int], goal: int = 2020):
    lookup = {}
    for line in problem:
        diff = goal - line
        if line in lookup:
            return line * lookup[line]
        else:
            lookup[diff] = line


def solution_2(problem: List[int]):
    for line in problem:
        goal = 2020 - line
        partial = solution(problem, goal)
        if partial is not None:
            return partial * line


if __name__ == '__main__':
    with open('inputs/day1.txt', 'r') as f:
        input = [int(n.strip('\n')) for n in f.readlines()]
        print(solution_2(input))