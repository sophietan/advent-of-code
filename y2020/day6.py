from pprint import pprint
from typing import List


def solution(input: List[str]):
    questions = set()
    count = 0
    for line in input:
        entry = line.strip()
        if entry == '':
            count += len(questions)
            questions = set()
        questions = questions | set(entry)
    questions = questions | set(entry)
    count += len(questions)
    return count


def solution_2(input: str):
    questions = None
    count = 0
    groups = group_string(input)
    pprint(groups)
    for group in groups:
        for entry in group:
            if questions is None:
                questions = set(entry)
            else:
                questions = questions & set(entry)
        count += len(questions)
        questions = None

    return count


def group_string(string: str) -> List[List[str]]:
    groups = []
    group = []
    for line in string.splitlines():
        if not line:
            groups.append(group)
            group = []
        else:
            group.append(line)
    groups.append(group)
    return groups


if __name__ == '__main__':
    with open('y2020/inputs/day6.txt', 'r') as f:

        # pprint(solution(f.readlines()))
        pprint(solution_2(f.read()))
