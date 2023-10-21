import tkinter.font
from classes.text import Text

class Layout:
    def __init__(self, tokens):
        self.WIDTH, self.HEIGHT = 600, 800
        self.VSTEP,self.HSTEP = 18, 13
        self.cursor_x,self.cursor_y = self.VSTEP, self.HSTEP
        self.style = "roman"
        self.weight = "normal"
        self.size = 16
        self.display_list = []
        for tok in tokens:
            self.tokens(tok)

    def tokens(self, tok):
        if isinstance(tok, Text):
            for word in tok.text.split():
                font = tkinter.font.Font(
                      size=16,
                      weight=self.weight,
                      slant=self.style
                    )
                if self.cursor_x > self.WIDTH - self.HSTEP:
                    self.cursor_y += font.metrics("linespace") * 1.25
                    self.cursor_x = self.HSTEP
                    self.display_list.append((self.cursor_x, self.cursor_y, word, font))
                    self.cursor_x += font.measure(" ")

        elif tok.tag == "i":
            style = "italic"
        elif tok.tag == "/i":
            style = "roman"
        elif tok.tag == "b":
            weight = "bold"
        elif tok.tag == "/b":
            weight = "normal"

            self.scrolldown()
        return self.display_list

    def word(self):
        pass