from window import Window
from maze import Maze


def main():
    win = Window(300, 300)
    m = Maze(100, 100, 13, 20, 50, 50, win)
    m.solve()
    win.wait_for_close()


main()
