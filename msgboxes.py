import tkinter
from tkinter import messagebox as msgbox
from random import shuffle
import sys

def sysString(fmt, win, unix):
    if (sys.platform == "win32"):
        args = win
    else:
        args = unix
    return fmt.format(*args)

def displayErrors():
    titles = ["Error", "Err0r", "3rrOr", "=}|9|9y|9", "Ошибка", "错误", "Internet Explorer", "Outlook Express", "Help me", "Truth"]
    messages = ["Operation was a success.", "Thanks for your donation!", "Facebook account deleted!", sysString("Sending {} to all contacts.", ["My Documents\Do not open\p0rn"], ["~/donotopen/p0rn"]), "Malware installed!", "Keyboard not found", "ID10T", "I hear screaming", "If you had killed yourself your family would actually be relieved.", "I can't believe it, you actually have a negative IQ!"]
    shuffle(titles)
    shuffle(messages)
    for title, message in zip(titles, messages):
        msgbox.showerror(title, message)
    
root = tkinter.Tk()
root.withdraw()
displayErrors()
