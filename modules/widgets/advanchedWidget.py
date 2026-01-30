import customtkinter as ctk
import tkinter as tk
from modules.themes.themes import default_font, heading_font, frame_font
import modules.utils.getEncoders

ADVANCHED_WINDOW_NAME = 'Advanched Options'
ADVANCHED_WINDOW_GEOMETRY = '1000x700'
valuesDict: dict = {}

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

    if valuesDict:
        print(f"{"="*100}\n")
        print(valuesDict)
        print(f"{"="*100}\n")
    else:
        print('ValuesDict is empty')
    
    self.advanched_widgets_options()

    ctk.CTkButton(self.advanchedPopUpWindow, text='Done', command=self.doneAdvanchedWindow_func, font=default_font).pack(padx=10, pady=10)
    ctk.CTkButton(self.advanchedPopUpWindow, text='Exit',  command=self.exitAdvanchedWindow_func, font=default_font).pack(padx=10, pady=10)


def exitAdvanchedWindow_func(self):
    self.advanchedPopUpWindow.destroy()
    self.advanched_check_value.set(False)

def doneAdvanchedWindow_func(self):
    global valuesDict
    values: dict = valuesDict
    try:        
        values['audioBitRate'] = self.audioBitRateEntry.get() if self.audioBitRate_check_value.get() else None
        values['audioBuffer'] = self.audioBufferEntry.get() if self.audioBuffer_check_value.get() else None
        values['audioOutputBuffer'] = self.audioOutputBufferEntry.get() if self.audioOutputBuffer_check_value.get() else None
        values['audioCodec'] = self.audioCodec_value.get() if self.audioCodec_check_value.get() else None
        values['audioEncoder'] = self.audioEncoder_value.get() if self.audioEncoder_check_value.get() else None
        values['audioDup'] = self.audioDup_check_value.get() if self.audioDup_check_value.get() else None

        values['videoBitRate'] = self.videoBitRateEntry.get() if self.videoBitRate_check_value.get() else None
        values['videoBuffer'] = self.videoBufferEntry.get() if self.videoBuffer_check_value.get() else None
        values['videoCodec'] = self.videoCodec_value.get() if self.videoCodec_check_value.get() else None
        values['videoEncoder'] = self.videoEncoder_value.get() if self.videoEncoder_check_value.get() else None

        values['cameraAr'] = self.cameraArEntry.get() if self.cameraAr_check_value.get() else None
        values['cameraFps'] = self.cameraFpsEntry.get() if self.cameraFps_check_value.get() else None
        values['cameraSize'] = self.cameraSizeEntry.get() if self.cameraSize_check_value.get() else None
        values['cameraHighSpeed'] = self.cameraHighSpeed_check_value.get() if self.cameraHighSpeed_check_value.get() else None
        
        values['windowTitle'] = self.windowTitleEntry.get() if self.windowTitle_check_value.get() else None
        values['windowX'] = self.windowXEntry.get() if self.windowX_check_value.get() else None
        values['windowY'] = self.windowYEntry.get() if self.windowY_check_value.get() else None
        values['windowWidth'] = self.windowWidthEntry.get() if self.windowWidth_check_value.get() else None
        values['windowHeight'] = self.windowHeightEntry.get() if self.windowHeight_check_value.get() else None
        values['newDisplay'] = self.newDisplayEntry.get() if self.newDisplay_check_value.get() else None
        values['maxSize'] = self.maxSizeEntry.get() if self.maxSize_check_value.get() else None
        values['crop'] = self.cropEntry.get() if self.crop_check_value.get() else None
        values['angle'] = self.angleEntry.get() if self.angle_check_value.get() else None
        values['alwaysOnTop'] = self.alwaysOnTop_check_value.get() if self.alwaysOnTop_check_value.get() else None
        values['fullScreen'] = self.fullScreen_check_value.get() if self.fullScreen_check_value.get() else None
        values['windowBorderless'] = self.windowBorderless_check_value.get() if self.windowBorderless_check_value.get() else None

        values['maxFps'] = self.maxFpsEntry.get() if self.maxFps_check_value.get() else None
        values['shortcutMod'] = self.shortcutMod_value.get() if self.shortcutMod_check_value.get() else None
        values['forceAdbForward'] = self.forceAdbForward_check_value.get() if self.forceAdbForward_check_value.get() else None
        values['killAdbOnClose'] = self.killAdbOnClose_check_value.get() if self.killAdbOnClose_check_value.get() else None
        values['noKeyRepeat'] = self.noKeyRepeat_check_value.get() if self.noKeyRepeat_check_value.get() else None
        values['rawKeyEvents'] = self.rawKeyEvents_check_value.get() if self.rawKeyEvents_check_value.get() else None
        values['legacyPaste'] = self.legacyPaste_check_value.get() if self.legacyPaste_check_value.get() else None
        values['showTouches'] = self.showTouches_check_value.get() if self.showTouches_check_value.get() else None
        values['noMouseHover'] = self.noMouseHover_check_value.get() if self.noMouseHover_check_value.get() else None

        values['pauseOnExit'] = self.pauseOnExitEntry.get() if self.pauseOnExit_check_value.get() else None
        values['screenOffTimeout'] = self.screenOffTimeoutEntry.get() if self.screenOffTimeout_check_value.get() else None            
        values['timeLimit'] = self.timeLimitEntry.get() if self.timeLimit_check_value.get() else None
        values['noPowerOn'] = self.noPowerOn_check_value.get() if self.noPowerOn_check_value.get() else None
        values['turnScreenOff'] = self.turnScreenOff_check_value.get() if self.turnScreenOff_check_value.get() else None
        values['powerOffOnClose'] = self.powerOffOnClose_check_value.get() if self.powerOffOnClose_check_value.get() else None
        values['disableScreenSaver'] = self.disableScreenSaver_check_value.get() if self.disableScreenSaver_check_value.get() else None
        values['stayAwake'] = self.stayAwake_check_value.get() if self.stayAwake_check_value.get() else None

        values['record'] = self.recordEntry.get() if self.record_check_value.get() else None
        values['recordFormats'] = self.recordFormats_value.get() if self.recordFormats_check_value.get() else None
        values['recordOrientation'] = self.recordOrientation_value.get() if  self.recordOrientation_check_value.get() else None

        values['port'] = self.portEntry.get() if self.port_check_value.get() else None
        values['tunnelHost'] = self.tunnelHostEntry.get() if self.tunnelHost_check_value.get() else None
        values['tunnelPort'] = self.tunnelPortEntry.get() if self.tunnelPort_check_value.get() else None

        values['noVdDestroyContent'] = self.noVdDestroyContent_check_value.get() if self.noVdDestroyContent_check_value.get() else None
        values['noVdSystemDecorations'] = self.noVdSystemDecorations_check_value.get() if self.noVdSystemDecorations_check_value.get() else None

        values['v4l2Sink'] = self.v4l2SinkEntry.get() if self.v4l2Sink_check_value.get() else None
        values['v4l2Buffer'] = self.v4l2BufferEntry.get() if self.v4l2BufferEntry.get() else None

        values['renderDriver'] = self.renderDriver_value.get() if self.renderDriver_check_value.get() else None

        values['startApp'] = self.startAppEntry.get() if self.startApp_check_value.get() else None

        values['pushTarget'] = self.pushTargetEntry.get() if self.pushTarget_check_value.get() else None
        values['captureOrientation'] = self.captureOrientationEntry.get() if self.captureOrientation_check_value.get() else None
        values['noCleanUp'] = self.noCleanUp_check_value.get() if self.noCleanUp_check_value.get() else None
        values['noClipboardAutoSync'] = self.noClipboardAutoSync_check_value.get() if self.noClipboardAutoSync_check_value.get() else None
        values['noDownsizeOnError'] = self.noDownsizeOnError_check_value.get() if self.noDownsizeOnError_check_value.get() else None
        values['noMipMaps'] = self.noMipMaps_check_value.get() if self.noMipMaps_check_value.get() else None
        values['printFps'] = self.printFps_check_value.get() if self.printFps_check_value.get() else None
        values['preferText'] = self.preferText_check_value.get() if self.preferText_check_value.get() else None
        values['requireAudio'] = self.requireAudio_check_value.get() if self.requireAudio_check_value.get() else None
        
    except Exception as e:
        print(f'Error on doneAdvanchedWindow_func: {e}')

    self.exitAdvanchedWindow_func()
    


