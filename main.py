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

def scraper_function():
    # scraped to inside text box
    page = requests.get(frame_site)
    return "page.text"

def my_function():  # start Web Scraper code
    messagebox.showinfo("Program Alert", "Web Scraper Started")
    text_box.insert(END, scraper_function) # print "lol" to text_box
    print(page.content) # scrape to console

click_button = Button(win, text="Scrape", command=my_function)

text_box = Text(
    win,
    height=12,
    width=80
)
r.pack()


# https://www.geeksforgeeks.org/python-tkinter-text-widget/

click_button.pack()
text_box.pack()

win.resizable(False, False)

win.mainloop()