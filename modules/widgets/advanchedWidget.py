import customtkinter as ctk
import tkinter as tk
from modules.themes.themes import default_font, heading_font

ADVANCHED_WINDOW_NAME = 'Advanched Options'
ADVANCHED_WINDOW_GEOMETRY = '1000x1000'

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

    self.advanchedWindowHeading = ctk.CTkLabel(self.advanchedPopUpWindow, text='Advanched Options', font=heading_font)
    self.advanchedWindowHeading.pack(padx=10, pady=10)

    self.advanched_widgets_options()

    ctk.CTkButton(self.advanchedPopUpWindow, text='Exit',  command=self.exitAdvanchedWindow_func, font=default_font).pack(padx=10, pady=10)

        

def exitAdvanchedWindow_func(self):
    self.advanchedPopUpWindow.destroy()
    self.advanched_check_value.set(False)

def advanched_widgets_options(self):

    self.advanchedWindow_frame = ctk.CTkFrame(self.advanchedPopUpWindow, border_color='black', border_width=3)
    self.advanchedWindow_frame.pack(padx=10, pady=10)
    
    self.alwaysOnTop_check_value = ctk.BooleanVar()
    self.alwaysOnTopCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='AlwaysOnTop', command=False, variable=self.alwaysOnTop_check_value, font=default_font)
    self.alwaysOnTopCheckBox.grid(row=0, column=0, padx=10, pady=10)

    self.angle_check_value = ctk.BooleanVar()
    self.angleCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='Angle:', command=self.enable_angle_option, variable=self.angle_check_value, font=default_font)
    self.angleCheckBox.grid(row=0, column=1, padx=10, pady=10)

    # self.angleLabel = ctk.CTkLabel(self.advanchedWindow_frame, text='Angle:', font=default_font)
    # self.angleLabel.grid(row=0, column=0, padx=5, pady=5)

    self.angleEntry = ctk.CTkEntry(self.advanchedWindow_frame, width=70, font=default_font)
    self.angleEntry.grid(row=0, column=2, padx=10, pady=10)
    self.angleEntry.insert(ctk.END, '360')
    self.angleEntry.configure(state='disabled')

    self.audioBitRate_check_value = ctk.BooleanVar()
    self.audioBitRateCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='AudioBitRate:', command=self.enable_audioBitRate_option, variable=self.audioBitRate_check_value, font=default_font)
    self.audioBitRateCheckBox.grid(row=1, column=0, padx=10, pady=10)

    self.audioBitRateEntry = ctk.CTkEntry(self.advanchedWindow_frame, width=150, font=default_font)
    self.audioBitRateEntry.grid(row=1, column=1, padx=10, pady=10)
    self.audioBitRateEntry.insert(ctk.END, '128K')
    self.audioBitRateEntry.configure(state='disabled')

    self.audioBuffer_check_value = ctk.BooleanVar()
    self.audioBufferCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='AudioBuffer:', command=self.enable_audioBuffer_option, variable=self.audioBuffer_check_value, font=default_font)
    self.audioBufferCheckBox.grid(row=1, column=2, padx=10, pady=10)

    self.audioBufferEntry = ctk.CTkEntry(self.advanchedWindow_frame, width=70, font=default_font)
    self.audioBufferEntry.grid(row=1, column=3, padx=10, pady=10)
    self.audioBufferEntry.insert(ctk.END, '50')
    self.audioBufferEntry.configure(state='disabled')

    self.audioCodec_check_value = ctk.BooleanVar()
    self.audioCodecCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='AudioCodec:', command=self.enable_audioCodec_option, variable=self.audioCodec_check_value, font=default_font)
    self.audioCodecCheckBox.grid(row=2, column=0, padx=10, pady=10)

    self.audioCodecOptions: list = ["opus", "aac", "flac", "raw"]
    self.audioCodec_value = ctk.StringVar()
    self.audioCodec_value.set(self.audioCodecOptions[0])

    self.audioCodecOptionMenu = ctk.CTkOptionMenu(self.advanchedWindow_frame, variable=self.audioCodec_value, values=self.audioCodecOptions, font=default_font)
    self.audioCodecOptionMenu.grid(row=2, column=1, padx=10, pady=10)
    self.audioCodecOptionMenu.configure(state='disabled')   

    self.audioDup_check_value = ctk.BooleanVar()
    self.audioDupCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='AudioDup', command=False, variable=self.audioDup_check_value, font=default_font)
    self.audioDupCheckBox.grid(row=2, column=2, padx=10, pady=10)
    self.audioDupCheckBox.configure(state='disabled')

    self.get_audioDup_option()

    self.audioEncoder_check_value = ctk.BooleanVar()
    self.audioEncoderCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='AudioEncoder:', command=self.enable_audioEncoder_option, variable=self.audioEncoder_check_value, font=default_font)
    self.audioEncoderCheckBox.grid(row=3, column=0, padx=10, pady=10)

    self.audioEncoders: list = ["Sample"]
    self.audioEncoder_value = ctk.StringVar()
    self.audioEncoder_value.set(self.audioEncoders[0])

    self.audioEncoderOptionMenu = ctk.CTkOptionMenu(self.advanchedWindow_frame, variable=self.audioEncoder_value, values=self.audioEncoders, font=default_font)
    self.audioEncoderOptionMenu.grid(row=3, column=1, padx=10, pady=10)
    self.audioEncoderOptionMenu.configure(state='disabled')

    self.audioOutputBuffer_check_value = ctk.BooleanVar()
    self.audioOutputBufferCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='AudioOutputBuffer:', variable=self.audioOutputBuffer_check_value, command=self.enable_audioOutputBuffer_option, font=default_font)
    self.audioOutputBufferCheckBox.grid(row=3, column=2, padx=10, pady=10)

    self.audioOutputBufferEntry = ctk.CTkEntry(self.advanchedWindow_frame, width=70, font=default_font)
    self.audioOutputBufferEntry.grid(row=3, column=3, padx=10, pady=10)
    self.audioOutputBufferEntry.insert(ctk.END, '5')
    self.audioOutputBufferEntry.configure(state='disabled')

    self.videoBitRate_check_value = ctk.BooleanVar()
    self.videoBitRateCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='VideoBitRate:', command=self.enable_videoBitRate_option, variable=self.videoBitRate_check_value, font=default_font)
    self.videoBitRateCheckBox.grid(row=4, column=0, padx=10, pady=10)

    self.videoBitRateEntry = ctk.CTkEntry(self.advanchedWindow_frame, width=150, font=default_font)
    self.videoBitRateEntry.grid(row=4, column=1, padx=10, pady=10)
    self.videoBitRateEntry.insert(ctk.END, '8M')
    self.videoBitRateEntry.configure(state='disabled')
    
    self.cameraAr_check_value = ctk.BooleanVar()
    self.cameraArCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='CameraAr:', command=self.enable_cameraAr_option, variable=self.cameraAr_check_value, font=default_font)
    self.cameraArCheckBox.grid(row=4, column=2, padx=10, pady=10)

    self.cameraArEntry = ctk.CTkEntry(self.advanchedWindow_frame, width=70, font=default_font)
    self.cameraArEntry.grid(row=4, column=3, padx=10, pady=10)
    # self.cameraArEntry.insert(ctk.END, '')
    self.cameraArEntry.configure(state='disabled')

    self.cameraFps_check_value = ctk.BooleanVar()
    self.cameraFpsCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='CameraFps:', command=self.enable_cameraFps_option, variable=self.cameraFps_check_value, font=default_font)
    self.cameraFpsCheckBox.grid(row=5, column=0, padx=10, pady=10)

    self.cameraFpsEntry = ctk.CTkEntry(self.advanchedWindow_frame, width=70, font=default_font)
    self.cameraFpsEntry.grid(row=5, column=1, padx=10, pady=10)
    self.cameraFpsEntry.insert(ctk.END, '30')
    self.cameraFpsEntry.configure(state='disabled')

    self.cameraHighSpeed_check_value = ctk.BooleanVar()
    self.cameraHighSpeedCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='CameraHighSpeed', command=False, variable=self.cameraHighSpeed_check_value, font=default_font)
    self.cameraHighSpeedCheckBox.grid(row=5, column=2, padx=10, pady=10)

    self.cameraSize_check_value = ctk.BooleanVar()
    self.cameraSizeCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='CameraSize:', command=self.enable_cameraSize_option, variable=self.cameraSize_check_value, font=default_font)
    self.cameraSizeCheckBox.grid(row=6, column=0, padx=10, pady=10)

    self.cameraSizeEntry = ctk.CTkEntry(self.advanchedWindow_frame, width=150, font=default_font)
    self.cameraSizeEntry.grid(row=6, column=1, padx=10, pady=10)
    # self.cameraSizeEntry.insert(ctk.END, '')
    self.cameraSizeEntry.configure(state='disabled')

    self.captureOrientation_check_value = ctk.BooleanVar()
    self.captureOrientationCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='CaptureOrientation:', command=self.enable_captureOrientation_option, variable=self.captureOrientation_check_value, font=default_font)
    self.captureOrientationCheckBox.grid(row=6, column=2, padx=10, pady=10)

    self.captureOrientationEntry = ctk.CTkEntry(self.advanchedWindow_frame, width=70, font=default_font)
    self.captureOrientationEntry.grid(row=6, column=3, padx=10, pady=10)
    # self.captureOrientationEntry.insert(ctk.END, '')
    self.captureOrientationEntry.configure(state='disabled')

    self.crop_check_value = ctk.BooleanVar()
    self.cropCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='Crop:', command=self.enable_crop_option, variable=self.crop_check_value, font=default_font)
    self.cropCheckBox.grid(row=7, column=0, padx=10, pady=10)

    self.cropEntry = ctk.CTkEntry(self.advanchedWindow_frame, width=150, font=default_font)
    self.cropEntry.grid(row=7, column=1, padx=10, pady=10)
    # self.cropEntry.insert(ctk.END, '')
    self.cropEntry.configure(state='disabled')
    
    self.disableScreenSaver_check_value = ctk.BooleanVar()
    self.disableScreenSaverCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='DisableScreenSaver', command=False, variable=self.disableScreenSaver_check_value, font=default_font)
    self.disableScreenSaverCheckBox.grid(row=7, column=2, padx=10, pady=10)

    self.fullScreen_check_value = ctk.BooleanVar()
    self.fullScreenCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='FullScreen', command=False, variable=self.fullScreen_check_value, font=default_font)
    self.fullScreenCheckBox.grid(row=8, column=0, padx=10, pady=10)

    self.forceAdbForward_check_value = ctk.BooleanVar()
    self.forceAdbForwardCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='ForceAdbForward', variable=self.forceAdbForward_check_value, font=default_font)
    self.forceAdbForwardCheckBox.grid(row=8, column=1, padx=10, pady=10)
    
    self.forceAdbForward_check_value = ctk.BooleanVar()
    self.forceAdbForwardCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='ForceAdbForward', variable=self.forceAdbForward_check_value, font=default_font)
    self.forceAdbForwardCheckBox.grid(row=8, column=1, padx=10, pady=10)

    self.killAdbOnClose_check_value = ctk.BooleanVar()
    self.killAdbOnCloseCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='killAdbOnClose', variable=self.killAdbOnClose_check_value, font=default_font)
    self.killAdbOnCloseCheckBox.grid(row=8, column=2, padx=10, pady=10)

    self.legacyPaste_check_value = ctk.BooleanVar()
    self.legacyPasteCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='LegacyPaste', variable=self.legacyPaste_check_value, font=default_font)
    self.legacyPasteCheckBox.grid(row=9, column=0, padx=10, pady=10)

    self.maxSize_check_value = ctk.BooleanVar()
    self.maxSizeCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='MaxSize:', command=self.enable_maxSize_option, variable=self.maxSize_check_value, font=default_font)
    self.maxSizeCheckBox.grid(row=9, column=1, padx=10, pady=10)

    self.maxSizeEntry = ctk.CTkEntry(self.advanchedWindow_frame, width=150, font=default_font)
    self.maxSizeEntry.grid(row=9, column=2, padx=10, pady=10)
    # self.maxSizeEntry.insert(ctk.END, '')
    self.maxSizeEntry.configure(state='disabled')


    self.maxFps_check_value = ctk.BooleanVar()
    self.maxFpsCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='MaxFps:', command=self.enable_maxFps_option, variable=self.maxFps_check_value, font=default_font)
    self.maxFpsCheckBox.grid(row=10, column=0, padx=10, pady=10)

    self.maxFpsEntry = ctk.CTkEntry(self.advanchedWindow_frame, width=70, font=default_font)
    self.maxFpsEntry.grid(row=10, column=1, padx=10, pady=10)
    # self.FpsEntry.insert(ctk.END, '')
    self.maxFpsEntry.configure(state='disabled')

    self.newDisplay_check_value = ctk.BooleanVar()
    self.newDisplayCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='NewDisplay:', command=self.enable_newDisplay_option, variable=self.newDisplay_check_value, font=default_font)
    self.newDisplayCheckBox.grid(row=10, column=2, padx=10, pady=10)

    self.newDisplayEntry = ctk.CTkEntry(self.advanchedWindow_frame, width=150, font=default_font)
    self.newDisplayEntry.grid(row=10, column=3, padx=10, pady=10)
    # self.newDisplayEntry.insert(ctk.END, '')
    self.newDisplayEntry.configure(state='disabled')

    self.noCleanUp_check_value = ctk.BooleanVar()
    self.noCleanUpCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='NoCleanUp', variable=self.noCleanUp_check_value, font=default_font)
    self.noCleanUpCheckBox.grid(row=11, column=0, padx=10, pady=10)

    self.noClipboardAutoSync_check_value = ctk.BooleanVar()
    self.noClipboardAutoSyncCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='NoClipboardAutoSync', variable=self.noClipboardAutoSync_check_value, font=default_font)
    self.noClipboardAutoSyncCheckBox.grid(row=11, column=1, padx=10, pady=10)


    self.noDownsizeOnError_check_value = ctk.BooleanVar()
    self.noDownsizeOnErrorCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='NoDownsizeOnError', variable=self.noDownsizeOnError_check_value, font=default_font)
    self.noDownsizeOnErrorCheckBox.grid(row=11, column=2, padx=10, pady=10)

    self.noKeyRepeat_check_value = ctk.BooleanVar()
    self.noKeyRepeatCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='NoKeyRepeat', variable=self.noKeyRepeat_check_value, font=default_font)
    self.noKeyRepeatCheckBox.grid(row=12, column=0, padx=10, pady=10)


    self.noMipMaps_check_value = ctk.BooleanVar()
    self.noMipMapsCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='NoMipMaps', variable=self.noMipMaps_check_value, font=default_font)
    self.noMipMapsCheckBox.grid(row=12, column=1, padx=10, pady=10)

    self.noMouseHover_check_value = ctk.BooleanVar()
    self.noMouseHoverCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='NoMouseHover', variable=self.noMouseHover_check_value, font=default_font)
    self.noMouseHoverCheckBox.grid(row=12, column=2, padx=10, pady=10)



    self.noPowerOn_check_value = ctk.BooleanVar()
    self.noPowerOnCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='NoPowerOn', variable=self.noPowerOn_check_value, font=default_font)
    self.noPowerOnCheckBox.grid(row=13, column=0, padx=10, pady=10)


    self.noVdDestroyContent_check_value = ctk.BooleanVar()
    self.noVdDestroyContentCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='NoVdDestroyContent', variable=self.noVdDestroyContent_check_value, font=default_font)
    self.noVdDestroyContentCheckBox.grid(row=13, column=1, padx=10, pady=10)

    self.noVdSystemDecorations_check_value = ctk.BooleanVar()
    self.noVdSystemDecorationsCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='NoVdSystemDecorations', variable=self.noVdSystemDecorations_check_value, font=default_font)
    self.noVdSystemDecorationsCheckBox.grid(row=13, column=2, padx=10, pady=10)

    self.port_check_value = ctk.BooleanVar()
    self.portCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='Port:', command=self.enable_port_option, variable=self.port_check_value, font=default_font)
    self.portCheckBox.grid(row=14, column=0, padx=10, pady=10)

    self.portEntry = ctk.CTkEntry(self.advanchedWindow_frame, width=150, font=default_font)
    self.portEntry.grid(row=14, column=1, padx=10, pady=10)
    self.portEntry.configure(state='disabled')

    self.pauseOnExit_check_value = ctk.BooleanVar()
    self.pauseOnExitCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='PauseOnExit:', command=self.enable_pauseOnExit_option, variable=self.pauseOnExit_check_value, font=default_font)
    self.pauseOnExitCheckBox.grid(row=14, column=2, padx=10, pady=10)

    self.pauseOnExitEntry = ctk.CTkEntry(self.advanchedWindow_frame, width=150, font=default_font)
    self.pauseOnExitEntry.grid(row=14, column=3, padx=10, pady=10)
    self.pauseOnExitEntry.configure(state='disabled')

    self.powerOffOnClose_check_value = ctk.BooleanVar()
    self.powerOffOnCloseCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='PowerOffOnClose', variable=self.powerOffOnClose_check_value, font=default_font)
    self.powerOffOnCloseCheckBox.grid(row=15, column=0, padx=10, pady=10)

    self.preferText_check_value = ctk.BooleanVar()
    self.preferTextCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='PreferText', variable=self.preferText_check_value, font=default_font)
    self.preferTextCheckBox.grid(row=15, column=1, padx=10, pady=10)

    self.printFps_check_value = ctk.BooleanVar()
    self.printFpsCheckBox = ctk.CTkCheckBox(self.advanchedWindow_frame, text='PrintFps', variable=self.printFps_check_value, font=default_font)
    self.printFpsCheckBox.grid(row=15, column=2, padx=10, pady=10)


    
    