def audioOptionFrame_func(self, master):
    self.audioOptionFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.audioOptionFrame.grid(row=0, column=0, padx=10, pady=10)
    ctk.CTkLabel(self.audioOptionFrame, text='-: Audio :-', font=frame_font).grid(row=0, column=0, padx=10, pady=10)


    self.audioBitRate_check_value = ctk.BooleanVar()
    self.audioBitRateCheckBox = ctk.CTkCheckBox(self.audioOptionFrame, text='AudioBitRate:', command=self.enable_audioBitRate_option, variable=self.audioBitRate_check_value, font=default_font)
    self.audioBitRateCheckBox.grid(row=1, column=0, padx=10, pady=10)

    self.audioBitRateEntry = ctk.CTkEntry(self.audioOptionFrame, width=150, font=default_font)
    self.audioBitRateEntry.grid(row=1, column=1, padx=10, pady=10)
    self.audioBitRateEntry.insert(ctk.END, '128K')
    self.audioBitRateEntry.configure(state='disabled')


    self.audioBuffer_check_value = ctk.BooleanVar()
    self.audioBufferCheckBox = ctk.CTkCheckBox(self.audioOptionFrame, text='AudioBuffer:', command=self.enable_audioBuffer_option, variable=self.audioBuffer_check_value, font=default_font)
    self.audioBufferCheckBox.grid(row=2, column=0, padx=10, pady=10)

    self.audioBufferEntry = ctk.CTkEntry(self.audioOptionFrame, width=150, font=default_font)
    self.audioBufferEntry.grid(row=2, column=1, padx=10, pady=10)
    self.audioBufferEntry.insert(ctk.END, '50')
    self.audioBufferEntry.configure(state='disabled')


    self.audioOutputBuffer_check_value = ctk.BooleanVar()
    self.audioOutputBufferCheckBox = ctk.CTkCheckBox(self.audioOptionFrame, text='AudioOutputBuffer:', variable=self.audioOutputBuffer_check_value, command=self.enable_audioOutputBuffer_option, font=default_font)
    self.audioOutputBufferCheckBox.grid(row=3, column=0, padx=10, pady=10)

    self.audioOutputBufferEntry = ctk.CTkEntry(self.audioOptionFrame, width=150, font=default_font)
    self.audioOutputBufferEntry.grid(row=3, column=1, padx=10, pady=10)
    self.audioOutputBufferEntry.insert(ctk.END, '5')
    self.audioOutputBufferEntry.configure(state='disabled')


    self.audioCodec_check_value = ctk.BooleanVar()
    self.audioCodecCheckBox = ctk.CTkCheckBox(self.audioOptionFrame, text='AudioCodec:', command=self.enable_audioCodec_option, variable=self.audioCodec_check_value, font=default_font)
    self.audioCodecCheckBox.grid(row=4, column=0, padx=10, pady=10)

    self.audioCodecOptions: list = ["opus", "aac", "flac", "raw"]
    self.audioCodec_value = ctk.StringVar()
    self.audioCodec_value.set(self.audioCodecOptions[0])


    self.audioCodecOptionMenu = ctk.CTkOptionMenu(self.audioOptionFrame, variable=self.audioCodec_value, command=None, values=self.audioCodecOptions, font=default_font)
    self.audioCodecOptionMenu.grid(row=4, column=1, padx=10, pady=10)
    self.audioCodecOptionMenu.configure(state='disabled')   
    

    self.audioEncoders: list = modules.utils.getEncoders.getEncoders(self, self.devices_menu.get(), forAudio=True)

    self.audioEncoder_check_value = ctk.BooleanVar()
    self.audioEncoderCheckBox = ctk.CTkCheckBox(self.audioOptionFrame, text='AudioEncoder:', command=self.enable_audioEncoder_option, variable=self.audioEncoder_check_value, font=default_font)
    self.audioEncoderCheckBox.grid(row=5, column=0, padx=10, pady=10)

    self.audioEncoder_value = ctk.StringVar()
    self.audioEncoder_value.set(self.audioEncoders[0])

    self.audioEncoderOptionMenu = ctk.CTkOptionMenu(self.audioOptionFrame, variable=self.audioEncoder_value, font=default_font)
    self.audioEncoderOptionMenu.grid(row=5, column=1, padx=10, pady=10)
    self.audioEncoderOptionMenu.configure(values=self.audioEncoders)
    self.audioEncoderOptionMenu.configure(state='disabled')

    self.audioDup_check_value = ctk.BooleanVar()
    self.audioDupCheckBox = ctk.CTkCheckBox(self.audioOptionFrame, text='AudioDup', command=False, variable=self.audioDup_check_value, font=default_font)
    self.audioDupCheckBox.grid(row=6, column=0, padx=10, pady=10)
    self.audioDupCheckBox.configure(state='disabled')
    self.get_audioDup_option()



