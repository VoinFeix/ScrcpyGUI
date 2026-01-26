from subprocess import check_output
import threading
import re


def getEncoders(self, device, codec: str, forAudio=None) -> list:
    if not codec or not device:
        return []
    
    encodersList: list = []
    cmd = ["scrcpy", "-s", device, "--list-encoders"]
    output = check_output(cmd).decode('utf-8')

    codeC = pattern = None

    if forAudio:
        output = output.split('INFO: List of audio encoders:')[1].split('scrcpy 3.3.1 <https://github.com/Genymobile/scrcpy>')[0].strip().split('\n')
        codeC = f'--audio-codec={codec}'
        pattern = '--audio-encoder=(.+)'
    else:
        output = output.split('INFO: List of video encoders:')[1].split('scrcpy 3.3.1 <https://github.com/Genymobile/scrcpy>')[0].strip().split('\n')
        codeC = f'--video-codec={codec}'
        pattern = '--video-encoder=(.+)'

    for i in output:
        if codec in i:
            found = re.search(pattern, i).group()
            encodersList.append(found.split('=')[1].split()[0])

    return encodersList

