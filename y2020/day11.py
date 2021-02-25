from pprint import pprint
from typing import List


def solution(arrangement: List[str]):
    copy = arrangement.copy()
    keep_going = True
    while keep_going:
        seats = 0
        for i, row in enumerate(arrangement):
            for j, col in enumerate(row):
                copy = fill_seats(i, j, arrangement, copy)
                seats += row.count('#')
        if arrangement == copy:
            pprint(copy)
            pprint(seats)
            keep_going = False
        arrangement = copy.copy()


def fill_seats(i: int, j: int, arrangement: List[str], copy: List[str]):
    to_check = [(i - 1, j - 1),
                (i, j - 1),
                (i - 1, j),
                (i - 1, j + 1),
                (i + 1, j - 1),
                (i, j + 1),
                (i + 1, j),
                (i + 1, j + 1)]
    seat_count = {'L': 0, '#': 0, '.': 0}
    for r, c in to_check:
        try:
            pos = arrangement[r][c]
            seat_count[pos] += 1
        except IndexError:
            continue
    #
    # pprint(seat_count)
    # pprint(arrangement[i][j])
    if arrangement[i][j] == 'L' and seat_count['#'] == 0:
        tmp = copy[i]
        pprint(tmp)
        new = tmp[:j] + '#' + tmp[j+1:]
        copy[i] = new
    if arrangement[i][j] == '#' and seat_count['#'] > 3:
        tmp = copy[i]
        new = tmp[:j] + 'L' + tmp[j+1:]
        copy[i] = new

    return copy


def solution_2(problem: List[str]):

    return NotImplemented


if __name__ == '__main__':
    with open('inputs/day11.txt', 'r') as f:
        arrangement = [line.strip() for line in f.readlines()]
        solution(arrangement)
