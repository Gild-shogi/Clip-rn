import TranslateStripe as strip
import tkinter
import tkinter.ttk as ttk
import time
import datetime as dt
import pyperclip
import os

class Application(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.lang = {"日本語":"ja", "英語":"en", "イタリア語":"it", "中国語":"zh", "ドイツ語":"de", "オランダ語":"nl"}
        self.langlist = ["日本語", "英語", "イタリア語", "中国語", "ドイツ語", "オランダ語"]
        self.combo1 = ttk.Combobox(values=self.langlist, textvariable=tkinter.StringVar())

        self.label1 = tkinter.Label(text="source")
        self.label1.place(x=5, y=0)
        self.label2 = tkinter.Label(text="target")
        self.label2.place(x=5, y=50)
        self.combo2 = ttk.Combobox(values=self.langlist, textvariable=tkinter.StringVar())
        self.combo1.current(1)
        self.combo2.current(0)
        self.combo1.place(x=10, y=22, width=92)
        self.combo2.place(x=10, y=72, width=92)
        self.flag1 = 0
        self.pack()
        master.title(u"strip clip")
        master.geometry("230x100")
        #self.label1 = tkinter.Label(text="")
        #self.label1.place(x=10, y=10)
        self.btn1 = tkinter.Button(master, text='start', command=self.btn_click1, bg="orange")
        self.btn1.place(x=110, y=22, width=100, height=70)
        master.after(2000, self.update)

    def update(self):
        if self.flag1 == 1: 
            datetime1 = dt.datetime.now().strftime( "%Y%m%d_%H%M%S" ) 
            strip.shapeText(self.lang[self.combo1.get()], self.lang[self.combo2.get()])
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