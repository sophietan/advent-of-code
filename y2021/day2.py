
class Submarine:
    def __init__(self,
                 input_data):
        self.depth = 0
        self.horizontal = 0
        self.instructions = input_data
        self.aim = 0

    def forward(self, unit: int):
        self.horizontal += unit
        self.depth += self.aim * unit

    def up(self, unit: int):
        self.aim -= unit

    def down(self, unit: int):
        self.aim += unit

    def calculate_result(self):
        return self.depth * self.horizontal

    def process_instructions(self):
        for x, y in self.instructions:
            func = self.__getattribute__(x)
            func(int(y))

        return self.calculate_result()


def solution(input_data: list):
    depth = 0
    aim = 0
    horizontal = 0
    for direction, unit in input_data:
        if direction == 'forward':
            horizontal += int(unit)
            depth += aim * int(unit)
        elif direction == 'up':
            aim -= int(unit)
        elif direction == 'down':
            aim += int(unit)
        else:
            raise RuntimeError('Unsupported direction')

    return depth * horizontal


if __name__ == '__main__':
    with open('input/day2.txt', 'r') as f:
        instructions = [line.split() for line in f.readlines()]
        print(solution(instructions))