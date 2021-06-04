import os
import threading
import time

def reqFolderChek():
    reqFolder = ['Telegram users', 'db']
    for folder in reqFolder:
        if folder not in os.listdir():
            os.mkdir(folder)
        else:
            pass


def stm():
    os.system('python Start_main.py')


def sm():
    os.system('python main.py')

rfc = threading.Thread(target=reqFolderChek())
startMain = threading.Thread(target=stm())
Main = threading.Thread(target=sm())


rfc.start()
rfc.join()
startMain.start()
Main.start()
