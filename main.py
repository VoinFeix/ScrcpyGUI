
import customtkinter as ctk

from modules.widgets import startWidget
from modules.widgets import mainFrames
# from modules.widgets import cameraWidget
from modules.widgets import devicesWidget
from modules.widgets import inputsWidget
from modules.widgets import audioWidget
from modules.widgets import videoWidget

from modules.utils import checkPkgs
from modules.utils import runScrcpy

from modules.logging import Logs

HEIGHT = 1200
WIDTH = 800
GEOMETRY = f'{HEIGHT}x{WIDTH}'

checkPkgs.checkPkgs()

logs = Logs()

class ScrcpyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('ScrcpyGUI')
        self.root.geometry(GEOMETRY)
        # self.root.resizable(False, False)
        ctk.set_appearance_mode('dark')
        
        # Main Frame
        mainFrames.mainFrames(self)

        # Devices Widget
        devicesWidget.devicesWidget(self)

        # Inputs Widget
        inputsWidget.inputsCheck(self)

        # Audio Widget
        audioWidget.audioCheck(self)

        # # Video Widget
        videoWidget.videoCheck(self)

        # Camera Widget
        # cameraWidget.cameraCheck(self)


        # Start Widget
        startWidget.startCheck(self)

    def input_widget(self):
        inputsWidget.input_widget(self)
    
    def audio_widget(self):
        audioWidget.audio_widget(self)
    
    def video_widget(self):
        videoWidget.video_widget(self)

    def camera_widget(self, *args):
        videoWidget.camera_widget(self, *args)

    def start_widget(self):
        startWidget.start_widget(self)

    def get_devices_list(self):
        devicesWidget.get_devices_list(self)

    def enable_otg(self):
        inputsWidget.enable_otg(self)

    def enable_keyboard_option(self):
        inputsWidget.enable_keyboard_option(self)

    def enable_mouse_option(self):
        inputsWidget.enable_mouse_option(self)

    def enable_gamepad_option(self):
        inputsWidget.enable_gamepad_option(self)          

    def enable_noControl_option(self):
        inputsWidget.enable_noControl_option(self)

    def enable_videoSource_option(self):
        videoWidget.enable_videoSource_option(self)

    def enable_noVideoPlayback_option(self):
        videoWidget.enable_noVideoPlayback_option(self)

    def enable_audioSource_option(self):
        audioWidget.enable_audioSource_option(self)

    def enable_noAudioPlayback_option(self):
        audioWidget.enable_noAudioPlayback_option(self)

    def enable_cameraID_option(self):
        videoWidget.enable_cameraID_option(self)

    def enable_cameraFacing_option(self):
        videoWidget.enable_cameraFacing_option(self)

    def update_everything(self):
        devicesWidget.update_everything(self)

    def runScrcpy(self):
        runScrcpy.runScrcpy(self)

    def stopScrcpy(self):
        runScrcpy.stopScrcpy(self)

    def exitScrcpy_func(self):
        self.stopScrcpy()
        self.root.quit()

if __name__ == '__main__':
    root = ctk.CTk()
    app = ScrcpyGUI(root)
    root.mainloop()