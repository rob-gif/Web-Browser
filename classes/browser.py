import tkinter


class Browser:
    def __init__(self, body):
        self.body = body
        self.WIDTH, self.HEIGHT = 800, 600
        self.SCROLL_STEP = 100
        self.display_list = []

    def draw(self):
        window = tkinter.Tk()
        window.title("Browser")
        window.geometry()
        #canvas = tkinter.Canvas(window, width=self.WIDTH, height=self.HEIGHT)
        label = tkinter.Label(
            window,
            text=self.body,
            foreground="black",
            background="white"
        )
        label.pack()

        window.mainloop()
