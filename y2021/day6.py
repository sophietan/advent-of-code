from collections import Counter


def solution(fish_ages: list[int], days: int = 80):
    fish_count = [0] * 9
    counter = Counter(fish_ages)
    for day, count in counter.items():
        fish_count[day] = count
    for _ in range(days):
        # decrement day
        zeros = fish_count.pop(0)
        # zeros become sixes
        fish_count[6] += zeros
        # Add on the new fish
        fish_count += [0] * 9
        fish_count[8] = zeros
    print(sum(fish_count))


if __name__ == '__main__':
    with open('input/day6.txt', 'r') as f:
        input_data = [int(f) for f in f.read().split(',')]
        print(solution(input_data, 256))
