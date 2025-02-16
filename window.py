from tkinter import Tk, BOTH, Canvas, Label

class Window:
    def __init__(self, height=500, width=400):
        self.__root = Tk()
        self.__running = False

        self.__root.title("Maze Slover")
        label = Label(self.__root, text="Tkinter is working!")
        self.__canvas = Canvas(self.__root, bg="black",
                               width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        label.pack()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False
