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
        self._break_entrance_and_exit()

    def _create_cells(self):
        for j in range(self._cols):
            self._cells.append([])
            for i in range(self._rows):
                c = j*self._cell_size_x
                t = i*self._cell_size_y
                cell = Cell(Point(self._x1+c, self._y1+t),
                            Point(self._cell_size_x+c+self._x1, self._cell_size_y+t+self._y1), win=self._win)
                self._cells[j].append(cell)
        for col in range(len(self._cells)):
            for cell in range(len(self._cells[col])):
                self._draw_cell(col, cell)

    def _draw_cell(self, x, y):
        if len(self._cells) != 0:
            self._cells[x][y].draw()
            self._animate()

    def _animate(self):
        if self._win is not None:
            self._win.redraw()
            time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._cols-1][self._rows-1
                                  ].has_bottom_wall = False
        self._draw_cell(self._cols-1, self._rows-1)