def videoOptionFrame_func(self, master):
    self.videoOptionFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.videoOptionFrame.grid(row=0, column=1, padx=10, pady=10)
    ctk.CTkLabel(self.videoOptionFrame, text='-: Video :-', font=frame_font).grid(row=0, column=0, padx=10, pady=10)

    self.videoBitRate_check_value = ctk.BooleanVar()
    self.videoBitRateCheckBox = ctk.CTkCheckBox(self.videoOptionFrame, text='VideoBitRate:', command=self.enable_videoBitRate_option, variable=self.videoBitRate_check_value, font=default_font)
    self.videoBitRateCheckBox.grid(row=1, column=0, padx=10, pady=10)

    self.videoBitRateEntry = ctk.CTkEntry(self.videoOptionFrame, width=150, font=default_font)
    self.videoBitRateEntry.grid(row=1, column=1, padx=10, pady=10)
    self.videoBitRateEntry.insert(ctk.END, '8M')
    self.videoBitRateEntry.configure(state='disabled')


    self.videoBuffer_check_value = ctk.BooleanVar()
    self.videoBufferCheckBox = ctk.CTkCheckBox(self.videoOptionFrame, text='VideoBuffer:', command=self.enable_videoBuffer_option, variable=self.videoBuffer_check_value, font=default_font)
    self.videoBufferCheckBox.grid(row=2, column=0, padx=10, pady=10)
    
    self.videoBufferEntry = ctk.CTkEntry(self.videoOptionFrame, width=150, font=default_font)
    self.videoBufferEntry.grid(row=2, column=1, padx=10, pady=10)
    self.videoBufferEntry.insert(ctk.END, '0')
    self.videoBufferEntry.configure(state='disabled')


    self.videoCodec_check_value = ctk.BooleanVar()
    self.videoCodecCheckBox = ctk.CTkCheckBox(self.videoOptionFrame, text='VideoCodec:', command=self.enable_videoCodec_option, variable=self.videoCodec_check_value, font=default_font)
    self.videoCodecCheckBox.grid(row=3, column=0, padx=10, pady=10)

    self.videoCodecs: list = ["h264", "h265", "av1"]
    self.videoCodec_value = ctk.StringVar()
    self.videoCodec_value.set(self.videoCodecs[0])

    self.videoCodecOptionMenu = ctk.CTkOptionMenu(self.videoOptionFrame, command=None, variable=self.videoCodec_value, values=self.videoCodecs, font=default_font)
    self.videoCodecOptionMenu.grid(row=3, column=1, padx=10, pady=10)
    self.videoCodecOptionMenu.configure(state='disabled')


    self.videoEncoder_check_value = ctk.BooleanVar()
    self.videoEncoderCheckBox = ctk.CTkCheckBox(self.videoOptionFrame, text='VideoEncoder:', command=self.enable_videoEncoder_option, variable=self.videoEncoder_check_value, font=default_font)
    self.videoEncoderCheckBox.grid(row=4, column=0, padx=10, pady=10)

    self.videoEncoders: list = modules.utils.getEncoders.getEncoders(self, self.devices_menu.get(), forAudio=False)
    self.videoEncoder_value = ctk.StringVar()
    self.videoEncoder_value.set(self.videoEncoders[0])

    self.videoEncoderOptionMenu = ctk.CTkOptionMenu(self.videoOptionFrame, command=None, variable=self.videoEncoder_value, values=self.videoEncoders, font=default_font)
    self.videoEncoderOptionMenu.grid(row=4, column=1, padx=10, pady=10)
    self.videoEncoderOptionMenu.configure(state='disabled')


    ctk.CTkLabel(self.videoOptionFrame, text='').grid(row=5, column=0, padx=10, pady=10)
    ctk.CTkLabel(self.videoOptionFrame, text='').grid(row=6, column=0, padx=10, pady=10)
    ctk.CTkLabel(self.videoOptionFrame, text='').grid(row=7, column=0, padx=10, pady=10)





def cameraOptionFrame_func(self, master):
    self.cameraOptionFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.cameraOptionFrame.grid(row=1, column=0, padx=10, pady=10)
    ctk.CTkLabel(self.cameraOptionFrame, text='-: Camera :-', font=frame_font).grid(row=0, column=0, padx=10, pady=10)

    self.cameraAr_check_value = ctk.BooleanVar()
    self.cameraArCheckBox = ctk.CTkCheckBox(self.cameraOptionFrame, text='CameraAr:', command=self.enable_cameraAr_option, variable=self.cameraAr_check_value, font=default_font)
    self.cameraArCheckBox.grid(row=1, column=0, padx=10, pady=10)

    self.cameraArEntry = ctk.CTkEntry(self.cameraOptionFrame, width=150, font=default_font)
    self.cameraArEntry.grid(row=1, column=1, padx=10, pady=10)
    # self.cameraArEntry.insert(ctk.END, '')
    self.cameraArEntry.configure(state='disabled')


    self.cameraFps_check_value = ctk.BooleanVar()
    self.cameraFpsCheckBox = ctk.CTkCheckBox(self.cameraOptionFrame, text='CameraFps:', command=self.enable_cameraFps_option, variable=self.cameraFps_check_value, font=default_font)
    self.cameraFpsCheckBox.grid(row=2, column=0, padx=10, pady=10)

    self.cameraFpsEntry = ctk.CTkEntry(self.cameraOptionFrame, width=150, font=default_font)
    self.cameraFpsEntry.grid(row=2, column=1, padx=10, pady=10)
    self.cameraFpsEntry.insert(ctk.END, '30')
    self.cameraFpsEntry.configure(state='disabled')


    self.cameraSize_check_value = ctk.BooleanVar()
    self.cameraSizeCheckBox = ctk.CTkCheckBox(self.cameraOptionFrame, text='CameraSize:', command=self.enable_cameraSize_option, variable=self.cameraSize_check_value, font=default_font)
    self.cameraSizeCheckBox.grid(row=3, column=0, padx=10, pady=10)

    self.cameraSizeEntry = ctk.CTkEntry(self.cameraOptionFrame, width=150, font=default_font)
    self.cameraSizeEntry.grid(row=3, column=1, padx=10, pady=10)
    # self.cameraSizeEntry.insert(ctk.END, '')
    self.cameraSizeEntry.configure(state='disabled')


    self.cameraHighSpeed_check_value = ctk.BooleanVar()
    self.cameraHighSpeedCheckBox = ctk.CTkCheckBox(self.cameraOptionFrame, text='CameraHighSpeed', command=False, variable=self.cameraHighSpeed_check_value, font=default_font)
    self.cameraHighSpeedCheckBox.grid(row=4, column=0, padx=10, pady=10)

    ctk.CTkLabel(self.cameraOptionFrame, text='').grid(row=5, column=0, padx=10, pady=10)
    ctk.CTkLabel(self.cameraOptionFrame, text='').grid(row=6, column=0, padx=10, pady=10)
    ctk.CTkLabel(self.cameraOptionFrame, text='').grid(row=7, column=0, padx=10, pady=10)
    ctk.CTkLabel(self.cameraOptionFrame, text='').grid(row=8, column=0, padx=10, pady=10)
    ctk.CTkLabel(self.cameraOptionFrame, text='').grid(row=9, column=0, padx=10, pady=10)
    ctk.CTkLabel(self.cameraOptionFrame, text='').grid(row=10, column=0, padx=10, pady=10)
    ctk.CTkLabel(self.cameraOptionFrame, text='').grid(row=11, column=0, padx=10, pady=10)
    ctk.CTkLabel(self.cameraOptionFrame, text='').grid(row=12, column=0, padx=10, pady=10)



