import TranslateStripe as strip
import tkinter
import time
import datetime as dt
import pyperclip
import os

class Application(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.flag1 = 0
        self.pack()
        master.title(u"strip clip")
        master.geometry("300x40")
        self.label1 = tkinter.Label(text="")
        self.label1.place(x=10, y=10)
        self.btn1 = tkinter.Button(master, text='start', command=self.btn_click1, bg="orange")
        self.btn1.place(x=180, y=10, width=100)
        master.after(2000, self.update)

    def update(self):
        if self.flag1 == 1: 
            datetime1 = dt.datetime.now().strftime( "%Y%m%d_%H%M%S" ) 
            strip.shapeText()
        self.master.after(2000, self.update) 
    def btn_click1(self):
        self.label1.config(text="")
        if self.flag1 == 0:
            self.flag1 = 1 
            self.btn1.config(bg = 'red', text = 'stop' ) 
        else: 
            self.flag1 = 0 
            self.btn1.config(bg = 'orange', text = 'start' ) 


def main(): 
    root = tkinter.Tk()
    app = Application( master=root ) 
    app.mainloop()

if __name__ == "__main__": 
    main() 