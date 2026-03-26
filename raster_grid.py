# The `RasterGrid` represents a structured, rectangular grid in 2d space.
# Each cell of the grid is identified by its column/row index pair:
#
#  ________ ________ ________
# |        |        |        |
# | (0, 1) | (1, 1) | (2, 2) |
# |________|________|________|
# |        |        |        |
# | (0, 0) | (1, 0) | (2, 0) |
# |________|________|________|
#
#
# One can construct a `RasterGrid` by specifying the lower left and upper right
# corners of a domain and the number of cells one wants to use in x- and y-directions.
# Then, `RasterGrid` allows to iterate over all cells and retrieve the center point
# of that cell.
#
# This class can be significantly cleaned up, though. Give it a try, and if you need
# help you may look into the file `raster_grid_hints.py`.
# Make sure to make small changes, verifying that the test still passes, and put
# each small change into a separate commit.
from typing import Tuple
from math import isclose
from dataclasses import dataclass


class Point:
    def __init__(self, x0: float, y0: float) -> None:
        self._coordinate_x = x0
        self._coordinate_y = y0

    def get_coordinate_x(self) -> float:
        return self._coordinate_x

    def get_coordinate_y(self) -> float:
        return self._coordinate_y


class RasterGrid:
    @dataclass
    class Cell:
        _cell_index_x: int
        _cell_index_y: int

    def __init__(self, p0: Point, p1: Point, nx: int, ny: int) -> None:
        self._lower_left_corner_x = p0.get_coordinate_x()
        self._lower_left_corner_y = p0.get_coordinate_y()
        self._upper_right_corner_x = p1.get_coordinate_x()
        self._upper_right_corner_y = p1.get_coordinate_y()
        self._cell_count_x = nx
        self._cell_count_y = ny
        self.number_of_cells = nx * ny
        self.cells = [
            self.Cell(i, j)
            for i in range(self._cell_count_x)
            for j in range(self._cell_count_y)
        ]

    def get_cell_center_coordinates(self, cell: Cell) -> Tuple[float, float]:
        _cell_size_x = (
            self._upper_right_corner_x - self._lower_left_corner_x
        ) / self._cell_count_x
        _cell_size_y = (
            self._upper_right_corner_y - self._lower_left_corner_y
        ) / self._cell_count_y
        return (
            self._lower_left_corner_x
            + (float(cell._cell_index_x) + 0.5) * _cell_size_x,
            self._lower_left_corner_y
            + (float(cell._cell_index_y) + 0.5) * _cell_size_y,
        )


def test_number_of_cells():
    p0 = Point(0.0, 1.0)
    p1 = Point(1.0, 1.0)
    assert RasterGrid(p0, p1, 10, 10).number_of_cells == 100
    assert RasterGrid(p0, p1, 10, 20).number_of_cells == 200
    assert RasterGrid(p0, p1, 20, 10).number_of_cells == 200
    assert RasterGrid(p0, p1, 20, 20).number_of_cells == 400


def test_cell_center():
    p0 = Point(0.0, 0.0)
    p1 = Point(2.0, 2.0)
    grid = RasterGrid(p0, p1, 2, 2)
    expected_centers = [(0.5, 0.5), (1.5, 0.5), (0.5, 1.5), (1.5, 1.5)]

    for cell in grid.cells:
        for center in expected_centers:
            if isclose(
                grid.get_cell_center_coordinates(cell)[0], center[0]
            ) and isclose(grid.get_cell_center_coordinates(cell)[1], center[1]):
                expected_centers.remove(center)

    assert len(expected_centers) == 0


if __name__ == "__main__":
    test_number_of_cells()
    test_cell_center()
    print("All tests passed")