def windowOptionFrame_func(self, master):
    self.windowOptionFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.windowOptionFrame.grid(row=1, column=1, padx=10, pady=10)
    ctk.CTkLabel(self.windowOptionFrame, text='-: Window :-', font=frame_font).grid(row=0, column=0, padx=10, pady=10)


    self.windowTitle_check_value = ctk.BooleanVar()
    self.windowTitleCheckBox = ctk.CTkCheckBox(self.windowOptionFrame, text='WindowTitle:', command=self.enable_windowTitle_option, variable=self.windowTitle_check_value, font=default_font)
    self.windowTitleCheckBox.grid(row=1, column=0, padx=10, pady=10)
    
    self.windowTitleEntry = ctk.CTkEntry(self.windowOptionFrame, width=150, font=default_font)
    self.windowTitleEntry.grid(row=1, column=1, padx=10, pady=10)
    self.windowTitleEntry.insert(ctk.END, 'auto')
    self.windowTitleEntry.configure(state='disabled')


    self.windowX_check_value = ctk.BooleanVar()
    self.windowXCheckBox = ctk.CTkCheckBox(self.windowOptionFrame, text='WindowX:', command=self.enable_windowX_option, variable=self.windowX_check_value, font=default_font)
    self.windowXCheckBox.grid(row=2, column=0, padx=10, pady=10)
    
    self.windowXEntry = ctk.CTkEntry(self.windowOptionFrame, width=150, font=default_font)
    self.windowXEntry.grid(row=2, column=1, padx=10, pady=10)
    self.windowXEntry.insert(ctk.END, 'auto')
    self.windowXEntry.configure(state='disabled')


    self.windowY_check_value = ctk.BooleanVar()
    self.windowYCheckBox = ctk.CTkCheckBox(self.windowOptionFrame, text='WindowY:', command=self.enable_windowY_option, variable=self.windowY_check_value, font=default_font)
    self.windowYCheckBox.grid(row=3, column=0, padx=10, pady=10)
    
    self.windowYEntry = ctk.CTkEntry(self.windowOptionFrame, width=150, font=default_font)
    self.windowYEntry.grid(row=3, column=1, padx=10, pady=10)
    self.windowYEntry.insert(ctk.END, 'auto')
    self.windowYEntry.configure(state='disabled')


    self.windowWidth_check_value = ctk.BooleanVar()
    self.windowWidthCheckBox = ctk.CTkCheckBox(self.windowOptionFrame, text='WindowWidth:', command=self.enable_windowWidth_option, variable=self.windowWidth_check_value, font=default_font)
    self.windowWidthCheckBox.grid(row=4, column=0, padx=10, pady=10)
    
    self.windowWidthEntry = ctk.CTkEntry(self.windowOptionFrame, width=150, font=default_font)
    self.windowWidthEntry.grid(row=4, column=1, padx=10, pady=10)
    self.windowWidthEntry.insert(ctk.END, '0')
    self.windowWidthEntry.configure(state='disabled')


    self.windowHeight_check_value = ctk.BooleanVar()
    self.windowHeightCheckBox = ctk.CTkCheckBox(self.windowOptionFrame, text='WindowHeight:', command=self.enable_windowHeight_option, variable=self.windowHeight_check_value, font=default_font)
    self.windowHeightCheckBox.grid(row=5, column=0, padx=10, pady=10)
    
    self.windowHeightEntry = ctk.CTkEntry(self.windowOptionFrame, width=150, font=default_font)
    self.windowHeightEntry.grid(row=5, column=1, padx=10, pady=10)
    self.windowHeightEntry.insert(ctk.END, '0')
    self.windowHeightEntry.configure(state='disabled')


    self.newDisplay_check_value = ctk.BooleanVar()
    self.newDisplayCheckBox = ctk.CTkCheckBox(self.windowOptionFrame, text='NewDisplay:', command=self.enable_newDisplay_option, variable=self.newDisplay_check_value, font=default_font)
    self.newDisplayCheckBox.grid(row=6, column=0, padx=10, pady=10)

    self.newDisplayEntry = ctk.CTkEntry(self.windowOptionFrame, width=150, font=default_font)
    self.newDisplayEntry.grid(row=6, column=1, padx=10, pady=10)
    # self.newDisplayEntry.insert(ctk.END, '')
    self.newDisplayEntry.configure(state='disabled')


    self.maxSize_check_value = ctk.BooleanVar()
    self.maxSizeCheckBox = ctk.CTkCheckBox(self.windowOptionFrame, text='MaxSize:', command=self.enable_maxSize_option, variable=self.maxSize_check_value, font=default_font)
    self.maxSizeCheckBox.grid(row=7, column=0, padx=10, pady=10)

    self.maxSizeEntry = ctk.CTkEntry(self.windowOptionFrame, width=150, font=default_font)
    self.maxSizeEntry.grid(row=7, column=1, padx=10, pady=10)
    # self.maxSizeEntry.insert(ctk.END, '')
    self.maxSizeEntry.configure(state='disabled')


    self.crop_check_value = ctk.BooleanVar()
    self.cropCheckBox = ctk.CTkCheckBox(self.windowOptionFrame, text='Crop:', command=self.enable_crop_option, variable=self.crop_check_value, font=default_font)
    self.cropCheckBox.grid(row=8, column=0, padx=10, pady=10)

    self.cropEntry = ctk.CTkEntry(self.windowOptionFrame, width=150, font=default_font)
    self.cropEntry.grid(row=8, column=1, padx=10, pady=10)
    # self.cropEntry.insert(ctk.END, '')
    self.cropEntry.configure(state='disabled')



    self.angle_check_value = ctk.BooleanVar()
    self.angleCheckBox = ctk.CTkCheckBox(self.windowOptionFrame, text='Angle:', command=self.enable_angle_option, variable=self.angle_check_value, font=default_font)
    self.angleCheckBox.grid(row=9, column=0, padx=10, pady=10)

    self.angleEntry = ctk.CTkEntry(self.windowOptionFrame, width=150, font=default_font)
    self.angleEntry.grid(row=9, column=1, padx=10, pady=10)
    self.angleEntry.configure(state='disabled')


    self.alwaysOnTop_check_value = ctk.BooleanVar()
    self.alwaysOnTopCheckBox = ctk.CTkCheckBox(self.windowOptionFrame, text='AlwaysOnTop', command=False, variable=self.alwaysOnTop_check_value, font=default_font)
    self.alwaysOnTopCheckBox.grid(row=10, column=0, padx=10, pady=10)


    self.fullScreen_check_value = ctk.BooleanVar()
    self.fullScreenCheckBox = ctk.CTkCheckBox(self.windowOptionFrame, text='FullScreen', command=False, variable=self.fullScreen_check_value, font=default_font)
    self.fullScreenCheckBox.grid(row=11, column=0, padx=10, pady=10)


    self.windowBorderless_check_value = ctk.BooleanVar()
    self.windowBorderlessCheckBox = ctk.CTkCheckBox(self.windowOptionFrame, text='WindowBorderless', variable=self.windowBorderless_check_value, font=default_font)
    self.windowBorderlessCheckBox.grid(row=12, column=0, padx=10, pady=10)



