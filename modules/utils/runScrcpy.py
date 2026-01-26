import subprocess
import threading

def getAudioOptionFrameValues(self):
    
    audioBitRate = None
    if self.audioBitRate_check_value.get():
        audioBitRate = self.audioBitRateEntry.get()

    audioBuffer = None
    if self.audioBuffer_check_value.get():
        audioBuffer = self.audioBufferEntry.get()

    audioOutputBuffer = None
    if self.audioOutputBuffer_check_value.get():
        audioOutputBuffer = self.audioOutputBufferEntry.get()
    
    audioCodec = None
    if self.audioCodec_check_value.get():
        audioCodec = self.audioCodec_value.get()
    
    audioEncoder = None
    if self.audioEncoder_check_value.get():
        audioEncoder = self.audioEncoder_value.get()

    audioDup = None
    if self.audioDup_check_value.get():
        audioDup = self.audioDup_check_value.get()

    return audioBitRate, audioBuffer, audioOutputBuffer, audioCodec, audioEncoder, audioDup


def getVideoOptionFrameValues(self):

    videoBitRate = None
    if self.videoBitRate_check_value.get():
        videoBitRate = self.videoBitRateEntry.get()

    videoBuffer = None
    if self.videoBuffer_check_value.get():
        videoBuffer = self.videoBufferEntry.get()

    videoCodec = None
    if self.videoCodec_check_value.get():
        videoCodec = self.videoCodec_value.get()

    videoEncoder = None
    if self.videoEncoder_check_value.get():
        videoEncoder = self.videoEncoder_value.get()
    
    return videoBitRate, videoBuffer, videoCodec, videoEncoder


def getCameraOptionFrameValues(self):
    cameraAr = None
    if self.cameraAr_check_value.get():
        cameraAr = self.cameraArEntry.get()

    cameraFps = None
    if self.cameraFps_check_value.get():
        cameraFps = self.cameraFpsEntry.get()

    cameraSize = None
    if self.cameraSize_check_value.get():
        cameraSize = self.cameraSizeEntry.get()
    
    cameraHighSpeed = None
    if self.cameraHighSpeed_check_value.get():
        cameraHighSpeed = self.cameraHighSpeed_check_value.get()

    return cameraAr, cameraFps, cameraSize, cameraHighSpeed


def getWindowOptionFrameValues(self):
    windowTitle = None
    if self.windowTitle_check_value.get():
        windowTitle = self.windowTitleEntry.get()

    windowX = None
    if self.windowX_check_value.get():
        windowX = self.windowXEntry.get()
    
    windowY = None
    if self.windowY_check_value.get():
        windowY = self.windowYEntry.get()

    windowWidth = None
    if self.windowWidth_check_value.get():
        windowWidth = self.windowWidthEntry.get()

    windowHeight = None
    if self.windowHeight_check_value.get():
        windowHeight = self.windowHeightEntry.get()

    newDisplay = None
    if self.newDisplay_check_value.get():
        newDisplay = self.newDisplayEntry.get()

    maxSize = None
    if self.maxSize_check_value.get():
        maxSize = self.maxSizeEntry.get()
    
    crop = None
    if self.crop_check_value.get():
        crop = self.cropEntry.get()

    angle = None
    if self.angle_check_value.get():
        angle = self.angleEntry.get()
    
    alwaysOnTop = None
    if self.alwaysOnTop_check_value.get():
        alwaysOnTop = self.alwaysOnTop_check_value.get()

    fullScreen = None
    if self.fullScreen_check_value.get():
        fullScreen = self.fullScreen_check_value.get()
    
    windowBorderless = None
    if self.windowBorderless_check_value.get():
        windowBorderless = self.windowBorderless_check_value.get()
    
    return windowTitle, windowX, windowY, windowWidth, windowHeight, newDisplay, maxSize, crop, angle, alwaysOnTop, fullScreen, windowBorderless


