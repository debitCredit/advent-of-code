# TODO: Refactor, introduce tests, set up CI/CD

import re

Point = tuple[int, int]  # (x, y) points on a grid

neighbors4 = ((0, 1), (1, 0), (0, -1), (-1, 0))
neighbors8 = ((1, 1), (1, -1), (-1, 1), (-1, -1)) + neighbors4


class Grid(dict):
    """A 2D grid, implemented as a mapping of {(x, y): cell_contents}."""

    def __init__(self, mapping=(), rows=(), neighbors=neighbors4):
        """Initialize with, e.g., either `mapping={(0, 0): 1, (1, 0): 2, ...}`,
        or `rows=[(1, 2, 3), (4, 5, 6)].
        `neighbors` is a collection of (dx, dy) deltas to neighboring points.`"""
        super().__init__()
        self.update(mapping if mapping else
                    {(x, y): val
                     for y, row in enumerate(rows)
                     for x, val in enumerate(row)})
        self.width = max(x for x, y in self) + 1
        self.height = max(y for x, y in self) + 1
        self.deltas = neighbors

    def copy(self):
        return Grid(self, neighbors=self.deltas)

    def neighbors(self, point) -> list[Point]:
        """Points on the grid that neighbor `point`."""
        x, y = point
        return [(x + dx, y + dy) for (dx, dy) in self.deltas
                if (x + dx, y + dy) in self]

    def to_rows(self) -> list[list[object]]:
        """The contents of the grid in a rectangular list of lists."""
        return [[self[x, y] for x in range(self.width)]
                for y in range(self.height)]


def mapt(fn, *args) -> tuple:
    """map(fn, *args) and return the result as a tuple."""
    return tuple(map(fn, *args))


def digits(text: str) -> tuple[int]:
    """A tuple of all the digits in text (as ints 0–9), ignoring non-digit characters."""
    return mapt(int, re.findall(r'\d', text))
