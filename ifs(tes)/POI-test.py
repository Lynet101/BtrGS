import time
import subprocess
import os

"""
A bit messy, but h2i, i2h, along with POI is working
"""

DM='lightdm'
CALL=os.system
D_PCI1="0000:01:00.0"
D_PCI2="0000:01:00.1"

DEDIX='/etc/X11.nvi /etc/X11'
INTEX='/etc/X11.inte /etc/X11'
HYBX='/etc/X11.hyb /etc/X11'
X_DIR='/etc/X11'

#Done | Working
def main():
    action=input('switch/poi: ')
    if action == 'poi':
        start()
    elif action == 'switch':
        mode=input('what mode (i2h, i2d, h2i, h2d, d2h, d2i):' )
        try:
            function_dictionary[mode]()
        except:
            print("mode doesn't exist")


#Done | Working
def start():
    APP=input('APP: ')
    i2h()
    CALL(f'doas -u slindau prime-run {APP}')
    check(APP)

#Done | Working
def check(APP):
    running=True
    while running == True:
        time.sleep(0.1)
        try:
            app_pid=subprocess.check_output(f'pidof {APP}', shell=True)
            print(f'app running with pid {app_pid}')
        except:
            print('app not running')
            h2i()
            running = False

#Done | Working
def i2h():
    try:
        CALL('echo 1 > /sys/bus/pci/rescan')
        if CALL('lsmod | grep nvi') != "":
            print('drivers already loaded!')
        else:
            CALL('modprobe nvidia nvidia_uvm nvidia_drm nvidia_modeset')
    except:
        print('failed to load dGPU')
        return

#Done | Working
def h2i():
    try:
        subprocess.check_output("lsof /dev/nvidia0 | awk '{print $1}' | xargs -I {} pkill -f {}", shell=True)
        CALL(f'echo "{D_PCI1}" > /sys/bus/pci/devices/{D_PCI1}/driver/unbind')
        CALL(f'echo "{D_PCI2}" > /sys/bus/pci/devices/{D_PCI2}/driver/unbind')
        CALL(f'echo 1 > /sys/bus/pci/devices/{D_PCI1}/remove')
        CALL(f'echo 1 > /sys/bus/pci/devices/{D_PCI2}/remove')
        #CALL('rmmod -f nvidia nvidia_uvm nvidia_drm nvidia_modeset')
    except:
        CALL(f'echo "{D_PCI1}" > /sys/bus/pci/devices/{D_PCI1}/driver/unbind')
        CALL(f'echo "{D_PCI2}" > /sys/bus/pci/devices/{D_PCI2}/driver/unbind')
        CALL(f'echo 1 > /sys/bus/pci/devices/{D_PCI1}/remove')
        CALL(f'echo 1 > /sys/bus/pci/devices/{D_PCI2}/remove')
        #CALL('rmmod -f nvidia nvidia_uvm nvidia_drm nvidia_modeset')

def d2i():
    try:
        CALL(f'rc-service {DM} stop')
        try:
            try:
                subprocess.check_output("lsof /dev/nvidia0 | awk '{print $1}' | xargs -I {} pkill -f {}", shell=True)
                CALL(f'echo "{D_PCI1}" > /sys/bus/pci/devices/{D_PCI1}/driver/unbind')
                CALL(f'echo "{D_PCI2}" > /sys/bus/pci/devices/{D_PCI2}/driver/unbind')
                CALL(f'echo 1 > /sys/bus/pci/devices/{D_PCI1}/remove')
                CALL(f'echo 1 > /sys/bus/pci/devices/{D_PCI2}/remove')
                #CALL('rmmod -f nvidia nvidia_uvm nvidia_drm nvidia_modeset')
            except:
                CALL(f'echo "{D_PCI1}" > /sys/bus/pci/devices/{D_PCI1}/driver/unbind')
                CALL(f'echo "{D_PCI2}" > /sys/bus/pci/devices/{D_PCI2}/driver/unbind')
                CALL(f'echo 1 > /sys/bus/pci/devices/{D_PCI1}/remove')
                CALL(f'echo 1 > /sys/bus/pci/devices/{D_PCI2}/remove')
                #CALL('rmmod -f nvidia nvidia_uvm nvidia_drm nvidia_modeset')
        except:
            print('Error when trying to get running processes\nAborting!')
            return
        CALL(f'rm -r {X_DIR} && cp -r {INTEX}')
        CALL(f'rc-service {DM} start')
    except:
        print('failed to switch')

def i2d():
    try:
        CALL(f'rc-service {DM} stop')
        try:
            CALL('echo 1 > /sys/bus/pci/rescan')
            if CALL('lsmod | grep nvi') != "":
                print('drivers already loaded!')
            else:
                CALL('modprobe nvidia nvidia_uvm nvidia_drm nvidia_modeset')
        except:
            print('failed to load dGPU')
            return
        CALL(f'rm -r {X_DIR} && cp -r {DEDIX}')
        CALL(f'rc-service {DM} start')
    except:
        print('failed to switch')
        return

#Done | Not tested
def h2d():
    try:
        CALL(f'rc-service {DM} stop')
        CALL(f'rm -r {X_DIR} && cp -r {DEDIX}')
        CALL(f'rc-service {DM} start')
    except:
        print('failed to switch')
        return

#Done | Not tested
def d2h():
    try:
        CALL(f'rc-service {DM} stop')
        CALL(f'rm -r {X_DIR} && cp -r {HYBX}')
        CALL(f'rc-service {DM} start')
    except:
        print('failed to switch')
        return

function_dictionary={'i2h':i2h, 'i2d':i2d, 'h2i':h2i, 'h2d':h2d, 'd2h':d2h, 'd2i':d2i}

if __name__ == '__main__':
    main()