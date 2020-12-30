from __future__ import annotations

from typing import Tuple, Union


IndexType = Union[Tuple[int, int], Tuple[int, slice], Tuple[slice, int]]


class Map:

    def __init__(self,
                 data: str,
                 wrap_x: bool = False,
                 wrap_y: bool = False) -> None:
        self._data = data.splitlines()
        self.wrap_x = wrap_x
        self.wrap_y = wrap_y

    def __getitem__(self, pos: IndexType) -> Union[Map, str]:
        x, y = pos
        if isinstance(y, int):
            if self.wrap_y:
                if y < 0:
                    raise ValueError('Cannot have negative y with wrapped y')
                y = y % len(self._data)
            rows = [self._data[y]]

        elif isinstance(y, slice):
            if self.wrap_y and y.start < 0 or y.stop < 0:
                raise ValueError('Cannot have negative y offsets with wrapped y')
            y_indices = list(range(y.start or 0, y.stop or len(self._data), y.step or 1))
            rows = []
            for y_i in y_indices:
                if self.wrap_y:
                    y_i = y_i % len(self._data)
                rows.append(self._data[y_i])

        else:
            raise TypeError(f'Unsupported y indexer {type(y).__name__}: {y!r}')

        if isinstance(x, int):
            final = []
            for row in rows:
                if self.wrap_x:
                    if x < 0:
                        raise ValueError('Cannot have negative x with wrapped x')
                    x = x % len(row)
                final.append(row[x])

        elif isinstance(x, slice):
            if self.wrap_x and x.start < 0 or x.stop < 0:
                raise ValueError('Cannot have negative y offsets with wrapped y')
            final = []
            for row in rows:
                x_indices = list(range(x.start or 0, x.stop or len(row), x.step or 1))
                new_row = ''
                for x_i in x_indices:
                    if self.wrap_x:
                        x_i = x_i % len(row)
                    new_row += row[x_i]
                final.append(new_row)

        else:
            raise TypeError(f'Unsupported x indexer {type(x).__name__}: {x!r}')

        if isinstance(x, int) and isinstance(y, int):
            return final[0][0]
        return Map('\n'.join(final),
                   wrap_x=self.wrap_x,
                   wrap_y=self.wrap_y)

    def __str__(self):
        return '\n'.join(self._data)


if __name__ == '__main__':
    with open('y2020/inputs/day3.txt') as f:
        m = Map(f.read())[0:10, 0:5]
    print(m)
    print('-' * 80)
    print(m[0:2, 3])
    print('-' * 80)
    print(m[3, 0:5])
    print('-' * 80)
    print(m[1, 1])
