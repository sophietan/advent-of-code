from pprint import pprint
from typing import List


def solution(input: List[str]):
    highest = -1
    seats = {r * 8 + c for r in range(128) for c in range(8)}

    for bp in input:
        row = [n for n in range(128)]
        column = [m for m in range(8)]
        for char in bp.strip():
            mid_row = len(row) // 2
            if len(row) == 1:
                row = row
            elif char == 'F':
                row = row[:mid_row]
            elif char == 'B':
                row = row[mid_row:]

            mid_col = len(column) // 2
            if len(column) == 1:
                column = column
            elif char == 'L':
                column = column[:mid_col]
            elif char == 'R':
                column = column[mid_col:]
        uid = row[0] * 8 + column[0]
        seats.discard(uid)
        if uid > highest:
            highest = uid
    pprint(seats)

    return highest


def solution_2(input: List[str]):
    pass


if __name__ == '__main__':
    with open('y2020/inputs/day5.txt', 'r') as f:
        pprint(solution(f.readlines()))
        # pprint(solution_2(f.readlines()))
