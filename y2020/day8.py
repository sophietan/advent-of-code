from typing import List


class Game:
    def __init__(self, instructions: List[str]):
        self.instructions = instructions
        self.position = 0
        self.prev_position = 0
        self.score = 0
        self.seen = set()

    def acc(self, arg: int):
        self.score += arg
        self.seen.add(self.position)
        self.prev_position = self.position
        self.position += 1

    def jmp(self, arg: int):
        self.seen.add(self.position)
        self.prev_position = self.position
        self.position += arg

    def nop(self, arg: int):
        self.seen.add(self.position)
        self.prev_position = self.position
        self.position += 1

    def reset(self):
        self.position = 0
        self.seen = set()
        self.prev_position = 0
        self.score = 0

    def process(self):
        while self.position not in self.seen and self.position < len(self.instructions):
            instruction = self.instructions[self.position]
            i, arg = instruction.strip().split()
            op = getattr(self, i)
            op(int(arg))
        else:
            if self.position < len(self.instructions):
                old = self.instructions[self.prev_position]
                self.instructions[self.prev_position] = old.replace('jmp', 'nop')
                self.reset()
                self.process()
            print(self.score)


def main():
    with open('../y2020/inputs/day8.txt', 'r') as f:
        g = Game(f.readlines())
        g.process()


if __name__ == '__main__':
    main()
