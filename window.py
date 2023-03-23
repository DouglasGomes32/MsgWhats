import time
import urllib
import webbrowser
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def btn_clicked():
    cellfone = entry0.get()
    msg = entry1.get("1.0", END)
    print(cellfone)
    print(msg)

def btn_clicked():
    cellfone = entry0.get()
    msg = entry1.get("1.0", END)
    browser = webdriver.Chrome()
    browser.get('https://web.whatsapp.com')
    time.sleep(30)
    text = urllib.parse.quote(msg)
    browser.get(f'https://web.whatsapp.com/send?phone=+{cellfone}&text={text}')
    time.sleep(30) 
    browser.find_element("xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p').send_keys(Keys.ENTER)

window = Tk()

window.geometry("701x497")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 497,
    width = 701,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    371.0, 248.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    533.0, 229.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 409, y = 210,
    width = 248,
    height = 37)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    533.0, 370.5,
    image = entry1_img)

entry1 = Text(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 409, y = 307,
    width = 248,
    height = 125)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 451, y = 446,
    width = 150,
    height = 35)

window.resizable(False, False)
window.mainloop()