def controlOptionFrame_func(self, master):
    self.controlOptionFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.controlOptionFrame.grid(row=2, column=0, padx=10, pady=10)
    ctk.CTkLabel(self.controlOptionFrame, text='-: Control :-', font=frame_font).grid(row=0, column=0, padx=10, pady=10)

    self.maxFps_check_value = ctk.BooleanVar()
    self.maxFpsCheckBox = ctk.CTkCheckBox(self.controlOptionFrame, text='MaxFps:', command=self.enable_maxFps_option, variable=self.maxFps_check_value, font=default_font)
    self.maxFpsCheckBox.grid(row=1, column=0, padx=10, pady=10)

    self.maxFpsEntry = ctk.CTkEntry(self.controlOptionFrame, width=150, font=default_font)
    self.maxFpsEntry.grid(row=1, column=1, padx=10, pady=10)
    self.maxFpsEntry.configure(state='disabled')


    self.shortcutMod_check_value = ctk.BooleanVar()
    self.shortcutModCheckBox = ctk.CTkCheckBox(self.controlOptionFrame, text='ShortcutMod:', command=self.enable_shortcutMod_option, variable=self.shortcutMod_check_value, font=default_font)
    self.shortcutModCheckBox.grid(row=2, column=0, padx=10, pady=10)

    self.shortcutMods: list = ["lctrl", "rctrl", "lalt", "ralt", "lsuper", "rsuper"]
    self.shortcutMod_value = ctk.StringVar()
    self.shortcutMod_value.set(self.shortcutMods[0])

    self.shortcutModOptionMenu = ctk.CTkOptionMenu(self.controlOptionFrame, command=None, variable=self.shortcutMod_value, values=self.shortcutMods, font=default_font)
    self.shortcutModOptionMenu.grid(row=2, column=1, padx=10, pady=10)
    self.shortcutModOptionMenu.configure(state='disabled')


    self.forceAdbForward_check_value = ctk.BooleanVar()
    self.forceAdbForwardCheckBox = ctk.CTkCheckBox(self.controlOptionFrame, text='ForceAdbForward', variable=self.forceAdbForward_check_value, font=default_font)
    self.forceAdbForwardCheckBox.grid(row=3, column=0, padx=10, pady=10)
    

    self.killAdbOnClose_check_value = ctk.BooleanVar()
    self.killAdbOnCloseCheckBox = ctk.CTkCheckBox(self.controlOptionFrame, text='killAdbOnClose', variable=self.killAdbOnClose_check_value, font=default_font)
    self.killAdbOnCloseCheckBox.grid(row=4, column=0, padx=10, pady=10)


    self.noKeyRepeat_check_value = ctk.BooleanVar()
    self.noKeyRepeatCheckBox = ctk.CTkCheckBox(self.controlOptionFrame, text='NoKeyRepeat', variable=self.noKeyRepeat_check_value, font=default_font)
    self.noKeyRepeatCheckBox.grid(row=5, column=0, padx=10, pady=10)


    self.rawKeyEvents_check_value = ctk.BooleanVar()
    self.rawKeyEventsCheckBox = ctk.CTkCheckBox(self.controlOptionFrame, text='RawKeyEvents', variable=self.rawKeyEvents_check_value, font=default_font)
    self.rawKeyEventsCheckBox.grid(row=6, column=0, padx=10, pady=10)


    self.legacyPaste_check_value = ctk.BooleanVar()
    self.legacyPasteCheckBox = ctk.CTkCheckBox(self.controlOptionFrame, text='LegacyPaste', variable=self.legacyPaste_check_value, font=default_font)
    self.legacyPasteCheckBox.grid(row=7, column=0, padx=10, pady=10)


    self.showTouches_check_value = ctk.BooleanVar()
    self.showTouchesCheckBox = ctk.CTkCheckBox(self.controlOptionFrame, text='ShowTouches', variable=self.showTouches_check_value, font=default_font)
    self.showTouchesCheckBox.grid(row=8, column=0, padx=10, pady=10)


    self.noMouseHover_check_value = ctk.BooleanVar()
    self.noMouseHoverCheckBox = ctk.CTkCheckBox(self.controlOptionFrame, text='NoMouseHover', variable=self.noMouseHover_check_value, font=default_font)
    self.noMouseHoverCheckBox.grid(row=9, column=0, padx=10, pady=10)
    




def powerOptionFrame_func(self, master):
    self.powerOptionFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.powerOptionFrame.grid(row=2, column=1, padx=10, pady=10)
    ctk.CTkLabel(self.powerOptionFrame, text='-: Power :-', font=frame_font).grid(row=0, column=0, padx=10, pady=10)
    
    
    self.pauseOnExit_check_value = ctk.BooleanVar()
    self.pauseOnExitCheckBox = ctk.CTkCheckBox(self.powerOptionFrame, text='PauseOnExit:', command=self.enable_pauseOnExit_option, variable=self.pauseOnExit_check_value, font=default_font)
    self.pauseOnExitCheckBox.grid(row=1, column=0, padx=10, pady=10)

    self.pauseOnExitEntry = ctk.CTkEntry(self.powerOptionFrame, width=150, font=default_font)
    self.pauseOnExitEntry.grid(row=1, column=1, padx=10, pady=10)
    self.pauseOnExitEntry.configure(state='disabled')


    self.screenOffTimeout_check_value = ctk.BooleanVar()
    self.screenOffTimeoutCheckBox = ctk.CTkCheckBox(self.powerOptionFrame, text='screenOffTimeout:', command=self.enable_screenOffTimeout_option, variable=self.screenOffTimeout_check_value, font=default_font)
    self.screenOffTimeoutCheckBox.grid(row=2, column=0, padx=10, pady=10)
    
    self.screenOffTimeoutEntry = ctk.CTkEntry(self.powerOptionFrame, width=150, font=default_font)
    self.screenOffTimeoutEntry.grid(row=2, column=1, padx=10, pady=10)
    self.screenOffTimeoutEntry.configure(state='disabled')


    self.timeLimit_check_value = ctk.BooleanVar()
    self.timeLimitCheckBox = ctk.CTkCheckBox(self.powerOptionFrame, text='TimeLimit:', command=self.enable_timeLimit_option, variable=self.timeLimit_check_value, font=default_font)
    self.timeLimitCheckBox.grid(row=3, column=0, padx=10, pady=10)
    
    self.timeLimitEntry = ctk.CTkEntry(self.powerOptionFrame, width=150, font=default_font)
    self.timeLimitEntry.grid(row=3, column=1, padx=10, pady=10)
    self.timeLimitEntry.configure(state='disabled')


    self.noPowerOn_check_value = ctk.BooleanVar()
    self.noPowerOnCheckBox = ctk.CTkCheckBox(self.powerOptionFrame, text='NoPowerOn', variable=self.noPowerOn_check_value, font=default_font)
    self.noPowerOnCheckBox.grid(row=4, column=0, padx=10, pady=10)


    self.turnScreenOff_check_value = ctk.BooleanVar()
    self.turnScreenOffCheckBox = ctk.CTkCheckBox(self.powerOptionFrame, text='turnScreenOff', variable=self.turnScreenOff_check_value, font=default_font)
    self.turnScreenOffCheckBox.grid(row=5, column=0, padx=10, pady=10)


    self.powerOffOnClose_check_value = ctk.BooleanVar()
    self.powerOffOnCloseCheckBox = ctk.CTkCheckBox(self.powerOptionFrame, text='PowerOffOnClose', variable=self.powerOffOnClose_check_value, font=default_font)
    self.powerOffOnCloseCheckBox.grid(row=6, column=0, padx=10, pady=10)


    self.disableScreenSaver_check_value = ctk.BooleanVar()
    self.disableScreenSaverCheckBox = ctk.CTkCheckBox(self.powerOptionFrame, text='DisableScreenSaver', command=False, variable=self.disableScreenSaver_check_value, font=default_font)
    self.disableScreenSaverCheckBox.grid(row=7, column=0, padx=10, pady=10)

    self.stayAwake_check_value = ctk.BooleanVar()
    self.stayAwakeCheckBox = ctk.CTkCheckBox(self.powerOptionFrame, text='StayAwake', variable=self.stayAwake_check_value, font=default_font)
    self.stayAwakeCheckBox.grid(row=8, column=0, padx=10, pady=10)

    ctk.CTkLabel(self.powerOptionFrame, text='').grid(row=9, column=0, padx=10, pady=10)



