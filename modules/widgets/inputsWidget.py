import customtkinter as ctk
from modules.themes.themes import default_font

def inputsCheck(self):
    self.inputsFrame = ctk.CTkFrame(self.topFrame, border_color='black', border_width=3)
    self.inputsFrame.pack(side=ctk.LEFT, anchor='nw', padx=10, pady=10)
    
    self.input_check_value = ctk.BooleanVar()
    self.inputCheckBox = ctk.CTkCheckBox(self.inputsFrame, text='Inputs', command=self.input_widget, variable=self.input_check_value, font=default_font)
    self.inputCheckBox.grid(row=0, column=0, padx=10, pady=10)
    
def input_widget(self):
    if not self.input_check_value.get():
        # self.inputsLabel.destroy()

        self.otgCheckBox.destroy()

        self.keyboardCheckBox.destroy()
        self.keyboardMode_menu.destroy()
        
        self.mouseCheckBox.destroy()
        self.mouseMode_menu.destroy()

        self.gamepadCheckBox.destroy()
        self.gamepadMode_menu.destroy()

        self.noControlCheckBox.destroy()

        self.inputCheckBox.configure(text='Inputs')
        return 

    # self.inputsLabel = ctk.CTkLabel(self.inputsFrame, text=' Inputs:', font=default_font)
    # self.inputsLabel.grid(row=0, column=0, padx=5, pady=5)
    self.inputCheckBox.configure(text='Inputs:')

    self.otg_check_value = ctk.BooleanVar()
    self.otgCheckBox = ctk.CTkCheckBox(self.inputsFrame, text='OTG', command=self.enable_otg, variable=self.otg_check_value, font=default_font)
    self.otgCheckBox.grid(row=0, column=1, padx=8, pady=8)
    
    self.keyboard_check_value = ctk.BooleanVar()
    self.keyboardCheckBox = ctk.CTkCheckBox(self.inputsFrame, text='Keyboard:', command=self.enable_keyboard_option, variable=self.keyboard_check_value, font=default_font)
    self.keyboardCheckBox.grid(row=0, column=2, padx=8, pady=8)
    self.keyboardCheckBox.configure(state='normal')

    self.keyboardModes: list = ["sdk", "uhid", "aoa"]
    self.keyboardMode_value = ctk.StringVar()
    self.keyboardMode_value.set(self.keyboardModes[0])

    self.keyboardMode_menu = ctk.CTkOptionMenu(self.inputsFrame, variable=self.keyboardMode_value, values=self.keyboardModes ,font=default_font)
    self.keyboardMode_menu.grid(row=0, column=3, padx=8, pady=8)
    self.keyboardMode_menu.configure(state='disabled')
    
    self.mouse_check_value = ctk.BooleanVar()
    self.mouseCheckBox = ctk.CTkCheckBox(self.inputsFrame, text='Mouse:', command=self.enable_mouse_option, variable=self.mouse_check_value, font=default_font)
    self.mouseCheckBox.grid(row=0, column=4, padx=8, pady=8)
    self.mouseCheckBox.configure(state='normal')
    
    self.mouseModes: list = ["sdk", "uhid", "aoa"]
    self.mouseMode_value = ctk.StringVar()
    self.mouseMode_value.set(self.mouseModes[0])

    self.mouseMode_menu = ctk.CTkOptionMenu(self.inputsFrame, variable=self.mouseMode_value, values=self.mouseModes, font=default_font)
    self.mouseMode_menu.grid(row=0, column=5, padx=8, pady=8)
    self.mouseMode_menu.configure(state='disabled')

    self.gamepad_check_value = ctk.BooleanVar()
    self.gamepadCheckBox = ctk.CTkCheckBox(self.inputsFrame, text='Gamepad:', command=self.enable_gamepad_option, variable=self.gamepad_check_value, font=default_font)
    self.gamepadCheckBox.grid(row=1, column=1, padx=8, pady=5)
    self.gamepadCheckBox.configure(state='normal')

    self.gamepadModes: list = ["uhid", "aoa"]
    self.gamepadMode_value = ctk.StringVar()
    self.gamepadMode_value.set(self.gamepadModes[0])

    self.gamepadMode_menu = ctk.CTkOptionMenu(self.inputsFrame, variable=self.gamepadMode_value, values=self.gamepadModes, font=default_font)
    self.gamepadMode_menu.grid(row=1, column=2, padx=8, pady=8)
    self.gamepadMode_menu.configure(state='disabled')

    self.no_control_check_value = ctk.BooleanVar()
    self.noControlCheckBox = ctk.CTkCheckBox(self.inputsFrame, text='No Control', command=self.enable_noControl_option, variable=self.no_control_check_value, font=default_font)
    self.noControlCheckBox.grid(row=1, column=3, padx=8, pady=8)


def enable_otg(self):
    if self.otg_check_value.get():
        self.keyboardCheckBox.configure(state='disabled')
        self.mouseCheckBox.configure(state='disabled')
    else:
        self.keyboardCheckBox.configure(state='normal')
        self.mouseCheckBox.configure(state='normal')
        
def enable_keyboard_option(self):
    if self.keyboard_check_value.get():
        self.otgCheckBox.configure(state='disabled')
        self.keyboardMode_menu.configure(state='normal')
    else:
        if not self.mouse_check_value.get():
            self.otgCheckBox.configure(state='normal')
        self.keyboardMode_menu.configure(state='disabled')

def enable_mouse_option(self):
    if self.mouse_check_value.get():
        self.otgCheckBox.configure(state='disabled')
        self.mouseMode_menu.configure(state='normal')
    else:
        if not self.keyboard_check_value.get():
            self.otgCheckBox.configure(state='normal')
        self.mouseMode_menu.configure(state='disabled')

def enable_gamepad_option(self):
    if self.gamepad_check_value.get():
        self.gamepadMode_menu.configure(state='normal')
    else:
        self.gamepadMode_menu.configure(state='disabled')

def enable_noControl_option(self):
    if self.no_control_check_value.get():
        self.otgCheckBox.configure(state='disabled')
        self.otg_check_value.set(False)

        self.keyboardCheckBox.configure(state='disabled')
        self.keyboardMode_menu.configure(state='disabled')
        self.keyboard_check_value.set(False)

        self.mouseCheckBox.configure(state='disabled')
        self.mouseMode_menu.configure(state='disabled')
        self.mouse_check_value.set(False)

        self.gamepadCheckBox.configure(state='disabled')
        self.gamepadMode_menu.configure(state='disabled')
        self.gamepad_check_value.set(False)
    else:
        self.otgCheckBox.configure(state='normal')
        self.keyboardCheckBox.configure(state='normal')
        self.mouseCheckBox.configure(state='normal')
        self.gamepadCheckBox.configure(state='normal')