def getControlOptionFrameValues(self):

    maxFps = None
    if self.maxFps_check_value.get():
        maxFps = self.maxFpsEntry.get()

    shortCutMod = None
    if self.shortcutMod_check_value.get():
        shortCutMod = self.shortcutMod_value.get()

    forceAdbForward = None
    if self.forceAdbForward_check_value.get():
        forceAdbForward = self.forceAdbForward_check_value.get()

    killAdbOnClose = None
    if self.killAdbOnClose_check_value.get():
        killAdbOnClose = self.killAdbOnClose_check_value.get()

    noKeyRepeat = None
    if self.noKeyRepeat_check_value.get():
        noKeyRepeat = self.noKeyRepeat_check_value.get()

    rawKeyEvents = None
    if self.rawKeyEvents_check_value.get():
        rawKeyEvents = self.rawKeyEvents_check_value.get()

    legacyPaste = None
    if self.legacyPaste_check_value.get():
        legacyPaste = self.legacyPaste_check_value.get()

    showTouches = None
    if self.showTouches_check_value.get():
        showTouches = self.showTouches_check_value.get()

    noMouseHover = None
    if self.noMouseHover_check_value.get():
        noMouseHover = self.noMouseHover_check_value.get()
    
    return maxFps, shortCutMod, forceAdbForward, killAdbOnClose, noKeyRepeat, rawKeyEvents, legacyPaste, showTouches, noMouseHover


def getPowerOptionFrameValues(self):
    pauseOnExit = None
    if self.pauseOnExit_check_value.get():
        pauseOnExit = self.pauseOnExitEntry.get()

    screenOffTimeout = None
    if self.screenOffTimeout_check_value.get():
        screenOffTimeout = self.screenOffTimeoutEntry.get()

    timeLimit = None
    if self.timeLimit_check_value.get():
        timeLimit = self.timeLimitEntry.get()

    noPowerOn = None
    if self.noPowerOn_check_value.get():
        noPowerOn = self.noPowerOn_check_value.get()

    turnScreenOff = None
    if self.turnScreenOff_check_value.get():
        turnScreenOff = self.turnScreenOff_check_value.get()

    powerOffOnClose = None
    if self.powerOffOnClose_check_value.get():
        powerOffOnClose = self.powerOffOnClose_check_value.get()

    disableScreenSaver = None
    if self.disableScreenSaver_check_value.get():
        disableScreenSaver = self.disableScreenSaver_check_value.get()

    stayAwake = None
    if self.stayAwake_check_value.get():
        stayAwake = self.stayAwake_check_value.get()


    return pauseOnExit, screenOffTimeout, timeLimit, noPowerOn, turnScreenOff, powerOffOnClose, disableScreenSaver, stayAwake


def getRecordOptionFrameValues(self):
    record = None
    if self.record_check_value.get():
        record = self.recordEntry.get()

    recordFormats = None
    if self.recordFormats_check_value.get():
        recordFormats = self.recordFormats_value.get()

    recordOrientation = None
    if self.recordOrientation_check_value.get():
        recordOrientation = self.recordOrientation_value.get()

    return record, recordFormats, recordOrientation


def getConnectionsOptionFrameValues(self):
    port = None
    if self.port_check_value.get():
        port = self.portEntry.get()

    tunnelHost = None
    if self.tunnelHost_check_value.get():
        tunnelHost = self.tunnelHostEntry.get()

    tunnelPort = None
    if self.tunnelPort_check_value.get():
        tunnelPort = self.tunnelPortEntry.get()

    return port, tunnelHost, tunnelPort


def getVirtualDisplayOptionFrameValues(self):
    
    noVdDestroyContent = None
    if self.noVdDestroyContent_check_value.get():
        noVdDestroyContent = self.noVdDestroyContent_check_value.get()

    noVdSystemDecorations = None
    if self.noVdSystemDecorations_check_value.get():
        noVdSystemDecorations = self.noVdSystemDecorations_check_value.get()
    
    return noVdDestroyContent, noVdSystemDecorations

