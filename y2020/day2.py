from typing import List


def solution(problem: List[str]):
    num_valid = 0
    for line in problem:
        min_max, letter, password = line.split()
        min_, max_ = min_max.split('-')
        count = password.count(letter[0])
        if int(min_) <= count <= int(max_):
            num_valid += 1

    return num_valid


def solution_2(problem: List[str]):
    num_valid = 0
    for line in problem:
        min_max, letter, password = line.split()
        min_, max_ = min_max.split('-')
        letter = letter[0]
        a = password[int(min_) - 1]
        b = password[int(max_) - 1]
        num_valid += a == letter ^ b == letter

    return num_valid


if __name__ == '__main__':
    with open('inputs/day2.txt', 'r') as f:
        _input = [n.strip('\n') for n in f.readlines()]
        print(solution_2(_input))
