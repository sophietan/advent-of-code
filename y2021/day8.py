def solution_1():
    known_digits = {
        1: 2,
        7: 3,
        4: 4,
        8: 7
    }
    pass


if __name__ == '__main__':
    with open('input/day8.txt', 'r') as f:
        data = []
        for line in f.readlines():
            raw_signals, raw_digits = line.strip().split(' | ')
            signals = [''.join(sorted(s)) for s in raw_signals.split()]
            digits = [''.join(sorted(d)) for d in raw_digits.split()]
            data.append([signals, digits])
            # map(raw_signals.split())
            # data.append((signals, output))
        print(data)
        print(len(data))