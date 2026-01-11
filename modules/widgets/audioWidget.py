import customtkinter as ctk
from modules.themes.themes import default_font


def audioCheck(self):
    self.audioFrame = ctk.CTkFrame(self.middleFrame, border_color='black', border_width=3)
    self.audioFrame.pack(side=ctk.LEFT, anchor='ne', padx=10, pady=10)
    
    self.audio_check_value = ctk.BooleanVar()
    self.audioCheckBox = ctk.CTkCheckBox(self.audioFrame, text='Audio', command=self.audio_widget, variable=self.audio_check_value, font=default_font)
    self.audioCheckBox.grid(row=0, column=0, padx=10, pady=10)
    

def audio_widget(self):
    if not self.audio_check_value.get():
        self.audioCheckBox.configure(text='Audio')
        
        # self.audioSourceLabel.destroy()
        self.audioSourceCheckBox.destroy()
        self.audioSourceMode_menu.destroy()

        self.noAudioPlaybackCheckBox.destroy()

        self.noAudioForwardingCheckBox.destroy()
        return

    self.audioCheckBox.configure(text='Audio:')

    # self.audioSourceLabel = ctk.CTkLabel(self.audioFrame, text='AudioSource:', font=default_font)
    # self.audioSourceLabel.grid(row=0, column=1, padx=8, pady=8)

    self.audioSource_check_value = ctk.BooleanVar()
    self.audioSourceCheckBox = ctk.CTkCheckBox(self.audioFrame, text='AudioSource:', command=self.enable_audioSource_option, variable=self.audioSource_check_value, font=default_font)
    self.audioSourceCheckBox.grid(row=0, column=1, padx=10, pady=10)
    
    self.audioSourceModes: list = ["output", "playback", "mic", "mic-unprocessed", "mic-camcorder", "mic-voice-recognition", "mic-voice-communication", "voice-call", "voice-call-uplink", "voice-call-downlink", "voice-performance"]
    self.audioSourceMode_value = ctk.StringVar()
    self.audioSourceMode_value.set(self.audioSourceModes[0])

    self.audioSourceMode_menu = ctk.CTkOptionMenu(self.audioFrame, variable=self.audioSourceMode_value, values=self.audioSourceModes, font=default_font)
    self.audioSourceMode_menu.grid(row=0, column=2, padx=8, pady=8)
    self.audioSourceMode_menu.configure(state='disabled')

    self.noAudioPlayback_check_value = ctk.BooleanVar()
    self.noAudioPlaybackCheckBox = ctk.CTkCheckBox(self.audioFrame, text='NoAudioPlayback', command=self.enable_noAudioPlayback_option, variable=self.noAudioPlayback_check_value, font=default_font)
    self.noAudioPlaybackCheckBox.grid(row=0, column=3, padx=8, pady=8)

    self.noAudioForwarding_check_value = ctk.BooleanVar()
    self.noAudioForwardingCheckBox = ctk.CTkCheckBox(self.audioFrame, text='NoAudioForwarding', command=None, variable=self.noAudioForwarding_check_value, font=default_font)
    self.noAudioForwardingCheckBox.grid(row=0, column=4, padx=8, pady=8)

    # IDEA:
    """
        when user ticks another widget on the main window, the others ones will be closed automaticly, but their values will be saved in a variable which will later be accessed.
        Ex:
        when destroying all the widgets in InputsWidget it will save a variable with the values of InputsWidget options like self.otg_check_value.get() ==> 1 or and then when the user clicks on that InputsWidget the values will be automaticly set to those options which it belongs to
    """

def enable_audioSource_option(self):
    if self.audioSource_check_value.get():
        self.audioSourceMode_menu.configure(state='normal')
        self.noAudioPlayback_check_value.set(0)
    else:
        self.audioSourceMode_menu.configure(state='disabled')

def enable_noAudioPlayback_option(self):
    if self.noAudioPlayback_check_value.get():
        self.audioSourceMode_menu.configure(state='disabled')
        self.audioSource_check_value.set(0)
        self.audioSourceCheckBox.configure(state='disabled')
    else:
        self.audioSourceCheckBox.configure(state='normal')
