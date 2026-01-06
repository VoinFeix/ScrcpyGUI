import subprocess
from typing import List

def getDevices() -> List[str]:
    cmd = ["adb", "devices"]
    output = subprocess.check_output(cmd).decode('utf-8')

    devices: list = []
    
    for i in output.split('\t'):
        devices.append(i.split('\n')[1])
    
    return devices
