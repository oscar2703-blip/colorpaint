from tkinter import*
from tkinter import colorchooser
from tkinter.colorchooser import askcolor

class Paint(object):
    DEFAULT_COLOR = "black"
    def __init__(self):
        self.root = Tk()
        self.root.config(bg="orange")
        self.pen_button = Button(self.root, text="pen",
                             bg="green", bd=5, fg="white", command=self.use_pen)

        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text="Brush",
        bg = "green", bd=5, fg="white", command=self.use_brush)

        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text="Colour",
        bg = "green", bd=5, fg="white", command=self.choose_color)

        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.root, text="Eraser",
        bg = "green", bd=5, fg="white", command=self.user_eraser)
    
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.root, from_ = 1, to=20, bg="green", bd=5, fg="white", command=None)
        self.choose_size_button.grid(row=0, column=4)
    
        self.c = Canvas(self.root, bg="white", width=600, height=600)
        self.c.grid(row=1,column=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()

        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind("<B1-Motion", self.paint)

        self.c.bind("<Buttonrelease-1>".self.reset)

    def use_pen(self):
        self.active_button(self.pen_button)

    def use_brush(self):
        self.active_button(self.brush_button)

    def choose_color(self):
        self.eraser_button=False
        self.color=askcolor(color=self.color)[1]
    
    def user_eraser(self):
        self.active_button(self.eraser_button,eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.activate_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.activate_button = some_button
        self.eraser_on = eraser_mode
    
    def paint(self, event):
        elf.line_width = self.choose_size_button.get()
        paint_color = "white" if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y,
            width = self.line_width,
            capstyle = ROUND,
            smooth = True,
            splinesteps = 35
            )
            self.old_x = event.x
            self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

if __name__ == "__main__":
    Paint()
