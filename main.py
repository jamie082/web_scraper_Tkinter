from tkinter import *
from tkinter import messagebox

win = Tk()

win.geometry("700x350")
win.title("Python Guide")

scrape_site = "http://45.77.988.77/site/temp_site/main.html"

r = Label(win, text="http://45.77.988.77/site/temp_site/main.html", width=35)
r.pack()

win.resizable(False, False)
win.mainloop()