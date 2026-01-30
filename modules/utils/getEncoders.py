from subprocess import check_output
import threading
import re


def getEncoders(self, device, forAudio=None) -> list:
    if not device:
        return []
    
    cmd = ["scrcpy", "-s", device, "--list-encoders"]
    output = check_output(cmd).decode('utf-8')

    if forAudio:
        output = output.split('[server] INFO: List of video encoders:')[1].split('[server] INFO: List of audio encoders:')[1].split('scrcpy 3.3.1 <https://github.com/Genymobile/scrcpy>')[0].strip()
        pattern = r'--audio-encoder=(.+)'
        found: list = re.findall(pattern, output)
        encoders: list = [i.split()[0].strip() for i in found]
        return encoders

    else:
        output = output.split('[server] INFO: List of video encoders:')[1].split('[server] INFO: List of audio encoders:')[0].strip()
        pattern = r'--video-encoder=(.+)'
        found: list = re.findall(pattern, output)
        encoders: list = [i.split()[0].strip() for i in found]
        return encoders
    
    