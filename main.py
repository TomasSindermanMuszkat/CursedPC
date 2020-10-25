import tkinter as tk
from tkinter import messagebox as msgbox
from screeninfo import get_monitors

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

    def create_widgets(self, text, close_text):
        self.label = tk.Label(self, text=text)
        self.label.pack(side="top")
        self.quit = tk.Button(self, text=close_text,command=self.master.destroy)
        self.quit.pack(side="bottom")
        
screen = get_monitors()
width, height = screen[0].width, screen[0].height
labels = ["test1", "test2", "test3"]
exits = ["exit1", "exit2", "exit3"]
sizes = ["100x100", "200x200", "300x300"]
for i in range(len(labels)):
    root = tk.Tk()
    position = f"+{width//2-int(sizes[i].split('x')[0])//2}+{height//2-int(sizes[i].split('x')[1])//2}"
    root.geometry(sizes[i]+position)
    app = Application(master=root)
    app.create_widgets(labels[i], exits[i])
    app.mainloop()
