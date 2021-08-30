from pprint import pprint


def solution(no_insertions) -> int:
    buffer = [0, 1]
    step = 312
    current = 1
    for insertion_count in range(2, no_insertions + 1):
        next_pos = next_position(current, step, len(buffer))
        buffer.insert(next_pos, insertion_count)
        current = next_pos
    return buffer[current + 1]


def next_position(position, step, buffer_size) -> int:
    return (position + step) % buffer_size + 1


def solution_2():
    buffer = [0, 1]
    step = 312
    current = 1
    for insertion_count in range(2, 50_000_000 + 1):
        next_pos = next_position(current, step, len(buffer))
        buffer.insert(next_pos, insertion_count)
        current = next_pos
    index = buffer.index(0)
    return buffer[index + 1]


if __name__ == '__main__':
    print(solution_2())
