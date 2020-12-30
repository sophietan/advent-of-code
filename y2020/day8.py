from pprint import pprint
from typing import List


class Game:
    def __init__(self, instructions: List[str]):
        self.instructions = instructions
        self.position = 0
        self.score = 0

    def acc(self, arg: int):
        self.score += arg
        self.position += 1

    def jmp(self, arg: int):
        self.position += 1

    def nop(self):
        self.position += 1

    def process(self):
        for instruction in self.instructions:
            instruction = self.instructions[self.position]
            i, arg = instruction.strip().split()
            op = getattr(self, i)
            op(int(arg))

def main():
    with open('y2020/inputs/day8.txt', 'r') as f:
        g = Game(f.readlines())
        g.process()
        # pprint(f.readlines())



if __name__ == '__main__':
    main()
