import subprocess
import threading
import time
import os


def reqFolderChek():
    reqFolder = ['Telegram users', 'db']
    for folder in reqFolder:
        if folder in os.listdir():
            pass
        else:
            os.mkdir(folder)


startMain = threading.Thread(target=subprocess.call, args=(["python", "Start_main.py"],))
Main = threading.Thread(target=subprocess.call, args=(["python", "main.py"],))

reqFolderChek()

time.sleep(1)

startMain.start()
Main.start()
