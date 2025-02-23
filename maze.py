from point import Point
from cell import Cell
import time
import random


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
        seed=None
    ):
        self._win = win
        self._x1 = x1
        self._y1 = y1
        self._cells = []
        self._cols = num_cols
        self._rows = num_rows
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._valid_cells = []

        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _break_walls_r(self, i, j):
        current = None
        if self._cells[i][j] is not None:
            current = self._cells[i][j]
        else:
            return
        current.visited = True
        go = True
        while go:
            to_visit = []
            go_right = i+1
            go_left = i-1
            go_down = j+1
            go_up = j-1
            if go_right < self._cols:
                to_visit.append([go_right, j, "right"])
            if go_left >= 0:
                to_visit.append([go_left, j, "left"])
            if go_up >= 0:
                to_visit.append([i, go_up, "up"])
            if go_down < self._rows:
                to_visit.append([i, go_down, "down"])

            if len(to_visit) == 0:
                return
            not_visited = []
            for nei in to_visit:
                if self._cells[nei[0]][nei[1]] and not self._cells[nei[0]][nei[1]].visited:
                    not_visited.append(nei)

            if len(not_visited) == 0:
                return

            index = random.randrange(0, len(not_visited), 1)

            next = self._cells[not_visited[index][0]][not_visited[index][1]]
            print(not_visited[index])
            if not_visited[index][2] == "right":
                current.has_right_wall = False
                next.has_left_wall = False
            elif not_visited[index][2] == "left":
                print('left', not_visited[index])
                current.has_left_wall = False
                next.has_right_wall = False
            elif not_visited[index][2] == "up":
                print("up", not_visited[index])
                current.has_top_wall = False
                next.has_bottom_wall = False
            elif not_visited[index][2] == "down":
                current.has_bottom_wall = False
                next.has_top_wall = False

            next.visited = True
            self._draw_cell(i, j)
            self._draw_cell(not_visited[index][0], not_visited[index][1])
            self._break_walls_r(not_visited[index][0], not_visited[index][1])

