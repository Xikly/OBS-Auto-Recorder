import processcheck
import pydirectinput
import time
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
    print ('Scanning. Program has scanned {0} time/s.'.format(scanamount))

    scanamount = scanamount + 1

    for x in processlist:
        if processcheck.checkIfProcessRunning(x) is True:
            print ('Process running!')
            pydirectinput.press(hotkey)
            y = True
            while y is True:
                if processcheck.checkIfProcessRunning(x) is False:
                    print ('program exitted')
                    scanamount = 1
                    pydirectinput.press(hotkey)
                    y = False
                else:
                    time.sleep(2)
    
    time.sleep(5)

pnfile.close()

print ('OBS IS NOT OPEN!\nOPEN OBS FOR THE PROGRAM TO FUNCTION.')