def enable_angle_option(self):
    if self.angle_check_value.get():
        self.angleEntry.configure(state='normal')
    else:
        self.angleEntry.configure(state='disabled')


def enable_audioBitRate_option(self):
    # self.audioBitRateEntry.configure(state='normal') if self.audioBitRate_check_value.get() else self.audioBitRateEntry.configure(state='disabled')
 
    if self.audioBitRate_check_value.get():
        self.audioBitRateEntry.configure(state='normal')
    else:
        self.audioBitRateEntry.configure(state='disabled')

def enable_audioBuffer_option(self):
    if self.audioBuffer_check_value.get():
        self.audioBufferEntry.configure(state='normal')
    else:
        self.audioBufferEntry.configure(state='disabled')

def enable_audioCodec_option(self):
    if self.audioCodec_check_value.get():
        self.audioCodecOptionMenu.configure(state='normal')
    else:
        self.audioCodecOptionMenu.configure(state='disabled')

def get_audioDup_option(self):
    try:
        if self.audioSourceMode_value.get() == "playback":
            self.audioDupCheckBox.configure(state='normal')
        else:
            self.audioDupCheckBox.configure(state='disabled')
    except Exception as e:
        print(f'Error on get_audioDup_option function\n{str(e)}')

def enable_audioEncoder_option(self):
    if self.audioEncoder_check_value.get():
        self.audioEncoderOptionMenu.configure(state='normal')
    else:
        self.audioEncoderOptionMenu.configure(state='disabled')

