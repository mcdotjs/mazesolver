from line import Line
from point import Point
from cell import Cell
import time


class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._win = win
        self._x1 = x1
        self._y1 = y1
        self._cells = []
        self._cols = num_cols
        self._rows = num_rows
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._create_cells()

        for col in range(len(self._cells)):
            for cell in range(len(self._cells[col])):
                self._draw_cell(col, cell)

    def _create_cells(self):
        for j in range(self._rows):
            self._cells.append([])
            for i in range(self._cols):
                c = j*self._cell_size_x
                t = i*self._cell_size_y
                cell = Cell(Point(self._x1+c, self._y1+t),
                            Point(self._cell_size_x+c+self._x1, self._cell_size_y+t+self._y1), win=self._win)
                self._cells[j].append(cell)

    def _draw_cell(self, x, y):
        self._cells[x][y].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
