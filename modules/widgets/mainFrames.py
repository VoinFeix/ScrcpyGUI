import customtkinter as ctk
from modules.themes.themes import heading_font


def mainFrames(self):
    # self.root.rowconfigure(0, weight=1)
    # self.root.columnconfigure(0, weight=1)

    self.headingFrame = ctk.CTkFrame(self.root,)
    self.headingFrame.grid(row=0, column=0, sticky='NSEW', padx=10, pady=10)

    self.headingFrame.rowconfigure(0, weight=1)
    self.topHeading = ctk.CTkLabel(self.headingFrame, text='ScrcpyGUI', font=heading_font)
    self.topHeading.pack(anchor='center')


    self.firstFrame = ctk.CTkFrame(self.root,)
    self.firstFrame.grid(row=1, column=0, sticky='NSEW', padx=10, pady=8)
    
    self.topFrame = ctk.CTkFrame(self.root,)
    self.topFrame.grid(row=2, column=0, sticky='NSEW', padx=10, pady=8)

    self.middleFrame = ctk.CTkFrame(self.root,)
    self.middleFrame.grid(row=3, column=0, sticky='NSEW', padx=10, pady=8)

    self.lastFrame = ctk.CTkFrame(self.root,)
    self.lastFrame.grid(row=4, column=0, sticky='NSEW', padx=10, pady=8)

    self.bottomFrame = ctk.CTkFrame(self.root,)
    self.bottomFrame.grid(row=5, column=0, sticky='NSEW', padx=10, pady=8)

    self.runFrame = ctk.CTkFrame(self.root,)
    self.runFrame.grid(row=6, column=0, sticky='NSEW', padx=10, pady=8)