def getV4l2OptionFrameValues(self):
    v4l2Sink = None
    if self.v4l2Sink_check_value.get():
        v4l2Sink = self.v4l2SinkEntry.get()

    v4l2Buffer = None
    if self.v4l2Buffer_check_value.get():
        v4l2Buffer = self.v4l2BufferEntry.get()

    return v4l2Sink, v4l2Buffer

def getRenderDriversOptionFrameValues(self):
    renderDriver = None
    if self.renderDriver_check_value.get():
        renderDriver = self.renderDriver_value.get()
    
    return renderDriver

def getAppsOptionFrameValues(self):
    startApp = None
    if self.startApp_check_value.get():
        startApp = self.startAppEntry.get()

    return startApp

def getOtherOptionFrameValues(self):
    pushTarget = None
    if self.pushTarget_check_value.get():
        pushTarget = self.pushTargetEntry.get()
    
    captureOrientation = None
    if self.captureOrientation_check_value.get():
        captureOrientation = self.captureOrientationEntry.get()

    noCleanUp = None
    if self.noCleanUp_check_value.get():
        noCleanUp = self.noCleanUp_check_value.get()
    
    noClipboardAutoSync = None
    if self.noClipboardAutoSync_check_value.get():
        noClipboardAutoSync = self.noClipboardAutoSync_check_value.get()

    noDownsizeOnError = None
    if self.noDownsizeOnError_check_value.get():
        noDownsizeOnError = self.noDownsizeOnError_check_value.get()
    
    noMipMaps = None
    if self.noMipMaps_check_value.get():
        noMipMaps = self.noMipMaps_check_value.get()
    
    printFps = None
    if self.printFps_check_value.get():
        printFps = self.printFps_check_value.get()

    preferText = None
    if self.preferText_check_value.get():
        preferText = self.preferText_check_value.get()
    
    requireAudio = None
    if self.requireAudio_check_value.get():
        requireAudio = self.requireAudio_check_value.get()

    return pushTarget, captureOrientation, noCleanUp, noClipboardAutoSync, noDownsizeOnError, noMipMaps, printFps, preferText, requireAudio

