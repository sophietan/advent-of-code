from collections import Counter
from itertools import count


def solution_1(report: list[list[str]]):
    report_len = len(report)
    freq = count_frequency(report)
    gamma_bits = ['1' if f >= (report_len // 2) else '0' for f in freq]
    epsilon_bits = ['0' if f >= (report_len // 2) else '1' for f in freq]
    gamma = ''.join(gamma_bits)
    epsilon = ''.join(epsilon_bits)
    return int(gamma, 2) * int(epsilon, 2)


def count_frequency(report: list[list[str]]):
    byte_len = len(report[0])
    freq = [0 for _ in range(byte_len)]
    for nums in report:
        for i in range(byte_len):
            freq[i] += int(nums[i])
    return freq


def _solution_2(report: list[str], most_common: str, least_common: str) -> str:
    remaining = report.copy()
    for n in count():
        if len(remaining) == 1:
            return remaining[0]
        counter = Counter(number[n] for number in remaining)
        zeroes = counter.get('0', 0)
        ones = counter.get('1', 0)
        choice = most_common if ones >= zeroes else least_common
        remaining = [number for number in remaining if number[n] == choice]


def solution_2(report: list[str]):
    o2 = _solution_2(report, '1', '0')
    co2 = _solution_2(report, '0', '1')
    return int(o2, 2) * int(co2, 2)


if __name__ == '__main__':
    with open('input/day3.txt', 'r') as f:
        data = [b.strip() for b in f.readlines()]
        # print(solution_1(data))
        print(solution_2(data))
