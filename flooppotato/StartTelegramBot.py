import os
import threading
import time
import subprocess



def reqFolderChek():
    reqFolder = ['Telegram users', 'db']
    for folder in reqFolder:
        if folder in os.listdir():
            pass
        else:
            os.mkdir(folder)


def stm():
    os.system('python Start_main.py')


def sm():
    os.system('python main.py')


startMain = threading.Thread(target=os.system, args=("python Start_main.py",))
Main = threading.Thread(target=os.system, args=('python main.py',))

reqFolderChek()

time.sleep(1)

startMain.start()
Main.start()