def getValuesFromAdvanchedWidget(self):
    audioBitRate, audioBuffer, audioOutputBuffer, audioCodec, audioEncoder, audioDup = getAudioOptionFrameValues(self)

    print('\nAudioOptionFrameVales:')
    print(f'AudioBitRate: {audioBitRate}')
    print(f'AudioBuffer: {audioBuffer}')
    print(f'AudioOutputBuffer: {audioOutputBuffer}')
    print(f"AudioCodec: {audioCodec}")
    print(f"AudioEncoder: {audioEncoder}")
    print(f"AudioDup: {audioDup}")
    print('\n\n')

    videoBitRate, videoBuffer, videoCodec, videoEncoder = getVideoOptionFrameValues(self)

    print('\nVideoOptionFrameValues:')
    print(f"VideoBitRate: {videoBitRate}")
    print(f"VideoBuffer: {videoBuffer}")
    print(f"VideoCodec: {videoCodec}")
    print(f"VideoEncoder: {videoEncoder}")
    print('\n\n')


    cameraAr, cameraFps, cameraSize, cameraHighSpeed = getCameraOptionFrameValues(self)
    
    print('\nCameraOptionFrameValues:')
    print(f"CameraAr: {cameraAr}")
    print(f"CameraFps: {cameraFps}")
    print(f"CameraSize: {cameraSize}")
    print(f"CameraHighSpeed: {cameraHighSpeed}")
    print('\n\n')

    windowTitle, windowX, windowY, windowWidth, windowHeight, newDisplay, maxSize, crop, angle, alwaysOnTop, fullScreen, windowBorderless = getWindowOptionFrameValues(self)

    print('\nWindowOptionFrameValues:')
    print(f"WindowTitle: {windowTitle}")
    print(f"WindowX: {windowX}")
    print(f"WindowY: {windowY}")
    print(f"WindowWidth: {windowWidth}")
    print(f"WindowHeight: {windowHeight}")
    print(f"NewDisplay: {newDisplay}")
    print(f"MaxSize: {maxSize}")
    print(f"Crop: {crop}")
    print(f"Angle: {angle}")
    print(f"AlwaysOnTop: {alwaysOnTop}")
    print(f"FullScreen: {fullScreen}")
    print(f"WindowBorderless: {windowBorderless}")
    print('\n\n')

    maxFps, shortCutMod, forceAdbForward, killAdbOnClose, noKeyRepeat, rawKeyEvents, legacyPaste, showTouches, noMouseHover = getControlOptionFrameValues(self)

    print('\nControlOptionFrameValues:')
    print(f"MaxFps: {maxFps}")
    print(f"ShortCutMod: {shortCutMod}")
    print(f"ForceAdbForward: {forceAdbForward}")
    print(f"KillAdbOnClose: {killAdbOnClose}")
    print(f"NoKeyRepeat: {noKeyRepeat}")
    print(f"RawKeyEvents: {rawKeyEvents}")
    print(f"LegacyPaste: {legacyPaste}")
    print(f"ShowTouches: {showTouches}")
    print(f"NoMouseHover: {noMouseHover}")    
    print('\n\n')


    pauseOnExit, screenOffTimeout, timeLimit, noPowerOn, turnScreenOff, powerOffOnClose, disableScreenSaver, stayAwake = getPowerOptionFrameValues(self)

    print('\nPowerOptionFrameValues:')
    print(f"PauseOnExit: {pauseOnExit}")
    print(f"ScreenOfftimeout: {screenOffTimeout}")
    print(f"TimeLimit: {timeLimit}")
    print(f"NoPowerOn: {noPowerOn}")
    print(f"TurnScreenOff: {turnScreenOff}")
    print(f"PowerOffOnClose: {powerOffOnClose}")
    print(f"DisableScreenSaver: {disableScreenSaver}")
    print(f"StayAwake: {stayAwake}")
    print('\n\n')


    record, recordFormats, recordOrientation = getRecordOptionFrameValues(self)
    
    print('\nRecordOptionFrameValues:')
    print(f"Record: {record}")
    print(f"RecordFormats: {recordFormats}")
    print(f"RecordOrientation: {recordOrientation}")
    print('\n\n')

    port, tunnelHost, tunnelPort = getConnectionsOptionFrameValues(self)

    print('\nConnectionsOptionFrameValues:')
    print(f"Port: {port}")
    print(f"TunnelHost: {tunnelHost}")
    print(f"TunnelPort: {tunnelPort}")
    print('\n\n')

    noVdDestroyContent, noVdSystemDecorations = getVirtualDisplayOptionFrameValues(self)

    print('\nVirtualDisplayOptionFrameValues:')
    print(f"NoVdDestroyContent: {noVdDestroyContent}")
    print(f"NoVdSystemDecorations: {noVdSystemDecorations}")
    print('\n\n')

    v4l2Sink, v4l2Buffer = getV4l2OptionFrameValues(self)

    print('\nV4l2OptionFrameValues:')
    print(f"V4l2Sink: {v4l2Sink}")
    print(f"V4l2Buffer: {v4l2Buffer}")
    print('\n\n')

    renderDriver = getRenderDriversOptionFrameValues(self)

    print('\nRenderDriversOptionFrameValues:')
    print(f"RenderDriver: {renderDriver}")
    print('\n\n')

    startApp = getAppsOptionFrameValues(self)

    print('\nAppsOptionFrameValues:')
    print(f"StartApp: {startApp}")
    print('\n\n')

    pushTarget, captureOrientation, noCleanUp, noClipboardAutoSync, noDownsizeOnError, noMipMaps, printFps, preferText, requireAudio = getOtherOptionFrameValues(self)

    print('\nOtherOptionFrameValues:')
    print(f"PushTarget: {pushTarget}")
    print(f"CaptureOrientation: {captureOrientation}")
    print(f"NoCleanUp: {noCleanUp}")
    print(f"NoClipboardAutoSync: {noClipboardAutoSync}")
    print(f"NoDownSizeOnError: {noDownsizeOnError}")
    print(f"NoMipMaps: {noMipMaps}")
    print(f"PrintFps: {printFps}")
    print(f"PreferText: {preferText}")
    print(f"RequireAudio: {requireAudio}")
    print('\n\n')

    return audioBitRate, audioBuffer, audioOutputBuffer, audioCodec, audioEncoder, audioDup, videoBitRate, videoBuffer, videoCodec, videoEncoder, cameraAr, cameraFps, cameraSize, cameraHighSpeed, windowTitle, windowX, windowY, windowWidth, windowHeight, newDisplay, maxSize, crop, angle, alwaysOnTop, fullScreen, windowBorderless, maxFps, shortCutMod, forceAdbForward, killAdbOnClose, noKeyRepeat, rawKeyEvents, legacyPaste, showTouches, noMouseHover, pauseOnExit, screenOffTimeout, timeLimit, noPowerOn, turnScreenOff, powerOffOnClose, disableScreenSaver, stayAwake, record, recordFormats, recordOrientation, port, tunnelHost, tunnelPort, noVdDestroyContent, noVdSystemDecorations, v4l2Sink, v4l2Buffer, renderDriver, startApp, pushTarget, captureOrientation, noCleanUp, noClipboardAutoSync, noDownsizeOnError, noMipMaps, printFps, preferText, requireAudio

