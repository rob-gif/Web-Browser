import tkinter.font
from classes.text import Text
from classes.url import URL

# caching fonts to speed up the browser
FONTS = {}


class Layout:
    def __init__(self, tokens):
        self.WIDTH, self.HEIGHT = 600, 800
        self.VSTEP, self.HSTEP = 18, 13
        self.cursor_x, self.cursor_y = self.VSTEP, self.HSTEP
        self.style = "roman"
        self.weight = "normal"
        self.size = 16
        self.line = []

        for tok in tokens:
            self.tokens(tok)

        self.display_list = []

    def tokens(self, tok):
        if isinstance(tok, Text):
            for word in tok.text.split():
                font = self.get_font(
                    self.size,
                    self.weight,
                    self.style
                )
                w = font.measure(word)

                if self.cursor_x > self.WIDTH - self.HSTEP:
                    self.cursor_y += font.metrics("linespace") * 1.25
                    self.cursor_x = self.HSTEP
                    self.display_list.append((self.cursor_x, self.cursor_y, word, font))
                    self.line.append((self.cursor_x, word, font))
                    self.cursor_x += w + font.measure(" ")
                    self.flush()

        elif tok.tag == "i":
            self.style = "italic"
        elif tok.tag == "/i":
            self.style = "roman"
        elif tok.tag == "b":
            self.weight = "bold"
        elif tok.tag == "/b":
            self.weight = "normal"
        elif tok.tag == "small":
            self.size -= 2
        elif tok.tag == "/small":
            self.size += 2
        elif tok.tag == "big":
            self.size += 4
        elif tok.tag == "/big":
            self.size -= 4
        elif tok.tag == "br":
            self.flush()
        elif tok.tag == "/p":
            self.flush()
            self.cursor_y += self.VSTEP

        return self.display_list

    def flush(self):
        if not self.line: return
        metrics = [font.metrics() for x, word, font in self.line]
        max_ascent = max([metrics["ascent"] for metrics in metrics])
        baseline = self.cursor_y + 1.25 * max_ascent

        max_descent = max([metrics("descent") for metrics in metrics])
        self.cursor_y = baseline + 1.25 * max_descent

        for x, y, word in self.line:
            y = baseline - self.font.metrics("ascent")
            self.display_list.append((x, y, word))
            self.cursor_x = self.HSTEP
            self.line = []

    def get_font(self, size, weight, slant):
        key = (size, weight, slant)
        if key not in FONTS:
            font = tkinter.font.Font(
                size=size, weight=weight, slant=slant
            )
            label = tkinter.Label(font=font)
            FONTS[key] = (font, label)

        return FONTS[key][0]

