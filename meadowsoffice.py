# Jacob Meadows
# Computer Programming, 6th Period
# 06 December 2018
"""
[your last name]office.py
Create a program that can read, write, and save text files. When the person saves the file, let them choose name of the file. Of course they should be able to open any file they want as well. I think a menu bar with read (or open), and save will do the trick (but hey, you're the designer).
You have created a basic word processor!

Copyright (C) 2018 Jacob Meadows

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import tkinter as tk
from tkinter import filedialog


class App(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("meadowsoffice")
        self.master.config(width=1280, height=720)
        super().__init__(self.master, width=1280, height=720)
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.widgets = dict()
        self.widgets["top_menu"] = tk.Menu(self.master)
        self.widgets["file_menu"] = tk.Menu(self.widgets["top_menu"], tearoff=0)
        self.widgets["file_menu"].add_command(label="Open...", command=self.open_file_command)
        self.widgets["file_menu"].add_command(label="Save", command=self.save_command)
        self.widgets["file_menu"].add_command(label="Save as...", command=filedialog.asksaveasfile)
        self.widgets["file_menu"].add_separator()
        self.widgets["file_menu"].add_command(label="Exit", command=self.quit)
        self.widgets["top_menu"].add_cascade(label="File", menu=self.widgets["file_menu"])
        self.widgets["help_menu"] = tk.Menu(self.widgets["top_menu"], tearoff=0)
        self.widgets["help_menu"].add_command(label="About", command=self.about_command)
        self.widgets["top_menu"].add_cascade(label="Help", menu=self.widgets["help_menu"])
        self.master.config(menu=self.widgets["top_menu"])
        self.widgets["main_text"] = tk.Text(self)
        self.widgets["main_text"].place(x=0, y=0, relwidth=1, relheight=1)

    def open_file_command(self):
        filedialog.askopenfilename()

    def save_command(self):
        pass

    def about_command(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