command = None
def runProcess(device=None, otg=None, keyboard=None, mouse=None, gamepad=None, noControl=None, audioSource=None, noAudioForwarding=None, noAudioPlayback=None, videoSource=None, noVideoForwarding=None, cameraID=None, cameraFacing=None, noVideoPlayback=None, audioBitRate=None, audioBuffer=None, audioOutputBuffer=None, audioCodec=None, audioEncoder=None, audioDup=None, videoBitRate=None, videoBuffer=None, videoCodec=None, videoEncoder=None, cameraAr=None, cameraFps=None, cameraSize=None, cameraHighSpeed=None, windowTitle=None, windowX=None, windowY=None, windowWidth=None, windowHeight=None, newDisplay=None, maxSize=None, crop=None, angle=None, alwaysOnTop=None, fullScreen=None, windowBorderless=None, maxFps=None, shortCutMod=None, forceAdbForward=None, killAdbOnClose=None, noKeyRepeat=None, rawKeyEvents=None, legacyPaste=None, showTouches=None, noMouseHover=None, pauseOnExit=None, screenOffTimeout=None, timeLimit=None, noPowerOn=None, turnScreenOff=None, powerOffOnClose=None, disableScreenSaver=None, stayAwake=None, record=None, recordFormats=None, recordOrientation=None, port=None, tunnelHost=None, tunnelPort=None, noVdDestroyContent=None, noVdSystemDecorations=None, v4l2Sink=None, v4l2Buffer=None, renderDriver=None, startApp=None, pushTarget=None, captureOrientation=None, noCleanUp=None, noClipboardAutoSync=None, noDownsizeOnError=None, noMipMaps=None, printFps=None, preferText=None, requireAudio=None):
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

    if audioBitRate:
        audioBitRateCmd: list = [f'--audio-bit-rate={audioBitRate}']
        mainCmd += audioBitRateCmd
    
    if audioBuffer:
        audioBufferCmd: list = [f'--audio-buffer={audioBuffer}']
        mainCmd += audioBufferCmd
    
    if audioOutputBuffer:
        audioOutputBufferCmd: list = [f'--audio-output-buffer={audioOutputBuffer}']
        mainCmd += audioOutputBufferCmd
    
    if audioCodec:
        audioCodecCmd: list = [f'--audio-codec={audioCodec}']
        mainCmd += audioCodecCmd

    if audioEncoder:
        audioEncoderCmd: list = [f'--audio-encoder={audioEncoder}']
        mainCmd += audioEncoderCmd

    if audioDup:
        audioDupCmd: list = [f'--audio-dup']
        mainCmd += audioDupCmd
    
    if videoBitRate:
        videoBitRateCmd: list = [f'--video-bit-rate={videoBitRate}']
        mainCmd += videoBitRateCmd

    if videoBuffer:
        videoBufferCmd: list = [f'--video-buffer={videoBuffer}']
        mainCmd += videoBufferCmd

    if videoCodec:
        videoCodecCmd: list = [f'--video-codec={videoCodec}']
        mainCmd += videoCodecCmd
    
    if videoEncoder:
        videoEncoderCmd: list = [f'--video-encoder={videoEncoder}']
        mainCmd += videoEncoderCmd
    
    if cameraAr:
        cameraArCmd: list = [f'--camera-ar={cameraAr}']
        mainCmd += cameraArCmd
    
    if cameraFps:
        cameraFpsCmd: list = [f'--camera-fps={cameraFps}']
        mainCmd += cameraFpsCmd
    
    if cameraSize:
        cameraSizeCmd: list = [f'--camera-size={cameraSize}']
        mainCmd += cameraSizeCmd
    
    if cameraHighSpeed:
        cameraHighSpeedCmd: list = [f'--camera-high-speed']
        mainCmd += cameraHighSpeedCmd
    
    if windowTitle:
        windowTitleCmd: list = [f'--window-title={windowTitle}']
        mainCmd += windowTitleCmd
    
    if windowX:
        windowXCmd: list = [f'--window-x={windowX}']
        mainCmd += windowXCmd
    
    if windowY:
        windowYCmd: list = [f'--window-y={windowY}']
        mainCmd += windowYCmd
    
    if windowWidth:
        windowWidthCmd: list = [f'--window-width={windowWidth}']
        mainCmd += windowWidthCmd
    
    if windowHeight:
        windowHeightCmd: list = [f'--window-height={windowHeight}']
        mainCmd += windowHeightCmd
    
    if newDisplay:
        newDisplayCmd: list = [f'--new-display={newDisplay}']
        mainCmd += newDisplayCmd
    
    if maxSize:
        maxSizeCmd: list = [f'--max-size={maxSize}']
        mainCmd += maxSizeCmd

    if crop:
        cropCmd: list = [f'--crop={crop}']
        mainCmd += cropCmd
    
    if angle:
        angleCmd: list = [f'--angle={angle}']
        mainCmd += angleCmd
    
    if alwaysOnTop:
        alwaysOnTopCmd: list = [f'--always-on-top']
        mainCmd += alwaysOnTopCmd

    if fullScreen: 
        fullScreenCmd: list = [f'--fullscreen']
        mainCmd += fullScreenCmd
    
    if windowBorderless:
        windowBorderlessCmd: list = [f'--window-borderless']
        mainCmd += windowBorderlessCmd
    
    if maxFps:
        maxFpsCmd: list = [f'--max-fps={maxFps}']
        mainCmd += maxFpsCmd
    
    if shortCutMod:
        shortCutModCmd: list = [f'--short-cut={shortCutMod}']
        mainCmd += shortCutModCmd
    
    if forceAdbForward:
        forceAdbForwardCmd: list = [f'--force-adb-forward']
        mainCmd += forceAdbForwardCmd    
    
    if killAdbOnClose:
        killAdbOnCloseCmd: list = ['--kill-adb-on-close']
        mainCmd += killAdbOnCloseCmd
    
    if noKeyRepeat:
        noKeyRepeatCmd: list = ['--no-key-repeat']
        mainCmd += noKeyRepeatCmd
    
    if rawKeyEvents:
        rawKeyEventsCmd: list = ['--raw-key-events']
        mainCmd += rawKeyEventsCmd
    
    if legacyPaste:
        legacyPasteCmd: list = ['--legacy-paste']
        mainCmd += legacyPasteCmd
    
    if showTouches:
        showTouchesCmd: list = ['--show-touches']
        mainCmd += showTouchesCmd    
    
    if noMouseHover:
        noMouseHoverCmd: list = ['--no-mouse-hover']
        mainCmd += noMouseHoverCmd
    
    if pauseOnExit:
        pauseOnExitCmd: list = [f'--pause-on-exit={pauseOnExit}']
        mainCmd += pauseOnExitCmd
    
    if screenOffTimeout:
        screenOffTimeoutCmd: list = [f'--screen-off-timeout={screenOffTimeout}']
        mainCmd += screenOffTimeoutCmd
    
    if timeLimit:
        timeLimitCmd: list = [f'--time-limit={timeLimit}']
        mainCmd += timeLimitCmd

    if noPowerOn: 
        noPowerOnCmd: list = ['--no-power-on']
        mainCmd += noPowerOnCmd

    if turnScreenOff:
        turnScreenOffCmd: list = ['--turn-screen-off']
        mainCmd += turnScreenOffCmd

    if powerOffOnClose:
        powerOffOnCloseCmd: list = ['--power-off-on-close']
        mainCmd += powerOffOnCloseCmd

    if disableScreenSaver:
        disableScreenSaverCmd: list = ['--disable-screensaver']
        mainCmd += disableScreenSaverCmd

    if stayAwake:
        stayAwakeCmd: list = ['--stay-awake']
        mainCmd += stayAwakeCmd

    if record:
        recordCmd: list = [f'--record={record}']
        mainCmd += recordCmd
    
    if recordFormats:
        recordFormatsCmd: list = [f'--record-format={recordFormats}']
        mainCmd += recordFormatsCmd
    
    if recordOrientation: 
        recordOrientationCmd: list = [f'--record-orientation={recordOrientation}']
        mainCmd += recordOrientationCmd
    
    if port: 
        portCmd: list = [f'--port={port}']
        mainCmd += portCmd

    if tunnelHost: 
        tunnelHostCmd: list = [f'--tunnel-host={tunnelHost}']
        mainCmd += tunnelHostCmd

    if tunnelPort:
        tunnelPortCmd: list = [f'--tunnel-port={tunnelPort}']
        mainCmd += tunnelPortCmd

    if noVdDestroyContent:
        noVdDestroyContentCmd: list = ['--no-vd-destroy-content']
        mainCmd += noVdDestroyContentCmd

    if noVdSystemDecorations:
        noVdSystemDecorationsCmd: list = ['--no-vd-system-decorations']
        mainCmd += noVdSystemDecorationsCmd

    if v4l2Sink:
        v4l2SinkCmd: list = [f'--v4l2-sink={v4l2Sink}']
        mainCmd += v4l2SinkCmd

    if v4l2Buffer:
        v4l2BufferCmd: list = [f'--v4l2-buffer={v4l2Buffer}']
        mainCmd += v4l2BufferCmd

    if renderDriver: 
        renderDriverCmd: list = [f'--render-driver={renderDriver}']
        mainCmd += renderDriverCmd

    if startApp:
        startAppCmd: list = [f'--start-app={startApp}']
        mainCmd += startAppCmd

    if pushTarget: 
        pushTargetCmd: list = [f'--push-target={pushTarget}']
        mainCmd += pushTargetCmd

    if captureOrientation:
        captureOrientationCmd: list = [f'--capture-orientation={captureOrientation}']
        mainCmd += captureOrientationCmd

    if noCleanUp:
        noCleanUpCmd: list = ['--no-cleanup']
        mainCmd += noCleanUpCmd

    if noClipboardAutoSync:
        noClipboardAutoSyncCmd: list = ['--no-clipboard-autosync']
        mainCmd += noClipboardAutoSyncCmd

    if noDownsizeOnError:
        noDownsizeOnErrorCmd: list = ['--no-downsize-on-error']
        mainCmd += noDownsizeOnErrorCmd

    if noMipMaps:
        noMipMapsCmd: list = ['--no-mipmaps']
        mainCmd += noMipMapsCmd

    if printFps:
        printFpsCmd: list = ['--print-fps']
        mainCmd += printFpsCmd

    if preferText:
        preferTextCmd: list = ['--prefer-text']
        mainCmd += preferTextCmd

    if requireAudio: 
        requireAudioCmd: list = ['--require-audio']
        mainCmd += requireAudioCmd

    print(f'Main Command: {mainCmd}')
    # command = subprocess.Popen(mainCmd, text=False)

