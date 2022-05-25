from tkinter import *
import random
import pyperclip
import easygui

abcd = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
        'V', 'W', 'X', 'Y', 'Z']

def click_action():
    try:
        password = ''.join(random.choices(abcd, k=int(inputchar.get())))
        passwordtext = Label(app, text=password, font=35, fg='black')
        passwordtext.pack()
    except:
        easygui.msgbox('setup number of characters in password.', title='ERROR', ok_button='OK')
    pyperclip.copy(password)
    copied = Label(app, text="wygenerowane haslo skopiowano do schowka! :)", font=35, fg='black')
    copied.pack()


app = Tk()
app.title('password generator')
app.geometry('640x400')
label = Label(app, text='set number of chars:', font=30, fg='black')
label.pack()
inputchar = Entry(app, bd =5)
inputchar.pack()
button = Button(app, text="click to gen password", width=20, command=click_action)
button.pack()

app.mainloop()
