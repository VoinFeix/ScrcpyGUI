import customtkinter as ctk
from modules.themes.themes import default_font
from modules.utils import listCameraIDs

def videoCheck(self):
    self.videoFrame = ctk.CTkFrame(self.lastFrame, border_color='black', border_width=3)
    self.videoFrame.pack(side=ctk.LEFT, anchor='w', padx=10, pady=10)
    
    self.video_check_value = ctk.BooleanVar()
    self.videoCheckBox = ctk.CTkCheckBox(self.videoFrame, text='Video', command=self.video_widget, variable=self.video_check_value, font=default_font)
    self.videoCheckBox.grid(row=0, column=0, padx=10, pady=10)

def video_widget(self):
    if not self.video_check_value.get():
        self.videoCheckBox.configure(text='Video')
        # self.noVideoCheckBox.destroy()
        # self.videoSourceLabel.destroy()
        self.videoSourceCheckBox.destroy()
        self.videoSourceMode_menu.destroy()

        self.noVideoPlaybackCheckBox.destroy()
        
        self.noVideoForwardingCheckBox.destroy()
        try:
        
            self.cameraIDCheckBox.destroy()
            self.cameraID_menu.destroy()

            self.cameraFacingCheckBox.destroy()
            self.cameraFacing_menu.destroy()
            # self.cameraIDs.clear()
        except Exception as e:
            print(f'Error on video widget\n{str(e)}')

        return


    self.videoCheckBox.configure(text='Video:')

    # self.noVideo_check_value = ctk.BooleanVar()
    # self.noVideoCheckBox = ctk.CTkCheckBox(self.videoFrame, text='NoVideoPlayback', command=None, variable=self.noVideo_check_value, font=default_font)
    # self.noVideoCheckBox.grid(row=1, column=0, padx=10, pady=10)
    # self.noVideoCheckBox.configure(state='normal')
    
    # self.videoSourceLabel = ctk.CTkLabel(self.videoFrame, text='VideoSource:', font=default_font)
    # self.videoSourceLabel.grid(row=0, column=1, padx=10, pady=10)

    self.videoSource_check_value = ctk.BooleanVar()
    self.videoSourceCheckBox = ctk.CTkCheckBox(self.videoFrame, text='VideoSource:', command=self.enable_videoSource_option, variable=self.videoSource_check_value, font=default_font)
    self.videoSourceCheckBox.grid(row=0, column=1, padx=10, pady=10)

    self.videoSourceModes: list = ["display", "camera"]
    self.videoSourceMode_value = ctk.StringVar()
    self.videoSourceMode_value.set(self.videoSourceModes[0])


    self.videoSourceMode_menu = ctk.CTkOptionMenu(self.videoFrame, variable=self.videoSourceMode_value, command=self.camera_widget, values=self.videoSourceModes, font=default_font)
    self.videoSourceMode_menu.grid(row=0, column=2, padx=10, pady=10)
    self.videoSourceMode_menu.configure(state='disabled')


    self.noVideoPlayback_check_value = ctk.BooleanVar()
    self.noVideoPlaybackCheckBox = ctk.CTkCheckBox(self.videoFrame, text='NoVideoPlayback', command=self.enable_noVideoPlayback_option, variable=self.noVideoPlayback_check_value, font=default_font)
    self.noVideoPlaybackCheckBox.grid(row=0, column=3, padx=10, pady=10)

    self.noVideoForwarding_check_value = ctk.BooleanVar()
    self.noVideoForwardingCheckBox = ctk.CTkCheckBox(self.videoFrame, text='NoVideoForwarding', command=None, variable=self.noVideoForwarding_check_value, font=default_font)
    self.noVideoForwardingCheckBox.grid(row=0, column=4, padx=10, pady=10)


