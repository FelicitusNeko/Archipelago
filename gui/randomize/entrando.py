from tkinter import ttk, IntVar, StringVar, Checkbutton, Frame, Label, OptionMenu, E, W, LEFT, RIGHT
import gui.widgets as widgets
import json
import os

def entrando_page(parent):
    # Entrance Randomizer
    self = ttk.Frame(parent)

    # Entrance Randomizer options
    self.widgets = {}

    with open(os.path.join("resources","app","gui","randomize","entrando","widgets.json")) as myWidgets:
        myDict = json.load(myWidgets)
        dictWidgets = widgets.make_widgets_from_dict(self, myDict, self)
        for key in dictWidgets:
            self.widgets[key] = dictWidgets[key]
            self.widgets[key].pack(anchor=W)

    return self
