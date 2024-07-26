import requests
from threading import Timer
import os
import subprocess

dir_path = os.path.dirname(os.path.realpath(__file__))

GOOGLE_GEN_204_URL = "http://clients1.google.com/generate_204"
FREQ = 15 # Seconds

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

def iscaptive():
    try:
        r = requests.get(GOOGLE_GEN_204_URL)
    except Exception as e:
        print(repr(e))
        return False

    if r.status_code != 204:
        return True
    else:
        return False

def login():
    script_path = os.path.join(dir_path, 'login.py')
    subprocess.run(['python3', script_path])

def captivepass():
    if iscaptive():
        login()

if __name__ == "__main__":
    print("Started the Captive Checker script")
    captive_checker = RepeatTimer(FREQ, captivepass)
    captive_checker.start()
    captive_checker.join()
