
from Common.Log import Logger

logPrintLF = True
def logPrint(*args, **kwargs):
    global logPrintLF
    if 'end' in kwargs:
        logPrintLF = False
    else:
        if not logPrintLF:
            logPrintLF = True
            print()
    print(*args, **kwargs)


logger = Logger(logPrint)
