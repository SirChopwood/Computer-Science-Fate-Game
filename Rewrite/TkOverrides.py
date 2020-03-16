import tkinter


def test_event(event):
    print(f"Placeholder - {event}")


class Canvas(tkinter.Canvas):
    def __init__(self,  *args, **kw):
        super().__init__(*args, **kw)

    def set_grid(self, column, row, columnspan=0, rowspan=0, **kw):
        super().grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, **kw)

    def create_text(self, x, y, text, anchor="nw", colour="#ffffff", font="Imperfecto Regular", size=20, **kwargs):
        return super().create_text(x, y, text=str(text), anchor=anchor, fill=colour, font=(font, size), **kwargs)

    def create_button(self, x=0, y=0, text="Placeholder", sizex=100, sizey=30, function=test_event):
        CreateButton(self, x, y, text, sizex, sizey, function)


class CreateButton:
    def __init__(self, parent, x, y, text, sizex, sizey, function):
        self.background = parent.create_rectangle(x, y, x+sizex, int(y+sizey), fill="#555555")
        self.text = parent.create_text(int(x+(sizex/2)), int(y+(sizey/2)), text=text, anchor="c", colour="#ffffff")
        parent.tag_bind(self.background, "<Button-1>", function)
        parent.tag_bind(self.text, "<Button-1>", function)
