import tkinter
import tkinter.font


class Browser:
    def __init__(self, body):
        self.body = body
        self.scroll = 0
        self.WIDTH, self.HEIGHT = 800, 600
        self.HSTEP, self.VSTEP = 13, 18
        self.cursor_x, self.cursor_y = self.VSTEP, self.HSTEP
        self.window = tkinter.Tk()
        self.window.title("Browser")
        self.canvas = tkinter.Canvas(
            self.window,
            width=self.WIDTH,
            height=self.HEIGHT
        )
        self.canvas.pack()
        self.window.bind("<Down>", self.scrolldown)
        self.window.bind("<MouseWheel>", self.scrolldown)
        self.SCROLL_STEP = 100



    def draw(self, display_list):
        self.canvas.delete("all")
        for x, y, z in display_list:
            if y > self.scroll + self.HEIGHT: continue
            if y + self.VSTEP < self.scroll: continue
            self.canvas.create_text(x, y - self.scroll, text=z, font="Arial")
            self.window.resizable = True
            self.window.mainloop()

    def scrolldown(self):
        self.scroll += self.SCROLL_STEP
        self.draw()