def recordOptionFrame_func(self, master):
    self.recordOptionFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.recordOptionFrame.grid(row=3, column=0, padx=10, pady=10)
    ctk.CTkLabel(self.recordOptionFrame, text='-: Record :-', font=frame_font).grid(row=0, column=0, padx=10, pady=10)


    self.record_check_value = ctk.BooleanVar()
    self.recordCheckBox = ctk.CTkCheckBox(self.recordOptionFrame, text='Record:', command=self.enable_record_option, variable=self.record_check_value, font=default_font)
    self.recordCheckBox.grid(row=1, column=0, padx=10, pady=10)
    
    self.recordEntry = ctk.CTkEntry(self.recordOptionFrame, width=150, font=default_font)
    self.recordEntry.grid(row=1, column=1, padx=10, pady=10)
    self.recordEntry.configure(state='disabled')
    

    self.recordFormats_check_value = ctk.BooleanVar()
    self.recordFormatsCheckBox = ctk.CTkCheckBox(self.recordOptionFrame, text='RecordFormats:', command=self.enable_recordFormats_option, variable=self.recordFormats_check_value, font=default_font)
    self.recordFormatsCheckBox.grid(row=2, column=0, padx=10, pady=10)

    self.recordFormats: list = ["mp4", "mkv", "m4a", "mka", "opus", "aac", "flac", "wav"]
    self.recordFormats_value = ctk.StringVar()
    self.recordFormats_value.set(self.recordFormats[0])

    self.recordFormatsOptionMenu = ctk.CTkOptionMenu(self.recordOptionFrame, command=None, variable=self.recordFormats_value, values=self.recordFormats, font=default_font)
    self.recordFormatsOptionMenu.grid(row=2, column=1, padx=10, pady=10)
    self.recordFormatsOptionMenu.configure(state='disabled')


    self.recordOrientation_check_value = ctk.BooleanVar()
    self.recordOrientationCheckBox = ctk.CTkCheckBox(self.recordOptionFrame, text='RecordOrientation:', command=self.enable_recordOrientation_option, variable=self.recordOrientation_check_value, font=default_font)
    self.recordOrientationCheckBox.grid(row=3, column=0, padx=10, pady=10)

    self.recordOrientation: list = ["0", "90", "180", "270"]
    self.recordOrientation_value = ctk.StringVar()
    self.recordOrientation_value.set(self.recordOrientation[0])

    self.recordOrientationOptionMenu = ctk.CTkOptionMenu(self.recordOptionFrame, command=None, variable=self.recordOrientation_value, values=self.recordOrientation, font=default_font)
    self.recordOrientationOptionMenu.grid(row=3, column=1, padx=10, pady=10)
    self.recordOrientationOptionMenu.configure(state='disabled')





def connectionOptionFrame_func(self, master):
    self.connectionOptionFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.connectionOptionFrame.grid(row=3, column=1, padx=10, pady=10)
    ctk.CTkLabel(self.connectionOptionFrame, text='-: Connections :-', font=frame_font).grid(row=0, column=0, padx=10, pady=10)


    self.port_check_value = ctk.BooleanVar()
    self.portCheckBox = ctk.CTkCheckBox(self.connectionOptionFrame, text='Port:', command=self.enable_port_option, variable=self.port_check_value, font=default_font)
    self.portCheckBox.grid(row=1, column=0, padx=10, pady=10)

    self.portEntry = ctk.CTkEntry(self.connectionOptionFrame, width=150, font=default_font)
    self.portEntry.grid(row=1, column=1, padx=10, pady=10)
    self.portEntry.configure(state='disabled')


    self.tunnelHost_check_value = ctk.BooleanVar()
    self.tunnelHostCheckBox = ctk.CTkCheckBox(self.connectionOptionFrame, text='TunnelHost:', command=self.enable_tunnelHost_option, variable=self.tunnelHost_check_value, font=default_font)
    self.tunnelHostCheckBox.grid(row=2, column=0, padx=10, pady=10)
    
    self.tunnelHostEntry = ctk.CTkEntry(self.connectionOptionFrame, width=150, font=default_font)
    self.tunnelHostEntry.grid(row=2, column=1, padx=10, pady=10)
    self.tunnelHostEntry.configure(state='disabled')


    self.tunnelPort_check_value = ctk.BooleanVar()
    self.tunnelPortCheckBox = ctk.CTkCheckBox(self.connectionOptionFrame, text='TunnelPort:', command=self.enable_tunnelPort_option, variable=self.tunnelPort_check_value, font=default_font)
    self.tunnelPortCheckBox.grid(row=3, column=0, padx=10, pady=10)
    
    self.tunnelPortEntry = ctk.CTkEntry(self.connectionOptionFrame, width=150, font=default_font)
    self.tunnelPortEntry.grid(row=3, column=1, padx=10, pady=10)
    self.tunnelPortEntry.configure(state='disabled')



def virtualDisplayOptionFrame_func(self, master):
    self.virtualDisplayOptionFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.virtualDisplayOptionFrame.grid(row=4, column=0, padx=10, pady=10)
    ctk.CTkLabel(self.virtualDisplayOptionFrame, text='-: VirtualDisplay :-', font=frame_font).grid(row=0, column=0, padx=10, pady=10)


    self.noVdDestroyContent_check_value = ctk.BooleanVar()
    self.noVdDestroyContentCheckBox = ctk.CTkCheckBox(self.virtualDisplayOptionFrame, text='NoVdDestroyContent', variable=self.noVdDestroyContent_check_value, font=default_font)
    self.noVdDestroyContentCheckBox.grid(row=1, column=0, padx=10, pady=10)

    self.noVdSystemDecorations_check_value = ctk.BooleanVar()
    self.noVdSystemDecorationsCheckBox = ctk.CTkCheckBox(self.virtualDisplayOptionFrame, text='NoVdSystemDecorations', variable=self.noVdSystemDecorations_check_value, font=default_font)
    self.noVdSystemDecorationsCheckBox.grid(row=2, column=0, padx=10, pady=10)




