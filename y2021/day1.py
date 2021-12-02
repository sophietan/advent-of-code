def solution_1(measurements: list[int]):
    inc = 0
    prev_val = measurements[0]

    for m in measurements[1:]:
        if m > prev_val:
            inc += 1
        prev_val = m
    return inc


def solution_2(measurements: list[int]):
    inc = 0
    for i, m in enumerate(measurements):
        if (i < len(measurements) - 3) and m < measurements[i+3]:
            inc += 1
    return inc


if __name__ == '__main__':
    with open('input/day1.txt', 'r') as f:
        data = [int(m) for m in f.readlines()]
        # print(solution_1(data))
        print(solution_2(data))
