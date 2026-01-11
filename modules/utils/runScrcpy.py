import subprocess
import threading

command = None
def runProcess(device, otg, keyboard, mouse, gamepad, noControl, audioSource, noAudioForwarding, noAudioPlayback, videoSource, noVideoForwarding, cameraID, cameraFacing, noVideoPlayback):
    global command
    
    mainCmd: list = ['scrcpy', '-s', device]

    # Input Frame Values
    if noControl:
        otg = keyboard = mouse = gamepad = None
    else:
        if otg:
            keyboard = mouse = None
            otgCmd: list = ['--otg']
            mainCmd += otgCmd
        else:
            otg = None
            if keyboard is not None:
                keyboardCmd: list = [f'--keyboard={keyboard}']
                mainCmd += keyboardCmd
            if mouse is not None:
                mouseCmd: list = [f'--mouse={mouse}']
                mainCmd += mouseCmd

        if gamepad is not None:
            gamepadCmd: list = [f'--gamepad={gamepad}']
            mainCmd += gamepadCmd    
    
    # Audio Frame values
    if noAudioPlayback:
        noAudioPlaybackCmd: list = ['--no-audio-playback']
        mainCmd += noAudioPlaybackCmd
        
    else:
        if noAudioForwarding:
            noAudioForwardingCmd: list = ['--no-audio']
            mainCmd += noAudioForwardingCmd
        if audioSource is not None:
            audioSourceCmd: list = [f'--audio-source={audioSource}']
            mainCmd += audioSourceCmd

    # Video Frame Values
    if noVideoPlayback:
        noVideoPlaybackCmd: list = []
        mainCmd += noVideoPlaybackCmd
    else:
        if noVideoForwarding:
            noVideoForwardingCmd: list = ['--no-video']
            mainCmd += noVideoForwardingCmd
            
        if videoSource is not None:
            videoSourceCmd: list = [f'--video-source={videoSource}']
            mainCmd += videoSourceCmd
        if videoSource == 'camera':
            if cameraID is not None:
                cameraIDCmd: list = [f'--camera-id={cameraID}']
                mainCmd += cameraIDCmd
            if cameraFacing is not None:
                cameraFacing: list = [f'--camera-facing={cameraFacing}']
                mainCmd += cameraFacing

    print(f'Main Command: {mainCmd}')
    command = subprocess.Popen(mainCmd, text=False)

def start_runProcess_thread(device, otg, keyboard, mouse, gamepad, noControl, audioSource, noAudioForwarding, noAudioPlayback, videoSource, noVideoForwarding, cameraID, cameraFacing, noVideoPlayback):
    thread = threading.Thread(target=runProcess, args=(device, otg, keyboard, mouse, gamepad, noControl, audioSource, noAudioForwarding, noAudioPlayback, videoSource, noVideoForwarding, cameraID, cameraFacing, noVideoPlayback,))
    thread.start()

def stopScrcpy(self):
    try:
        global command
        command.terminate()
        
    except Exception as e:
        print(f'Error on stopScrcpy function\n{str(e)}')
        self.root.quit()

def runScrcpy(self):
    if self.devices_menu.get():
        device = self.devices_menu.get()
        print(f'\nDevice: {device}')
    else:
        print('No Device selected!!')
        return

    otg = None
    keyboard = None
    mouse = None
    gamepad = None
    noControl = False

    if self.input_check_value.get():
        try:
            if self.no_control_check_value.get():
                noControl = True
            elif self.otg_check_value.get():
                otg = self.otg_check_value.get()
            else:
                if self.keyboard_check_value.get():
                    keyboard = self.keyboardMode_value.get()
                if self.mouse_check_value.get():
                    mouse = self.mouseMode_value.get()

            if self.gamepad_check_value.get():
                gamepad = self.gamepadMode_value.get()

            print('\nInput Frame values:')
            print(f'OTG: {otg}')
            print(f'Keyboard: {keyboard}\nMouse: {mouse}')
            print(f'Gamepad: {gamepad}')

        except Exception as e:
            print(f'Error collecting values from input frame\n{str(e)}')


    audioSource = None
    noAudioForwarding = None   
    noAudioPlayback = False
    if self.audio_check_value.get():
        try:
            if self.noAudioPlayback_check_value.get():
                noAudioPlayback = True
            else:
                if self.audioSource_check_value.get():
                    audioSource = self.audioSourceMode_menu.get()
            
            noAudioForwarding = self.noAudioForwarding_check_value.get()

            print('\nAudio Frame values:')
            print(f'AudioSource: {audioSource}')
            print(f'NoAudioForwarding: {noAudioForwarding}')

        except Exception as e:
            print(f'Error collecting values from the audio frame\n{str(e)}')

    videoSource = None
    noVideoForwarding = None
    cameraID = None
    cameraFacing = None
    noVideoPlayback = False
    if self.video_check_value.get():
        try:
            if self.noVideoPlayback_check_value.get():
                noVideoPlayback = True
            else:
                if self.videoSource_check_value.get():
                    videoSource = self.videoSourceMode_menu.get()

                    if videoSource == 'camera':
                        if self.cameraID_check_value.get():
                            cameraID = self.cameraID_menu.get()

                        if self.cameraFacing_check_value.get():
                            cameraFacing = self.cameraFacing_menu.get()

            noVideoForwarding = self.noVideoForwarding_check_value.get()

            print('\nVideo Frame Values:')
            print(f'VideoSource: {videoSource}')
            print(f'NoVideoForwarding: {noVideoForwarding}')
            print(f'CameraID: {cameraID}')
            print(f'CameraFacing: {cameraFacing}')
        except Exception as e:
            print(f'Error collecting values from the video frame\n{str(e)}')


    start_runProcess_thread(
        device=device,
        otg=otg,
        keyboard=keyboard,
        mouse=mouse,
        gamepad=gamepad,
        noControl=noControl,
        audioSource=audioSource,
        noAudioForwarding=noAudioForwarding,
        noAudioPlayback=noAudioPlayback,
        videoSource=videoSource,
        noVideoForwarding=noVideoForwarding,
        cameraID=cameraID,
        cameraFacing=cameraFacing,
        noVideoPlayback=noVideoPlayback
    )


    return