def start_runProcess_thread(*args):
    thread = threading.Thread(target=runProcess, args=(*args,))
    thread.start()

def stopScrcpy(self):
    try:
        global command
        command.terminate()
        
    except Exception as e:
        print(f'Error on stopScrcpy function\n{str(e)}')
        



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


    if self.advanched_check_value.get():
        audioBitRate, audioBuffer, audioOutputBuffer, audioCodec, audioEncoder, audioDup, videoBitRate, videoBuffer, videoCodec, videoEncoder, cameraAr, cameraFps, cameraSize, cameraHighSpeed, windowTitle, windowX, windowY, windowWidth, windowHeight, newDisplay, maxSize, crop, angle, alwaysOnTop, fullScreen, windowBorderless, maxFps, shortCutMod, forceAdbForward, killAdbOnClose, noKeyRepeat, rawKeyEvents, legacyPaste, showTouches, noMouseHover, pauseOnExit, screenOffTimeout, timeLimit, noPowerOn, turnScreenOff, powerOffOnClose, disableScreenSaver, stayAwake, record, recordFormats, recordOrientation, port, tunnelHost, tunnelPort, noVdDestroyContent, noVdSystemDecorations, v4l2Sink, v4l2Buffer, renderDriver, startApp, pushTarget, captureOrientation, noCleanUp, noClipboardAutoSync, noDownsizeOnError, noMipMaps, printFps, preferText, requireAudio = getValuesFromAdvanchedWidget(self)

        start_runProcess_thread(
            device,
            otg,
            keyboard,
            mouse,
            gamepad,
            noControl,
            audioSource,
            noAudioForwarding,
            noAudioPlayback,
            videoSource,
            noVideoForwarding,
            cameraID,
            cameraFacing,
            noVideoPlayback,
            audioBitRate,
            audioBuffer,
            audioOutputBuffer,
            audioCodec,
            audioEncoder,
            audioDup,
            videoBitRate,
            videoBuffer,
            videoCodec,
            videoEncoder,
            cameraAr,
            cameraFps,
            cameraSize,
            cameraHighSpeed,
            windowTitle,
            windowX,
            windowY,
            windowWidth,
            windowHeight,
            newDisplay,
            maxSize,
            crop, 
            angle, 
            alwaysOnTop, 
            fullScreen, 
            windowBorderless, 
            maxFps, 
            shortCutMod, 
            forceAdbForward, 
            killAdbOnClose, 
            noKeyRepeat, 
            rawKeyEvents, 
            legacyPaste, 
            showTouches, 
            noMouseHover, 
            pauseOnExit, 
            screenOffTimeout, 
            timeLimit, 
            noPowerOn, 
            turnScreenOff, 
            powerOffOnClose, 
            disableScreenSaver, 
            stayAwake, 
            record, 
            recordFormats, 
            recordOrientation, 
            port, 
            tunnelHost, 
            tunnelPort, 
            noVdDestroyContent, 
            noVdSystemDecorations, 
            v4l2Sink, 
            v4l2Buffer, 
            renderDriver, 
            startApp, 
            pushTarget, 
            captureOrientation, 
            noCleanUp, 
            noClipboardAutoSync, 
            noDownsizeOnError, 
            noMipMaps, 
            printFps, 
            preferText, 
            requireAudio

        )
    
    else:
        start_runProcess_thread(
            device,
            otg,
            keyboard,
            mouse,
            gamepad,
            noControl,
            audioSource,
            noAudioForwarding,
            noAudioPlayback,
            videoSource,
            noVideoForwarding,
            cameraID,
            cameraFacing,
            noVideoPlayback
        )



    return