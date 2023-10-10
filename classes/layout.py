import tkinter.font
from .tag import Tag

class Layout:
    def __init__(self,text):
        self.text = text
        self.display_list = []
        self.WIDTH, self.HEIGHT = 800, 600
        self.HSTEP, self.VSTEP = 13, 18
        self.cursor_x, self.cursor_y = self.HSTEP, self.VSTEP
        self.fonts = tkinter.font.Font(
           family="Monospace",
           size=16,
           weight=self.weight,
           slant=self.style
        )
        self.weight = "normal"
        self.style = "roman"

    def boldness(self, tag):
            tag = Tag()
            if tag == "i":
                    self.style = "italic"
            elif tag == "/i":
                    self.style = "roman"
            elif tag == "b":
                    self.weight = "bold"
            elif tag == "/b":
                    self.weight = "normal"

    def layout(self):
        # logic for calculating where to display ;0
        w = self.fonts.measure(self.text)
        if self.cursor_x + w > self.WIDTH - self.HSTEP:
            self.cursor_y += self.fonts.metrics("linespace") * 1.25
            self.cursor_x = self.HSTEP

        for c in self.text:
            self.display_list.append((self.cursor_x,self.cursor_y,c,font))
            self.cursor_x += self.HSTEP

        return self.display_list


