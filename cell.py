from line import Line
from point import Point
# cell has four walls
# our class should know which walls it has, where it exists (x, y coords)
# has to have access to the window to draw itself


class Cell():
    def __init__(self, topleft, bottomright, hasLeft=True, hasRight=True, hasTop=True, hasBottom=True, win=None):
        self._x1 = topleft.x
        self._y1 = topleft.y
        self._x2 = bottomright.x
        self._y2 = bottomright.y
        self._win = win
        self.has_left_wall = hasLeft
        self.has_right_wall = hasRight
        self.has_top_wall = hasTop
        self.has_bottom_wall = hasBottom
        self.middlePoint = Point(
            (self._x1 + self._x2)/2, (self._y1 + self._y2)/2)
        self.visited = False

    def draw(self):
        if self._win is None:
            return
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "red")
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "black")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "red")
        else:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "black")
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "red")
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "red")
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black")

    def draw_move(self, another, undo=False):
        color = "white"
        if undo:
            color = "gray"
        self._win.draw_line(Line(self.middlePoint, another.middlePoint), color)
