from window import Window
from maze import Maze


def main():
    win = Window(300, 300)
    Maze(100, 100, 13, 23, 50, 50, win, 8)
    win.wait_for_close()


main()
