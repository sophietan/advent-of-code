import dataclasses
from enum import Enum
from typing import Tuple, List


class Direction(Enum):
    N = 'N'
    S = 'S'
    E = 'E'
    W = 'W'
    L = 'L'
    R = 'R'
    F = 'F'


@dataclasses.dataclass
class Ship:
    current_position: Tuple[int, int] = (0, 0)
    waypoint_position: Tuple[int, int] = (10, 1)
    current_direction: Direction = Direction.E
    compass = [Direction.N, Direction.E, Direction.S, Direction.W]

    @property
    def manhattan_distance(self):
        x, y = self.current_position
        return abs(x) + abs(y)

    def parse_instruction(self, instruction: Tuple[Direction, int]):
        direction, distance = instruction
        if direction is Direction.L:
            turns = distance // 90
            pos = self.compass.index(self.current_direction)
            new_direction = self.compass[pos - turns]
            distance = 0
            self.current_direction = new_direction
        elif direction is Direction.R:
            pos = self.compass.index(self.current_direction)
            turns = distance // 90
            new_direction = self.compass[(pos + turns) % 4]
            distance = 0
            self.current_direction = new_direction
        elif direction is Direction.F:
            new_direction = self.current_direction
        else:
            new_direction = direction
        self.current_position = self.move(new_direction, distance, self.current_position)

    def move(self, new_direction: Direction, distance: int, current):
        x, y = current
        if new_direction is Direction.N:
            y += distance
        elif new_direction is Direction.S:
            y -= distance
        elif new_direction is Direction.E:
            x += distance
        elif new_direction is Direction.W:
            x -= distance
        else:
            raise RuntimeError('Unsupported direction.')
        return x, y

    def parse_instructions_2(self, instruction: Tuple[Direction, int]):
        direction, distance = instruction
        if direction is Direction.L or direction is Direction.R:
            x, y = self.current_position
            if (distance == 90 and direction is Direction.L) or (distance == 270 and direction is Direction.R):
                w_x, w_y = self.waypoint_position
                w_y *= - 1
                self.waypoint_position = w_y, w_x
            elif distance == 180:
                w_x, w_y = self.waypoint_position
                w_x *= -1
                w_y *= -1
                self.waypoint_position = w_x, w_y
            elif (distance == 270 and direction is Direction.L) or (distance == 90 and direction is Direction.R):
                w_x, w_y = self.waypoint_position
                w_x *= -1
                self.waypoint_position = w_y, w_x
        elif direction is Direction.F:
            x, y = self.current_position
            w_x, w_y = self.waypoint_position
            x += (distance * w_x)
            y += (distance * w_y)
            self.current_position = x, y
        else:
            new_direction = direction
            self.waypoint_position = self.move(new_direction, distance, self.waypoint_position)


def solution_1(instructions: List[Tuple]):
    ship = Ship()
    for instruction in instructions:
        ship.parse_instruction(instruction)
    return ship.manhattan_distance


def solution_2(instructions: List[Tuple]):
    ship = Ship()
    for instruction in instructions:
        ship.parse_instructions_2(instruction)
    return ship.manhattan_distance


if __name__ == '__main__':
    with open('inputs/day12.txt', 'r') as f:
        instructions = []
        for line in f.readlines():
            line.strip()
            instructions.append((Direction[line[0]], int(line[1:])))

    # print(solution_1(instructions))
    print(solution_2(instructions))

