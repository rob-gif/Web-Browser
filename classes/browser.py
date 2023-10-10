# Here is where i add the window functionality to my cool web browser
# here goes nothing
#all i want to do is the GUI -- here

import tkinter

from .url import URL
from .layout import Layout


class Browser:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 800, 600
        self.window = tkinter.Tk()  # initialize a window
        self.canvas = tkinter.Canvas(
            self.window,
            width=self.WIDTH,
            height=self.HEIGHT
        )
        self.scroll = 0
        self.window.bind("<Down>", self.scrolldown)
        self.SCROLL_STEP = 100
        self.display_list = []


    def start(self):
        #draw the text on the window
        for x, y, c in self.display_list:
              self.canvas.create_text(x, y - self.scroll, text=c, font=self.fonts)
              self.canvas.create_text(400, 300, text="it works", font=self.fonts)
              self.canvas.pack()
              self.window.mainloop()


    #adding the scrolldown event handler that will be called when
    #the user scrollsdown
    def scrolldown(self, e):
        self.scroll += self.SCROLL_STEP
        self.draw()

     #scrolling draws the text once more so we delete the old text
    def draw(self):
        self.canvas.delete("all")

