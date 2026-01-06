import customtkinter as ctk
from modules.themes.themes import default_font
from modules.utils.devices import getDevices
from modules.utils.listCameraIDs import getCameraIDs

def devicesWidget(self):
    self.devicesFrame = ctk.CTkFrame(self.firstFrame, border_color='black', border_width=3)
    self.devicesFrame.pack(side=ctk.LEFT, anchor='nw', padx=10, pady=10)

    self.devicesListLabel = ctk.CTkLabel(self.devicesFrame, text='Devices:', font=default_font)
    self.devicesListLabel.grid(row=0, column=0, padx=10, pady=10)

    self.device_value = ctk.StringVar()
    # self.device_value.set(self.devices[0])

    self.devices_menu = ctk.CTkOptionMenu(self.devicesFrame, variable=self.device_value, font=default_font, command=None)
    self.devices_menu.grid(row=0, column=1, padx=10, pady=10)
    self.get_devices_list()

    # TODO: Fix this later
    ctk.CTkButton(self.devicesFrame, text='⟳', command=self.get_devices_list, font=default_font, width=28, height=28).grid(row=0, column=2, padx=10, pady=10)    

def get_devices_list(self):
    self.devices: list = getDevices()
    self.device_value.set(self.devices[0])
    self.devices_menu.configure(values=self.devices)
    

def update_everything(self):
    
    self.cameraID = getCameraIDs(self, self.devices_menu.get())
    self.cameraID_menu.configure(values=self.cameraID)