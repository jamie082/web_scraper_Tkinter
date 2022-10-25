from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

import requests

win = Tk()

win.geometry("700x300")
win.title("Web Scraper Site")

scrape_site = "http://45.77.98.77/site/temp_site/main.html"
frame_site = "http://45.77.98.57/site/temp_site/frame_1.html"

r = Label(win, text="http://45.77.988.77/site/temp_site/main.html", width=35)

page = requests.get(frame_site)
def scraper_function():
    messagebox.showinfo("Program Alert", "Web Scraper Started")
    text_box.insert(END, "lol...")

    print (page.text)

click_button = Button(win, text="Scrape", command=scraper_function)

text_box = Text(
    win,
    height=12,
    width=80
)
r.pack()

click_button.pack()
text_box.pack()

win.resizable(False, False)

win.mainloop()