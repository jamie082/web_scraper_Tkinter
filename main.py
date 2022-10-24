from tkinter import *
from tkinter import messagebox

win = Tk()

win.geometry("700x150")
win.title("Web Scraper Site")

scrape_site = "http://45.77.98.77/site/temp_site/main.html"
frame_site = "http://45.77.98.57/site/temp_site/frame_1.html"

r = Label(win, text="http://45.77.988.77/site/temp_site/main.html", width=35)
r.pack()

win.resizable(False, False)
win.mainloop()