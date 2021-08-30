from typing import List, Union


def solution_1(time: int, ids: List[int]):
    results = []
    shortest = None
    nearest_bus = None
    print(time)
    for bus in ids:
        multiplier = (time + bus) // bus
        next_bus = multiplier * bus
        remainder = next_bus - time
        print(bus, multiplier, next_bus, remainder)
        if shortest is None:
            shortest = remainder
            nearest_bus = bus
        else:
            if remainder < shortest:
                shortest = remainder
                nearest_bus = bus
    return shortest * nearest_bus


# Chinese Remainder Theorem - are you kidding me?!
def solution_2(schedule: List[Union[str, int]]):
    m_factor = 1
    coefficients = []
    simplified = []
    for s in schedule:
        bus, _ = s
        m_factor *= bus
    for s in schedule:
        bus, minutes = s
        coefficients.append((m_factor // bus, bus))
    for c in coefficients:
        thing, bus = c
        m, r = divmod(thing, bus)
        simple = thing - (m * bus)
        simplified.append((simple, bus))
    print(schedule)
    print(m_factor)
    print(coefficients)
    print(simplified)


def find_congruence(factor, modulo):
    return NotImplemented


if __name__ == '__main__':
    with open('inputs/day13.txt') as f:
        contents = f.readlines()
        timestamp = int(contents[0])
        bus_ids = []
        part_2 = []
        for index, value in enumerate(contents[1].split(',')):
            if value.isnumeric():
                bus_ids.append(int(value))
                part_2.append((int(value), index))

    # print(solution_1(timestamp, bus_ids))
    solution_2(part_2)
