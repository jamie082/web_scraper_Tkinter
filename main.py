from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

import requests

win = Tk()

win.geometry("700x300")
win.title("Jamie's Web Scraper")

scrape_site = "http://45.77.98.77/site/temp_site/main.html"
frame_site = "http://45.77.98.57/site/temp_site/frame_1.html"

page_2 = requests.get("http://45.77.98.57/site/temp_site/body_page.html")
soup_2 = BeautifulSoup(page_2.content, "html.parser")

r = Label(win, text="http://45.77.988.77/site/temp_site/main.html", width=35)
    
page = requests.get(frame_site)

my_list = ['Linux', 'Windows', 'Python', 'Web Links', 'Linux', 'portfolio']


def function_1(): # print to text_box
    #for i in my_list:
        #div_specify = soup.find_all(class_=i) # Linux, Windows, Python, Web Links, Linux, portfolio

# use lists in next function
    for counter in range(1): 
        paragraph = soup_2.find(class_="paragraph_main")
     
        return paragraph


def two_funct():
    string_output = []
    for counter in string_output:
        string_output = soup_2.find(class_="paragraph_main")

    messagebox.showinfo("Alert", "Web Scraper Started")
    text_box.insert(END, string_output)

def scraper_function():
    messagebox.showinfo("Alert", "Web Sraper Started")
    text_box.insert(END, string_output)

def clear_textbox():
    text_box.delete(1.0, 'end')

click_button = Button(win, text="Scrape", command=two_funct)
clear_button = Button(win, text="Clear", command=clear_textbox)

text_box = Text(
    win,
    height=12,
    width=80
)
r.pack()

click_button.pack()
clear_button.pack()
text_box.pack()

win.resizable(False, False)

win.mainloop()