def v4l2OptionFrame_func(self, master):
    self.v4l2OptionFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.v4l2OptionFrame.grid(row=4, column=1, padx=10, pady=10)
    ctk.CTkLabel(self.v4l2OptionFrame, text='-: V4l2 :-', font=frame_font).grid(row=0, column=0, padx=10, pady=10)

    self.v4l2Sink_check_value = ctk.BooleanVar()
    self.v4l2SinkCheckBox = ctk.CTkCheckBox(self.v4l2OptionFrame, text='V4l2Sink:', command=self.enable_v4l2Sink_option, variable=self.v4l2Sink_check_value, font=default_font)
    self.v4l2SinkCheckBox.grid(row=1, column=0, padx=10, pady=10)
    
    self.v4l2SinkEntry = ctk.CTkEntry(self.v4l2OptionFrame, width=150, font=default_font)
    self.v4l2SinkEntry.grid(row=1, column=1, padx=10, pady=10)
    self.v4l2SinkEntry.insert(ctk.END, '/dev/video0')
    self.v4l2SinkEntry.configure(state='disabled')


    self.v4l2Buffer_check_value = ctk.BooleanVar()
    self.v4l2BufferCheckBox = ctk.CTkCheckBox(self.v4l2OptionFrame, text='V4l2Buffer:', command=self.enable_v4l2Buffer_option, variable=self.v4l2Buffer_check_value, font=default_font)
    self.v4l2BufferCheckBox.grid(row=2, column=0, padx=10, pady=10)
    
    self.v4l2BufferEntry = ctk.CTkEntry(self.v4l2OptionFrame, width=150, font=default_font)
    self.v4l2BufferEntry.grid(row=2, column=1, padx=10, pady=10)
    self.v4l2BufferEntry.insert(ctk.END, '0')
    self.v4l2BufferEntry.configure(state='disabled')



def renderDriversOptionFrame_func(self, master):
    self.renderDriverOptionFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.renderDriverOptionFrame.grid(row=5, column=0, padx=10, pady=10)
    ctk.CTkLabel(self.renderDriverOptionFrame, text='-: RenderDrivers :-', font=frame_font).grid(row=0, column=0, padx=10, pady=10)


    self.renderDriver_check_value = ctk.BooleanVar()
    self.renderDriverCheckBox = ctk.CTkCheckBox(self.renderDriverOptionFrame, text='RenderDriver:', command=self.enable_renderDriver_option, variable=self.renderDriver_check_value, font=default_font)
    self.renderDriverCheckBox.grid(row=1, column=0, padx=10, pady=10)

    self.renderDrivers: list = ["direct3d", "opengl", "opengles2", "opengles", "metal", "software"]
    self.renderDriver_value = ctk.StringVar()
    self.renderDriver_value.set(self.renderDrivers[0])

    self.renderDriverOptionMenu = ctk.CTkOptionMenu(self.renderDriverOptionFrame, command=None, variable=self.renderDriver_value, values=self.renderDrivers, font=default_font)
    self.renderDriverOptionMenu.grid(row=1, column=1, padx=10, pady=10)
    self.renderDriverOptionMenu.configure(state='disabled')



def appOptionFrame_func(self, master):
    self.appOptionFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.appOptionFrame.grid(row=5, column=1, padx=10, pady=10)
    ctk.CTkLabel(self.appOptionFrame, text='-: Apps :-', font=frame_font).grid(row=0, column=0, padx=10, pady=10)


    self.startApp_check_value = ctk.BooleanVar()
    self.startAppCheckBox = ctk.CTkCheckBox(self.appOptionFrame, text='StartApp:', command=self.enable_startApp_option, variable=self.startApp_check_value, font=default_font)
    self.startAppCheckBox.grid(row=1, column=0, padx=10, pady=10)
    
    self.startAppEntry = ctk.CTkEntry(self.appOptionFrame, width=150, font=default_font)
    self.startAppEntry.grid(row=1, column=1, padx=10, pady=10)
    self.startAppEntry.configure(state='disabled')



def otherOptionFrame_func(self, master):
    self.otherOptionFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.otherOptionFrame.grid(row=6, column=0, padx=10, pady=10)
    ctk.CTkLabel(self.otherOptionFrame, text='-: Others :-', font=frame_font).grid(row=0, column=0, padx=10, pady=10)


    self.pushTarget_check_value = ctk.BooleanVar()
    self.pushTargetCheckBox = ctk.CTkCheckBox(self.otherOptionFrame, text='PushTarget:', command=self.enable_pushTarget_option, variable=self.pushTarget_check_value, font=default_font)
    self.pushTargetCheckBox.grid(row=1, column=0, padx=10, pady=10)
    
    self.pushTargetEntry = ctk.CTkEntry(self.otherOptionFrame, width=150, font=default_font)
    self.pushTargetEntry.grid(row=1, column=1, padx=10, pady=10)
    self.pushTargetEntry.insert(ctk.END, '/sdcard/Download')
    self.pushTargetEntry.configure(state='disabled')


    self.captureOrientation_check_value = ctk.BooleanVar()
    self.captureOrientationCheckBox = ctk.CTkCheckBox(self.otherOptionFrame, text='CaptureOrientation:', command=self.enable_captureOrientation_option, variable=self.captureOrientation_check_value, font=default_font)
    self.captureOrientationCheckBox.grid(row=2, column=0, padx=10, pady=10)

    self.captureOrientationEntry = ctk.CTkEntry(self.otherOptionFrame, width=150, font=default_font)
    self.captureOrientationEntry.grid(row=2, column=1, padx=10, pady=10)
    # self.captureOrientationEntry.insert(ctk.END, '')
    self.captureOrientationEntry.configure(state='disabled')


    self.noCleanUp_check_value = ctk.BooleanVar()
    self.noCleanUpCheckBox = ctk.CTkCheckBox(self.otherOptionFrame, text='NoCleanUp', variable=self.noCleanUp_check_value, font=default_font)
    self.noCleanUpCheckBox.grid(row=3, column=0, padx=10, pady=10)

    self.noClipboardAutoSync_check_value = ctk.BooleanVar()
    self.noClipboardAutoSyncCheckBox = ctk.CTkCheckBox(self.otherOptionFrame, text='NoClipboardAutoSync', variable=self.noClipboardAutoSync_check_value, font=default_font)
    self.noClipboardAutoSyncCheckBox.grid(row=4, column=0, padx=10, pady=10)


    self.noDownsizeOnError_check_value = ctk.BooleanVar()
    self.noDownsizeOnErrorCheckBox = ctk.CTkCheckBox(self.otherOptionFrame, text='NoDownsizeOnError', variable=self.noDownsizeOnError_check_value, font=default_font)
    self.noDownsizeOnErrorCheckBox.grid(row=5, column=0, padx=10, pady=10)

    self.noMipMaps_check_value = ctk.BooleanVar()
    self.noMipMapsCheckBox = ctk.CTkCheckBox(self.otherOptionFrame, text='NoMipMaps', variable=self.noMipMaps_check_value, font=default_font)
    self.noMipMapsCheckBox.grid(row=6, column=0, padx=10, pady=10)


    self.printFps_check_value = ctk.BooleanVar()
    self.printFpsCheckBox = ctk.CTkCheckBox(self.otherOptionFrame, text='PrintFps', variable=self.printFps_check_value, font=default_font)
    self.printFpsCheckBox.grid(row=7, column=0, padx=10, pady=10)


    self.preferText_check_value = ctk.BooleanVar()
    self.preferTextCheckBox = ctk.CTkCheckBox(self.otherOptionFrame, text='PreferText', variable=self.preferText_check_value, font=default_font)
    self.preferTextCheckBox.grid(row=8, column=0, padx=10, pady=10)


    self.requireAudio_check_value = ctk.BooleanVar()
    self.requireAudioCheckBox = ctk.CTkCheckBox(self.otherOptionFrame, text='RequireAudio', variable=self.requireAudio_check_value, font=default_font)
    self.requireAudioCheckBox.grid(row=9, column=0, padx=10, pady=10)








