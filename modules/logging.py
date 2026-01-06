import os
import datetime

LOGFILENAME = 'scrcpyGUI_logs.txt'

class Logs:    
    def log(self, text: str):
        text = text.strip()
        currentTime = datetime.datetime.now().strftime('%a %d %b %Y, %I:%M%:%S %p')
        log = f"{"="*10} {currentTime} {"="*10}\nLog: {text}\n{"="*10} [] {"="*10}"

        self.saveLogs(log)

    def saveLogs(self, log: str):
        try:
            with open(LOGFILENAME, 'a', encoding='utf-8') as logfile:
                pass
        except FileNotFoundError:
            with open(LOGFILENAME, 'w') as f:
                f.write('\n')
        except Exception as e:
            print(f"[Logging]: An error has occurred:\nError: {str(e)}")
    