def enable_audioOutputBuffer_option(self):
    if self.audioOutputBuffer_check_value.get():
        self.audioOutputBufferEntry.configure(state='normal')
    else:
        self.audioOutputBufferEntry.configure(state='disabled')

def enable_videoBitRate_option(self):
    if self.videoBitRate_check_value.get():
        self.videoBitRateEntry.configure(state='normal')
    else:
        self.videoBitRateEntry.configure(state='disabled')

def enable_cameraAr_option(self):
    if self.cameraAr_check_value.get():
        self.cameraArEntry.configure(state='normal')
    else:
        self.cameraArEntry.configure(state='disabled')

def enable_cameraFps_option(self):
    if self.cameraFps_check_value.get():
        self.cameraFpsEntry.configure(state='normal')
    else:
        self.cameraFpsEntry.configure(state='disabled')

def enable_cameraSize_option(self):
    if self.cameraSize_check_value.get():
        self.cameraSizeEntry.configure(state='normal')
    else:
        self.cameraSizeEntry.configure(state='disabled')

def enable_captureOrientation_option(self):
    if self.captureOrientation_check_value.get():
        self.captureOrientationEntry.configure(state='normal')
    else:
        self.captureOrientationEntry.configure(state='disabled')

def enable_crop_option(self):
    if self.crop_check_value.get():
        self.cropEntry.configure(state='normal')
    else:
        self.cropEntry.configure(state='disabled')


def enable_maxSize_option(self):
    if self.maxSize_check_value.get():
        self.maxSizeEntry.configure(state='normal')
    else:
        self.maxSizeEntry.configure(state='disabled')


def enable_maxFps_option(self):
    if self.maxFps_check_value.get():
        self.maxFpsEntry.configure(state='normal')
    else:
        self.maxFpsEntry.configure(state='disabled')

def enable_newDisplay_option(self):
    if self.newDisplay_check_value.get():
        self.newDisplayEntry.configure(state='normal')
    else:
        self.newDisplayEntry.configure(state='disabled')

def enable_port_option(self):
    if self.port_check_value.get():
        self.portEntry.configure(state='normal')
    else:
        self.portEntry.configure(state='disabled')

def enable_pauseOnExit_option(self):
    if self.pauseOnExit_check_value.get():
        self.pauseOnExitEntry.configure(state='normal')
    else:
        self.pauseOnExitEntry.configure(state='disabled')

