# Here is where i add the window functionality to my cool web browser
# here goes nothing

import tkinter

#from .url import URL


class Browser:
    def __init__(self):
        self.display_list = []
        self.HSTEP, self.VSTEP = 13, 18
        self.cursor_x, self.cursor_y = self.HSTEP, self.VSTEP
        WIDTH, HEIGHT = 800, 600
        self.window = tkinter.Tk()  # initialize a window
        self.canvas = tkinter.Canvas(
            self.window,
            width=WIDTH,
            height=HEIGHT
        )
        self.scroll = 0
        self.window.bind("<Down>", self.scrolldown)
        self.SCROLL_STEP = 100

    def layout(self,text):
        # logic for calculating where to display ;0
        for c in text:
            self.display_list.append((self.cursor_x,self.cursor_y,c))
            self.cursor_x += self.HSTEP
        return self.display_list

    def start(self):
        #draw the text on the window
        for x, y, c in self.display_list:
              self.canvas.create_text(x, y - self.scroll, text=c)
              self.canvas.create_text(400, 300, text="it works")
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

