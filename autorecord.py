import processcheck
import pydirectinput
import time
from datetime import datetime
from re import search

scanamount = 1

#CONFIG READING
pnfile = open("config.txt", "r")
pnamesread = pnfile.readlines()

hotkey = pnamesread[0]
hotkey = hotkey[13:]
hotkey = hotkey[:-2]
hotkey = hotkey.lower()

processlistraw = pnamesread[3:]

pnfile.close()

processlist = []

for x in processlistraw:
    if search(r'\n', x):
        i = x[:-1]
        processlist.append(i)
    else:
        processlist.append(x)

#PROGRAM BEGINNING
while processcheck.checkIfProcessRunning("obs64.exe") is True:
    print ('{0} | Scanning for process to open. Script has scanned {1} time/s.'.format(datetime.fromtimestamp(datetime.timestamp(datetime.now())), scanamount))

    scanamount = scanamount + 1

    for x in processlist:
        if processcheck.checkIfProcessRunning(x) is True:
            print ('{0} | Process running!'.format(datetime.fromtimestamp(datetime.timestamp(datetime.now()))))
            pydirectinput.press(hotkey)
            y = True
            scanamount = 1
            while y is True:
                print ('{0} | Scanning for process closure. Script has scanned {1} time/s.'.format(datetime.fromtimestamp(datetime.timestamp(datetime.now())), scanamount))
                if processcheck.checkIfProcessRunning(x) is False:
                    print ('{0} | Process exitted.'.format(datetime.fromtimestamp(datetime.timestamp(datetime.now()))))
                    scanamount = 1
                    pydirectinput.press(hotkey)
                    y = False
                else:
                    time.sleep(2)
                    scanamount = scanamount + 1
    
    time.sleep(5)

pnfile.close()

print ('{0} | OBS IS NOT OPEN!\nOPEN OBS FOR THE SCRIPT TO FUNCTION.'.format(datetime.fromtimestamp(datetime.timestamp(datetime.now()))))