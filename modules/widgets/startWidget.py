import customtkinter as ctk
from modules.themes.themes import default_font

def startCheck(self):
    self.startFrame = ctk.CTkFrame(self.runFrame, border_color='black', border_width=3)
    self.startFrame.grid(row=0, column=0, padx=10, pady=10, sticky='NSEW')
    self.startFrame.columnconfigure(0, weight=1)
    self.start_widget()

def start_widget(self):
    self.runScrcpyButton = ctk.CTkButton(self.startFrame, text='Run', width=20, height=5, command=self.runScrcpy, font=default_font)
    self.runScrcpyButton.grid(row=0, column=1, padx=10, pady=10)

    self.exitScrcpyButton = ctk.CTkButton(self.startFrame, text='Exit', width=20, height=5, command=self.exitScrcpy_func, font=default_font)
    self.exitScrcpyButton.grid(row=0, column=2,padx=10, pady=10)
