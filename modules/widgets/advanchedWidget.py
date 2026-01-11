import customtkinter as ctk
import tkinter as tk
from modules.themes.themes import default_font

ADVANCHED_WINDOW_NAME = 'Advanched Options'
ADVANCHED_WINDOW_GEOMETRY = '450x450'

window = None
def advanchedCheck(self):
    self.advanchedFrame = ctk.CTkFrame(self.bottomFrame, border_color='black', border_width=3)
    self.advanchedFrame.pack(side=ctk.LEFT, anchor='w', padx=10, pady=10)

    self.advanched_check_value = ctk.BooleanVar()
    self.advanchedCheckBox = ctk.CTkCheckBox(self.advanchedFrame, text='Advanched', variable=self.advanched_check_value, command=self.advanched_widget, font=default_font)
    self.advanchedCheckBox.grid(row=0, column=0, padx=10, pady=10)

def advanched_widget(self):
    global window 
    if not self.advanched_check_value.get():
        try:
            window.destroy()
            # self.advanchedPopUpWindow.destory()
        except Exception as e:
            print(f'Error Destroying AdvanchedPopUpWindow')
        return

    self.advanchedPopUpWindow = ctk.CTkToplevel(self.root)
    self.advanchedPopUpWindow.title(ADVANCHED_WINDOW_NAME)
    self.advanchedPopUpWindow.geometry(ADVANCHED_WINDOW_GEOMETRY)
    window = self.advanchedPopUpWindow


    ctk.CTkButton(self.advanchedPopUpWindow, text='Exit',  command=self.advanchedPopUpWindow.destroy, font=default_font).pack(padx=10, pady=10)
        
    
