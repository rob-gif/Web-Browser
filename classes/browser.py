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
        self.display_list = []
        self.fonts = tkinter.font.Font(
            family="Jetbrains mono",
            size=16,
            weight="bold",
            slant="italic"
        )

    # BASIC LAYOUT
    def layout(self, text):
        w = self.fonts.measure(text)

        for c in text:
            if self.cursor_x > self.WIDTH - self.HSTEP:
                self.cursor_y += self.fonts.metrics("linespace") * 1.25
                self.cursor_x = self.HSTEP
            self.display_list.append((self.cursor_x, self.cursor_y, c))
            self.cursor_x += w + self.fonts.measure(" ")

        self.scrolldown()
        return self.display_list

    def draw(self):
        self.canvas.delete("all")
        for x, y, z in self.display_list:
            if y > self.scroll + self.HEIGHT: continue
            if y + self.VSTEP < self.scroll: continue
            self.canvas.create_text(x, y - self.scroll, text=z, font="Arial")
            self.window.resizable = True
            self.window.mainloop()

    def scrolldown(self):
        self.scroll += self.SCROLL_STEP
        self.draw()
