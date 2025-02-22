from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze


def main():
    win = Window(300, 300)
    Maze(win=win)
    # size = 33
    # cols = 3
    # rows = 10
    # for j in range(cols):
    #     for i in range(rows):
    #         print(i)
    #         c = j*size
    #         t = i*size
    #         cell = Cell(win,  Point(0+c, 0+t),  Point(size+c, size+t))
    #         cell.draw()

    win.wait_for_close()
 #   line = Line(p1, p2)
  #  win.draw_line(line, "white")


main()
