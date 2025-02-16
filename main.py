from window import Window
from line import Line
from point import Point


def main():
    win = Window(800, 600)
    p1 = Point(0, 0)
    p2 = Point(839, 888)
    line = Line(p1, p2)
    win.draw_line(line, "white")
    win.wait_for_close()


main()
