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

string_ouput.text = []
def two_funct():
    for counter in string_output:
        counter = soup_2.find(class_="paragraph_main")
        return string_output.text

def scraper_function():
    messagebox.showinfo("Alert", "Web Scraper Started")
    text_box.insert(END, string_output.text)

def clear_textbox():
    text_box.delete(1.0, 'end')

click_button = Button(win, text="Scrape", command=scraper_function)
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