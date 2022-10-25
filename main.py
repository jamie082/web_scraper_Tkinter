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
    # scraped to inside text box
    page = ''
    for i in range(10):
        page += str(i)
    return page

s = scraper_function()

def print_function():
    print(s)
    text_box.insert(END, scraper_function)

def my_function():  # start Web Scraper code
    messagebox.showinfo("Program Alert", "Web Scraper Started")
    #text_box.insert(END, scraper_function) # print "lol" to text_box
    print(s) # scrape to console

click_button = Button(win, text="Scrape", command=print_function)

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