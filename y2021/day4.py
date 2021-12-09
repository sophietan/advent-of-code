import operator
from functools import reduce
from pprint import pprint


class BingoBoard:

    def __init__(self,
                 board_numbers: list,
                 board_size = 5):
        self.numbers = board_numbers.copy()
        self.unmatched_numbers = board_numbers.copy()
        self.matched_indices = []
        self.score = sum(board_numbers)
        self.board_size = board_size
        self.won = False
        self.last_num = None

    def check_number(self, number: int):
        if number in self.unmatched_numbers:
            index = self.numbers.index(number)
            self.matched_indices.append(index)
            self.unmatched_numbers.remove(number)
            self.score -= number
            self.won = self.check_if_won(index)
            self.last_num = number

    def check_if_won(self, index: int):
        row, col = divmod(index, self.board_size)

        cols = [i in self.matched_indices for i in range(col, len(self.numbers), self.board_size)]
        if all(cols):
            return True

        start = row * self.board_size
        rows = [j in self.matched_indices for j in range(start, start + self.board_size)]
        if all(rows):
            return True

        return False

    def __str__(self):
        grid = []
        for i in range(self.board_size):
            row = i * self.board_size
            r = ' '.join(str(n) if n in self.unmatched_numbers else 'XX' for n in self.numbers[row: row + self.board_size])
            grid.append(r)
        return '\n'.join(grid)


def solution_1(bingo_numbers: list[int], boards: list[BingoBoard]):
    for num in bingo_numbers:
        for b in boards:
            b.check_number(num)
            if b.won:
                print(b)
                print(b.score, num)
                return b.score * num


def solution_2(bingo_numbers: list[int], boards: list[BingoBoard]):
    won_boards = []
    for num in bingo_numbers:
        for b in boards:
            b.check_number(num)
            if b.won:
                won_boards.append(b)
            if len(won_boards) == len(boards):
                return b.score * b.last_num
    raise RuntimeError('Not everyone wins')


if __name__ == '__main__':
    with(open('input/day4.txt', 'r')) as f:
        data = [line.strip() for line in f.readlines()]
        generated_values = [int(num) for num in data[0].split(',')]
        boards = []
        board_numbers = []
        numbers = []
        for value in data[1:]:
            if value != '':
                numbers.append(value)
            else:
                if len(numbers) == 0:
                    continue
                board_numbers_str = ' '.join(numbers)
                board_numbers = [int(n) for n in board_numbers_str.split()]
                board = BingoBoard(board_numbers)
                boards.append(board)
                numbers = []

            board_numbers = []

        # print(solution_1(generated_values, boards))
        print(solution_2(generated_values, boards))
