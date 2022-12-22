import time
import threading
from Switching import *

#Done | Not tested
def start():
    try:
        if CALL('cat /var/BtrHGS/current.mode') == 'integrated':
            app=input('program to launch: ')
            i2h()
            thread = threading.Thread(target=(CALL(f'prime-run {app}', shell=True)))
            thread.start()
            check(app)
        else:
            print('This feature is only available when running in integrated')
    except:
        print('failed to read current state')


#Done | Not tested
def check(app):
    while running == True:
        time.sleep(1)
        try:
            app_pid=CALL(f'pidof {app}', shell=True)
            print(f'app running with pid {app_pid}')
        except:
            print('app not running')
            try:
                CALL("lsof /dev/nvidia* | awk '{print $2}' | xargs -I {} kill {}", shell=True) #procceses with more than one thread are... weird
                if CALL("lsof /dev/nvidia* ") == "":
                    h2i()
                    running = False
                else:
                    print('failed to kill remaining processes.... Aborting!')
                    running = False
            except:
                print('no processes found... continuing')
                h2i()
                running = False

    