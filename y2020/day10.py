from pprint import pprint
from typing import List


def solution(jolts: List[int]):
    hist = {1: 0, 2: 0, 3: 0}
    highest = max(jolts)
    jolts = [0] + jolts + [highest + 3]
    previous_jolt = 0
    for jolt in jolts:
        diff = jolt - previous_jolt
        if 4 > diff > 0:
            hist[diff] += 1
        previous_jolt = jolt
    return hist[1] * hist[3]


def solution_2(problem: List[int]):
    return NotImplemented


if __name__ == '__main__':
    with open('../y2020/inputs/day10.txt', 'r') as f:
        jolts = [int(n.strip('\n')) for n in f.readlines()]
        jolts.sort()
        print(solution(jolts))