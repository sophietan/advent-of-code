from collections import defaultdict
from typing import List


def solution(adapters: List[int]):
    diffs = defaultdict(int)
    highest = max(adapters)
    adapters = [0] + adapters + [highest + 3]
    previous_adapter = 0
    for adapter in adapters:
        diff = adapter - previous_adapter
        diffs[diff] += 1
        previous_adapter = adapter
    return diffs[1] * diffs[3]


def solution_2(adapters: List[int]):
    permutations = defaultdict(int)
    highest = max(adapters)
    adapters = [0] + adapters + [highest + 3]
    permutations[0] = 1
    for adapter in adapters:
        permutations[adapter] += permutations[adapter - 1]
        permutations[adapter] += permutations[adapter - 2]
        permutations[adapter] += permutations[adapter - 3]

    return permutations[adapters[-1]]


if __name__ == '__main__':
    with open('../y2020/inputs/day10.txt', 'r') as f:
        adapters = [int(n.strip('\n')) for n in f.readlines()]
        adapters.sort()
        print(solution_2(adapters))