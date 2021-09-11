from gtts import gTTS
import tkinter as tk
from tkinter import ttk
from tkinter import *
import os
import time


class MPGFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack()

        self.GrossObject = tk.StringVar()
        self.OhGross = tk.StringVar()
        
        ttk.Label(self, text="Gross Object:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.GrossObject).grid(column=1, row=0)

        ttk.Label(self, text="GrossInator: ").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.OhGross, state="readonly").grid(column=1, row=1)

    
        ttk.Button(self, text="GrossIfy",
                command=self.GrossIfy).grid(column=1, row=2, sticky=tk.E)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def GrossIfy(self):
        GrossObject = self.GrossObject.get()
        OhGross = self.OhGross.get()

        print(GrossObject)
        if GrossObject.lower() == "anime" or GrossObject.lower() == "default":
            os.system('defualt.mp3')
        OG = "Oh gross, " + GrossObject
        if GrossObject.lower() != "anime" and GrossObject.lower() != "default":
            self.PlayOhGrossFile()
            self.SaveGrossObject(GrossObject)
        print("Bye")
        print("---------------------------------------------------------------------------")

        self.OhGross.set(OG)

    def PlayOhGrossFile(self):
        print("will start playing")
        os.system('ohgross.mp3')
        time.sleep(1)

    def SaveGrossObject(self, grossobject):
        langauge = "en"
        print("en")
        output = gTTS(text=grossobject, lang=langauge, slow=False)
        print("output")
        output.save("grossobject.mp3")
        print("save")
        os.system('start grossobject.mp3')
        print("started")   

if __name__ == "__main__":

    root = tk.Tk()
    root.title("The GrossInator!")
    root.iconbitmap('Gross.ico')
    MPGFrame(root)
    root.mainloop()

