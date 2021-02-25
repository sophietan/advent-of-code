from pprint import pprint
from typing import List


def solution(wire_1: List[str], wire_2: List[str]):
    x, y = (0, 0)
    directions = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1)}
    seen = {(x, y)}
    shortest = 99999999
    for path in wire_1:
        dx, dy = directions[path[0]]
        for _ in range(int(path[1:])):
            x += dx
            y += dy
            seen.add((x, y))

    x, y = (0, 0)
    for path in wire_2:
        dx, dy = directions[path[0]]
        for _ in range(int(path[1:])):
            x += dx
            y += dy
            if (x, y) in seen:
                dist = abs(x) + abs(y)
                shortest = min(shortest, dist)
            else:
                seen.add((x, y))

    return shortest


def solution_2(wire_1: List[str], wire_2: List[str]):
    x, y = (0, 0)
    directions = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1)}
    path_1 = {}
    step = 0
    for path in wire_1:
        dx, dy = directions[path[0]]
        for _ in range(int(path[1:])):
            x += dx
            y += dy
            step += 1
            path_1[(x, y)] = step

    x, y = (0, 0)
    step = 0
    path_2 = {}
    for path in wire_2:
        dx, dy = directions[path[0]]
        for _ in range(int(path[1:])):
            x += dx
            y += dy
            step += 1
            path_2[(x, y)] = step

    intersections = path_1.keys() & path_2.keys()
    signal = 99999999

    for p in intersections:
        signal = min(path_1[p] + path_2[p], signal)
        pprint(signal)
        # pprint(f'{p}: path_1 + path_2 = {path_1[p]} + {path_2[p]}')

    # pprint(intersections)
    # signal = min(path_1[p] + path_2[p] for p in intersections)
    # pprint(signal)


if __name__ == '__main__':
    with open('y2019/inputs/day3.txt', 'r') as f:
        wire_1, wire_2 = f.readlines()
        pprint(solution_2(wire_1=wire_1.strip().split(','),
                          wire_2=wire_2.strip().split(',')))
