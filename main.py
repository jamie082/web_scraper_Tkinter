from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

import requests

win = Tk()

win.geometry("700x300")
win.title("Web Scraper Site")

scrape_site = "http://45.77.98.77/site/temp_site/main.html"
frame_site = "http://45.77.98.57/site/temp_site/frame_1.html"

page = requests.get(frame_site)

r = Label(win, text="http://45.77.988.77/site/temp_site/main.html", width=35)

def scraper_function():
    # scrape to inside text box
    print(page.content)

def my_function():  # start Web Scraper code
    messagebox.showinfo("Program Alert", "Web Scraper Started")
    text_box.insert(END, "lol") # print "lol" to text_box
    print(page.content) # scrape to console

click_button = Button(win, text="Scrape", command=my_function)

text_box = Text(
    win,
    height=12,
    width=80
)
r.pack()

click_button.pack()
text_box.pack(expand=True)
text_box.config(state="disabled")
click_button.pack()

win.resizable(False, False)
win.mainloop()