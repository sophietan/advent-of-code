import re
from typing import Dict, NamedTuple, List

LINE_FMT = re.compile(r'^(?P<colour>.+) bags contain '
                      r'((?P<no_inside>no other bags)'
                      r'|'
                      r'(?P<inside>.+?))'
                      r'\.\n?$')

SHINY = 'shiny gold'


class InsideThing(NamedTuple):
    count: int
    colour: str


def read_input() -> Dict[str, List[InsideThing]]:
    tree = {}
    with open('y2020/inputs/day7.txt', 'r') as f:
        for line in f.readlines():
            match = LINE_FMT.match(line)
            colour = match.group('colour')
            tree[colour] = []
            if not match.group('no_inside'):
                for thing in match.group('inside').split(', '):
                    count_str, thing = thing.split(maxsplit=1)
                    inside_colour, _ = thing.rsplit(maxsplit=1)
                    tree[colour].append(InsideThing(int(count_str), inside_colour))
    return tree


def has_shiny(colour: str, problem):
    for thing in problem[colour]:
        if thing.colour == SHINY or has_shiny(thing.colour, problem):
            return True
    return False


def part1(problem: Dict[str, List[InsideThing]]) -> int:
    return sum(has_shiny(colour, problem) for colour in problem)


def inside_bag_count(colour: str, problem) -> int:
    return sum(thing.count * (1 + inside_bag_count(thing.colour, problem))
               for thing in problem[colour])


def part2(problem: Dict[str, List[InsideThing]]) -> int:
    return inside_bag_count(SHINY, problem)


if __name__ == '__main__':
    print(part1(read_input()))
    print(part2(read_input()))
