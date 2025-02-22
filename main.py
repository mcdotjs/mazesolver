from window import Window
from maze import Maze


def main():
    win = Window(300, 300)
    Maze(100, 100, 10, 10, 50, 50, win)
    win.wait_for_close()


main()
