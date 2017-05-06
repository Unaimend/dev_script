from Tkinter import *
import tkFileDialog
# Uses PEP8 style guide


class Gui(object):
    def __init__(self, root):
        self.root = root
        self.var1 = BooleanVar()
        self.var2 = BooleanVar()
        self.dir_opt = {}
        self.path = 0

        self.download_sfml_box = Checkbutton(
            root, text="SFML", variable=self.var1).grid(row=0)
        self.download_lua_box = Checkbutton(
            root, text="Lua", variable=self.var2).grid(row=0, column=1)
        self.go_button = Button(root, text="GO").grid(row=2)
        self.exit_button = Button(
            root, text="Exit", command=root.quit).grid(row=2, column=1)
        self.where_button = Button(
            root, text="Where?", command=self.ask_dir).grid(row=2, column=2)
    # Checkbutton(root, text="3", variable=var1).grid(rod=3, sticky=d)

    def ask_dir(self):
        self.dir_opt['title'] = 'Please select directory'
        self.path = tkFileDialog.askdirectory(**self.dir_opt)
        if not self.path:
            return

    def run(self):
        self.root.mainloop()


GUI = Gui(Tk())
GUI.run()
print GUI.path
