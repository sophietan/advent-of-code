import statistics
from collections import Callable


def solution(positions: list[int], fuel_measure: Callable):
    costs = []
    for i in range(len(positions)):
        pos = positions[i]
        fuel_costs = [fuel_measure(p, pos) for p in positions]
        costs.append(sum(fuel_costs))
    return min(costs)


def abs_fuel(pos: int, relative_pos: int):
    return abs(pos - relative_pos)


def increasing_fuel(pos: int, relative_pos: int):
    distance = abs_fuel(pos, relative_pos)
    return distance * (distance + 1) // 2


def solution_2(positions: list[int]):
    costs = []
    crabs = sorted(positions)
    for p in range(min(crabs), max(crabs) + 1):
        fuel_costs = sum([increasing_fuel(p, c) for c in crabs])
        costs.append(fuel_costs)
    return min(costs)


def solution_1_median(positions: list[int]):
    crabs = sorted(positions)
    median = round(statistics.median(crabs))
    return sum(abs(c - median) for c in crabs)


if __name__ == '__main__':
    with open('input/day7.txt', 'r') as f:
        h_positions = [int(p) for p in f.read().strip().split(',')]
        print(solution_2(h_positions))
