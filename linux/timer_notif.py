import time
import subprocess

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

minute = 60
timer = minute*7
message =("Go get your burger")

time.sleep(timer)
sendmessage(message)
