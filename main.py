from tkinter import *
from tkinter import messagebox

win = Tk()

win.geometry("700x650")
win.title("Web Scraper Site")

scrape_site = "http://45.77.98.77/site/temp_site/main.html"
frame_site = "http://45.77.98.57/site/temp_site/frame_1.html"

r = Label(win, text="http://45.77.988.77/site/temp_site/main.html", width=35)

click_button = Button(win, text="Scrape")


text_box = Text(
    win,
    height=12,
    width=80
)
r.pack()

click_button.pack()

message=''
text_box.pack(expand=True)
text_box.insert('end', message)
text_box.config(state='disabled')



win.resizable(False, False)
win.mainloop()