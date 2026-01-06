import customtkinter as ctk
from modules.themes.themes import default_font

def cameraCheck(self):
    self.cameraFrame = ctk.CTkFrame(self.bottomFrame, border_color='black', border_width=3)
    self.cameraFrame.pack(side=ctk.LEFT, anchor='w', padx=10, pady=10)

    self.camera_check_value = ctk.BooleanVar()
    self.cameraCheckBox = ctk.CTkCheckBox(self.cameraFrame, text='Camera', command=self.camera_widget, variable=self.camera_check_value, font=default_font)
    self.cameraCheckBox.grid(row=0, column=0, padx=10, pady=10)

def camera_widget(self):
    pass