import tkinter as tk
from tkinter import ttk
from tkinter.constants import HORIZONTAL
from tkinter.messagebox import showinfo
from glob import glob
from main import generate_QR_Code
from os import path, remove
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("570x670")
        self.title('QR Code Generator')
        # self.resizable(0, 0) 
        
        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)

        self.create_widgets()
    
    def qrAction(self, inData):
        #pass the data to main.py function to get QR code 
        generate_QR_Code(inData=inData)
        #getting the latest png file 
        all_file = glob('QR_Code*.png')
        latestQRCode = max(all_file, key=path.getctime)
        load = Image.open(latestQRCode)
        render = ImageTk.PhotoImage(load)
        img = ttk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=100)

    def create_widgets(self):
        # username
        username_label = ttk.Label(self, text="Enter the data to encode:")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        username_entry = ttk.Entry(self)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5, ipadx=70)

        # Generate button 
        login_button = ttk.Button(self, text="      Generate QR Code      ", command=lambda: self.qrAction(username_entry.get()))
        login_button.grid(column=1, row=3, sticky=tk.N, padx=5, pady=5)
        
        # separator 
        separator = ttk.Separator(self, orient=HORIZONTAL)
        separator.grid(column=1, row=5, padx=5, pady=5)
        
    def on_closing(self):
        #Logic to remove all the QR file generated 
        for f in glob("QR_Code_*.png"):
            remove(f)
        # destroy the app, else the window won't close 
        app.destroy()
        


if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()