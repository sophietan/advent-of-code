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


def solution_2(report: list[list[str]]):
    report_len = len(report)
    freq = count_frequency(report)

    most_common_bits = ''.join(
        ['1' if count >= (report_len // 2) else '0' for count in freq]
    )
    least_common_bits = ''.join(
        ['0' if count >= (report_len // 2) else '1' for count in freq]
    )
    o2 = filter_values(report, most_common_bits)
    co = filter_values(report, least_common_bits)

    return int(o2, 2) * int(co, 2)


def filter_values(numbers: list, bit_criteria: str):
    copy = numbers.copy()
    pos = 0
    byte_len = len(numbers[0])
    while len(copy) > 1 and pos < byte_len:
        copy = list(filter(lambda line: line[pos] == bit_criteria[pos], copy))
        pos += 1
    return copy[0]


if __name__ == '__main__':
    with open('input/day3.txt', 'r') as f:
        data = [b.strip() for b in f.readlines()]
        # print(solution_1(data))
        print(solution_2(data))