def advanched_widgets_options(self):
    self.advanchedWindow_frame = ctk.CTkScrollableFrame(self.advanchedPopUpWindow, border_color='black', border_width=3, height=500, width=900)
    self.advanchedWindow_frame.pack(padx=10, pady=10)

    audioOptionFrame_func(self, self.advanchedWindow_frame)
    
    videoOptionFrame_func(self, self.advanchedWindow_frame)

    cameraOptionFrame_func(self, self.advanchedWindow_frame)

    windowOptionFrame_func(self, self.advanchedWindow_frame)

    controlOptionFrame_func(self, self.advanchedWindow_frame)

    powerOptionFrame_func(self, self.advanchedWindow_frame)
    
    recordOptionFrame_func(self, self.advanchedWindow_frame)

    connectionOptionFrame_func(self, self.advanchedWindow_frame)

    virtualDisplayOptionFrame_func(self, self.advanchedWindow_frame)

    v4l2OptionFrame_func(self, self.advanchedWindow_frame)

    renderDriversOptionFrame_func(self, self.advanchedWindow_frame)

    appOptionFrame_func(self, self.advanchedWindow_frame)

    otherOptionFrame_func(self, self.advanchedWindow_frame)










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

def enable_pushTarget_option(self):
    if self.pushTarget_check_value.get():
        self.pushTargetEntry.configure(state='normal')
    else:
        self.pushTargetEntry.configure(state='disabled')

def enable_record_option(self):
    if self.record_check_value.get():
        self.recordEntry.configure(state='normal')
    else:
        self.recordEntry.configure(state='disabled')

def enable_recordFormats_option(self):
    if self.recordFormats_check_value.get():
        self.recordFormatsOptionMenu.configure(state='normal')
    else:
        self.recordFormatsOptionMenu.configure(state='disabled')

def enable_recordOrientation_option(self):
    if self.recordOrientation_check_value.get():
        self.recordOrientationOptionMenu.configure(state='normal')
    else:
        self.recordOrientationOptionMenu.configure(state='disabled')

def enable_renderDriver_option(self):
    if self.renderDriver_check_value.get():
        self.renderDriverOptionMenu.configure(state='normal')
    else:
        self.renderDriverOptionMenu.configure(state='disabled')

def enable_screenOffTimeout_option(self):
    if self.screenOffTimeout_check_value.get():
        self.screenOffTimeoutEntry.configure(state='normal')
    else:
        self.screenOffTimeoutEntry.configure(state='disabled')

def enable_shortcutMod_option(self):
    if self.shortcutMod_check_value.get():
        self.shortcutModOptionMenu.configure(state='normal')
    else:
        self.shortcutModOptionMenu.configure(state='disabled')

def enable_startApp_option(self):
    if self.startApp_check_value.get():
        self.startAppEntry.configure(state='normal')
    else:
        self.startAppEntry.configure(state='disabled')

def enable_timeLimit_option(self):
    if self.timeLimit_check_value.get():
        self.timeLimitEntry.configure(state='normal')
    else:
        self.timeLimitEntry.configure(state='disabled')

def enable_tunnelHost_option(self):
    if self.tunnelHost_check_value.get():
        self.tunnelHostEntry.configure(state='normal')
    else:
        self.tunnelHostEntry.configure(state='disabled')

def enable_tunnelPort_option(self):
    if self.tunnelPort_check_value.get():
        self.tunnelPortEntry.configure(state='normal')
    else:
        self.tunnelPortEntry.configure(state='disabled')

def enable_v4l2Sink_option(self):
    if self.v4l2Sink_check_value.get():
        self.v4l2SinkEntry.configure(state='normal')
    else:
        self.v4l2SinkEntry.configure(state='disabled')

def enable_v4l2Buffer_option(self):
    if self.v4l2Buffer_check_value.get():
        self.v4l2BufferEntry.configure(state='normal')
    else:
        self.v4l2BufferEntry.configure(state='disabled')

def enable_videoCodec_option(self):
    if self.videoCodec_check_value.get():
        self.videoCodecOptionMenu.configure(state='normal')
    else:
        self.videoCodecOptionMenu.configure(state='disabled')

def enable_videoBuffer_option(self):
    if self.videoBuffer_check_value.get():
        self.videoBufferEntry.configure(state='normal')
    else:
        self.videoBufferEntry.configure(state='disabled')

def enable_videoEncoder_option(self):
    if self.videoEncoder_check_value.get():
        self.videoEncoderOptionMenu.configure(state='normal')
    else:
        self.videoEncoderOptionMenu.configure(state='disabled')

def enable_windowTitle_option(self):
    if self.windowTitle_check_value.get():
        self.windowTitleEntry.configure(state='normal')
    else:
        self.windowTitleEntry.configure(state='disabled')

def enable_windowX_option(self):
    if self.windowX_check_value.get():
        self.windowXEntry.configure(state='normal')
    else:
        self.windowXEntry.configure(state='disabled')

def enable_windowY_option(self):
    if self.windowY_check_value.get():
        self.windowYEntry.configure(state='normal')
    else:
        self.windowYEntry.configure(state='disabled')

def enable_windowWidth_option(self):
    if self.windowWidth_check_value.get():
        self.windowWidthEntry.configure(state='normal')
    else:
        self.windowWidthEntry.configure(state='disabled')

def enable_windowHeight_option(self):
    if self.windowHeight_check_value.get():
        self.windowHeightEntry.configure(state='normal')
    else:
        self.windowHeightEntry.configure(state='disabled')