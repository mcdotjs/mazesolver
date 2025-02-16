class Line:
    def __init__(self, first, second):
        self.start = first
        self.end = second

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )
