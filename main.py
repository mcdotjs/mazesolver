from window import Window
from line import Line
from point import Point
from cell import Cell


def main():
    win = Window(800, 600)
    p1 = Point(999, 100)
    p2 = Point(199, 999)
    cell = Cell(win, p1, p2)
    p11 = Point(300, 10)
    p22 = Point(10, 300)
    cell1 = Cell(win, p11, p22)

    cell.draw()
    cell1.draw()
    cell.draw_move(cell1)
    line = Line(p1, p2)
    win.draw_line(line, "white")
    win.wait_for_close()


main()