def camera_widget(self, *args):    
    if self.videoSourceMode_menu.get() != "camera":
        try:
            self.cameraIDCheckBox.destroy()
            self.cameraID_menu.destroy()
            # self.cameraIDs.clear()

            self.cameraFacingCheckBox.destroy()
            self.cameraFacing_menu.destroy()
        except Exception as e:
            print(f'Error on Camera Widget\n{str(e)}')
        return

    self.cameraID_check_value = ctk.BooleanVar()
    self.cameraIDCheckBox = ctk.CTkCheckBox(self.videoFrame, text='CameraID:', command=self.enable_cameraID_option, variable=self.cameraID_check_value, font=default_font)
    self.cameraIDCheckBox.grid(row=1, column=1, padx=10, pady=10)
    
    cameraIDs: list = [] 
    l = listCameraIDs.getCameraIDs(self.videoFrame, self.devices_menu.get())

    for id in l:
        cameraIDs.append(id)

    print("Camera IDS: ", cameraIDs)
#    self.cameraID: list = ["temp"]
    self.cameraID_value = ctk.StringVar()
    self.cameraID_value.set(cameraIDs[0])

    self.cameraID_menu = ctk.CTkOptionMenu(self.videoFrame, variable=self.cameraID_value, command=None, font=default_font)
    self.cameraID_menu.grid(row=1, column=2, padx=10, pady=10)
    self.cameraID_menu.configure(values=cameraIDs)
    self.cameraID_menu.configure(state='disabled')

    self.cameraFacing_check_value = ctk.BooleanVar()
    self.cameraFacingCheckBox = ctk.CTkCheckBox(self.videoFrame, text='CameraFacing',command=self.enable_cameraFacing_option, variable=self.cameraFacing_check_value, font=default_font)
    self.cameraFacingCheckBox.grid(row=1, column=3, padx=10, pady=10)

    self.cameraFacings: list = ["front", "back", "external"]
    self.cameraFacing_value = ctk.StringVar()
    self.cameraFacing_value.set(self.cameraFacings[0])

    self.cameraFacing_menu = ctk.CTkOptionMenu(self.videoFrame, variable=self.cameraFacing_value, command=None, values=self.cameraFacings, font=default_font)
    self.cameraFacing_menu.grid(row=1, column=4, padx=10, pady=10)
    self.cameraFacing_menu.configure(state='disabled')



def enable_videoSource_option(self):
    if self.videoSource_check_value.get():
        self.videoSourceMode_menu.configure(state='normal')
        self.noVideoPlayback_check_value.set(0)
    else:
        self.videoSourceMode_menu.configure(state='disabled')
        try:
            self.cameraIDCheckBox.destroy()
            self.cameraID_menu.destroy()
            self.cameraFacingCheckBox.destroy()
            self.cameraFacing_menu.destroy()
            # self.cameraIDs.clear()
        except Exception as e:
            print(f'Error on enable videoSource function\n{str(e)}')

def enable_noVideoPlayback_option(self):
    if self.noVideoPlayback_check_value.get():
        self.videoSource_check_value.set(0)
        self.videoSourceMode_menu.configure(state='disabled')
        self.videoSourceCheckBox.configure(state='disabled')
        
        try:
            self.cameraIDCheckBox.destroy()
            self.cameraID_menu.destroy()
            # self.cameraIDs.clear()

            self.cameraFacingCheckBox.destroy()
            self.cameraFacing_menu.destroy()
            self.videoSourceMode_value.set(self.videoSourceModes[0])
        except Exception as e:
            print(f'Error on enable noVideoPlayback function\n{str(e)}')
        # self.camera_widget()
    else:
        self.videoSourceCheckBox.configure(state='normal')

def enable_cameraID_option(self):
    if self.cameraID_check_value.get():
        self.cameraID_menu.configure(state='normal')
        self.cameraFacing_check_value.set(0)
        self.cameraFacing_menu.configure(state='disabled')
    else:
        self.cameraID_menu.configure(state='disabled')
        
def enable_cameraFacing_option(self):
    if self.cameraFacing_check_value.get():
        self.cameraFacing_menu.configure(state='normal')
        self.cameraID_check_value.set(0)
        self.cameraID_menu.configure(state='disabled')
    else:
        self.cameraFacing_menu.configure(state='disabled')


