from pprint import pprint


def solution_1(heightmap: list):
    total_risk = 0
    for row, tube in enumerate(heightmap):
        for col, height in enumerate(tube):
            h = int(height)
            if check_low_point(row, col, h, heightmap):
                total_risk += h + 1
    return total_risk


def check_low_point(row, col, height, heightmap):
    max_width = len(heightmap[0])
    max_depth = len(heightmap)
    to_check = [(row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1)]
    checks = []
    for r, c in to_check:
        try:
            if r == max_depth or r == - 1 or c == max_width or c == -1:
                continue
            other = int(heightmap[r][c])
            checks.append(other > height)
        except IndexError as e:
            continue
    return all(checks)


if __name__ == '__main__':
    with open('input/day9.txt', 'r') as f:
        lines = f.read().splitlines()
        pprint(lines)
        print(solution_1(lines))
