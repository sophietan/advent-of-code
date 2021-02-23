from itertools import combinations
from typing import List


def solution_1(_input: List[int]):
    for i in range(len(_input) - 25):
        window = _input[i:i+26]
        sums = set()
        for pair in combinations(window[:25], 2):
            sums.add(pair[0] + pair[1])
        if window[-1] not in sums:
            print(window[-1])
            return _input[:i+25], window[-1]
    return 0


def solution_2(_input: List[int], target: int):
    find_subarray_sum(_input, target)


def find_subarray_sum(_input: List[int], target: int):
    current_sum = 0
    look_up = {}
    print(_input)
    for i in range(0, len(_input)):
        current_sum = current_sum + _input[i]
        if current_sum == target:
            print(f'Sum found between 0 to {i}')
            low = min(_input[:i])
            high = max(_input[:1])
            print(low + high)
            return

        if current_sum - target in look_up:
            print(f'Sum found between {look_up[current_sum - target] + 1} to {i + 1}')
            start = look_up[current_sum - target] + 1
            end = i + 1
            low = min(_input[start:end + 1])
            high = max(_input[start:end + 1])
            print(low + high)
            return

        look_up[current_sum] = i

    raise ValueError('No solution')


if __name__ == '__main__':
    with open('../y2020/inputs/day9.txt', 'r') as f:
        _input = [int(n.strip('\n')) for n in f.readlines()]
        subarray, target = solution_1(_input)
        solution_2(subarray, target)
