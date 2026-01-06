from subprocess import check_output
import re
import threading

camera_ids = []

def getCameraIDs(self, device: str):
    global camera_ids
    cmd = ["scrcpy", "-s", device, "--list-cameras"]
    output = check_output(cmd).decode('utf-8')

    pattern = r'--camera-id=\d+'
    allids = re.findall(pattern, output)

    for i in allids:
        tmp = i.split('=')
        del tmp[0]
        camera_ids.append(tmp[0])


    return camera_ids
    
    

