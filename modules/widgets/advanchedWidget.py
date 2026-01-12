import customtkinter as ctk
import tkinter as tk
from modules.themes.themes import default_font, heading_font

ADVANCHED_WINDOW_NAME = 'Advanched Options'
ADVANCHED_WINDOW_GEOMETRY = '600x600'

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

# def enable_advanched_widgets_options(self):
#     enable_angle_option(self)

# def enable_angle_option(self):
#     if not self.angle_check_value.get():
#         try:
#             self.angleLabel.destroy()
#             self.angleEntry.destroy()
#         except Exception as e:
#             print(f'Error on enable_angle_option,\n{str(e)}')

#         return
    
#     self.angleFrame = ctk.CTkFrame(self.advanchedWindow_frame, border_color='white', border_width=3,)
#     self.angleFrame.grid(row=0, column=2, padx=5, pady=5)

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

