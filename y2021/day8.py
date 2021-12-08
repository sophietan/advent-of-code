import math


def solution_1(data: list):
    # len of signal to digit map
    known_digits = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }
    count = 0
    for _, output in data:
        lengths = map(len, output)
        for d in lengths:
            if d in known_digits.keys():
                count += 1
    return count


def solution_2(data: list):
    total = 0
    for signals, output in data:
        mapping = {i: '?' for i in range(10)}

        find_unique(signals, mapping)
        two_three_five = [v for v in filter(lambda x: len(x) == 5, signals)]
        six_nine_zero = [v for v in filter(lambda x: len(x) == 6, signals)]
        find_three(two_three_five, mapping)
        find_nine(six_nine_zero, mapping)
        find_zero(six_nine_zero, mapping)
        find_six(six_nine_zero, mapping)
        find_five(two_three_five, mapping)
        find_two(two_three_five, mapping)

        signal_to_digit = dict((v, k) for k, v in mapping.items())
        print(mapping)
        print(output)

        for i, signal in enumerate(output):
            exponent = len(output) - 1 - i
            total += math.pow(10, exponent) * signal_to_digit[signal]
    return total


def find_unique(signals: list[str], mapping: dict[int, str]) -> dict[int, str]:
    for s in signals:
        if len(s) == 2:
            mapping[1] = s
        if len(s) == 3:
            mapping[7] = s
        if len(s) == 7:
            mapping[8] = s
        if len(s) == 4:
            mapping[4] = s
    return mapping


def find_three(two_three_five: list[str], mapping: dict[int, str]) -> dict[int, str]:
    for signal in two_three_five:
        if all([e in set(signal) for e in mapping[1]]):

            mapping[3] = signal
    return mapping


def find_nine(six_nine_zero: list[str], mapping: dict[int, str]) -> dict[int, str]:
    for signal in six_nine_zero:
        elements = set(signal)
        if (all(e in elements for e in mapping[4])
                and all(e in elements for e in mapping[3])):
            mapping[9] = signal
    return mapping


def find_zero(six_nine_zero: list[str], mapping: dict[int, str]) -> dict[int, str]:
    for signal in six_nine_zero:
        if (all(e in set(signal) for e in mapping[1])
                and signal != mapping[9]):
            mapping[0] = signal
    return mapping


def find_six(six_nine_zero: list[str], mapping: dict[int, str]) -> dict[int, str]:
    for signal in six_nine_zero:
        if signal != mapping[0] and signal != mapping[9]:
            mapping[6] = signal
    return mapping


def find_five(two_three_five: list[str], mapping: dict[int, str]) -> dict[int, str]:
    print(mapping)
    for signal in two_three_five:
        print(signal)
        if all(e in mapping[6] for e in signal):
            mapping[5] = signal
    return mapping


def find_two(two_three_five: list[str], mapping: dict[int, str]) -> dict[int, str]:
    for signal in two_three_five:
        if signal != mapping[5] and signal != mapping[3]:
            mapping[2] = signal
    return mapping


if __name__ == '__main__':
    with open('input/day8.txt', 'r') as f:
        data = []
        raw_data = []
        for line in f.readlines():
            raw_signals, raw_digits = line.strip().split(' | ')
            raw_data.append([''.join(raw_signals.split()), ''.join(raw_digits.split())])
            s = [''.join(sorted(s)) for s in raw_signals.split()]
            d = [''.join(sorted(d)) for d in raw_digits.split()]
            data.append([s, d])
    print(solution_2(data))
