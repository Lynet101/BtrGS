import subprocess

#Needs to be replaced by system CALLs
D_PCI1 = "0000:01:00.0"
D_PCI2 = "0000:01:00.1"
DM = 'lightdm'

CALL=subprocess.check_output
attach=CALL('echo 1 > /sys/bus/pci/rescan')
remove1=CALL('echo 1 > /sys/bus/devices/', D_PCI1, '/remove')
remove2=CALL('echo 1 > /sys/bus/devices/', D_PCI2, '/remove')
stopdm=CALL('rc-service', DM, 'stop')
startdm=CALL('rc-service', DM, 'start')
load_driver=CALL('modprobe nvidia, nvidia_uvm, nvidia_drm, nvidia_modeset')
unload_driver=CALL('rmmod -f nvidia, nvidia_uvm, nvidia_drm, nvidia_modeset')
inteX=CALL('rm -r /etc/X11 && cp -r /etc/BtrHGS/X-integrated /etc/X11')
dediX=CALL('rm -r /etc/X11 && cp -r /etc/BtrHGS/X-dedicated /etc/X11')
kill=CALL("lsof /dev/nvidia* | awk '{print $2}' | xargs -I {} kill {}", shell=True)

#Done | Not tested
def switch_main(self):

    DECIRED = CALL('cat /var/BtrHGS/decired.mode')
    CURRENT = CALL('cat /var/BtrHGS/current.mode')

    if DECIRED == 'off':
        if CURRENT == 'on':
            d2i()
        
        if CURRENT == 'off':
            print("dGPU already off, won't proceed")
        
        if CURRENT == 'hybrid':
            h2i()
        
        else:
            print('CURRENT graphics mode unknown...')
    
    if DECIRED == 'on':
        if CURRENT == 'off':
            i2d()
        
        if CURRENT == 'on':
            print("dGPU already on, won't proceed")
        
        if CURRENT == 'hybrid':
            h2d()
        
        else:
            print('CURRENT graphics mode unknown...')
    
    if DECIRED == 'hybrid':
        if CURRENT == 'on':
            d2h()
        
        if CURRENT == 'hybrid':
            print("Already Hybrid, won't proceed")
        
        if CURRENT == 'off':
            i2h()
        else:
            print('CURRENT graphics mode unknown...')

"""
d2i | Dedicated to integrated
i2d | Integrated to dedicated
h2i | Hybrid to integrated
h2d | Hybrid to dedicated
d2h | Dedicated to hybrid
i2h | Integrated to hybrid
"""

#Done | Not tested
def d2i():
    try:
        stopdm
        try:
            if CALL('lsof /dev/nvidia*') != "":
                kill_choice=input('processes are still running on dGPU... Disabling it will kill theese processes\ndo you want to proceed(y/n)?\n')
                if kill_choice == 'y':
                    try:
                        kill
                        remove1
                        remove2
                        unload_driver   
                    except:
                        print('failed to kill processes, and unload dGPU')
                        return
                elif kill_choice == 'n':
                    print('please manually close the programs listed below, before continuing:')
                    print(CALL('lsof /dev/nvidia*'))
                    return
                else:
                    print('unrecognised option!')
            else:
                print('no processes are running... continuing')
                remove1
                remove2
                unload_driver
        except:
            print('Error when trying to get running processes\nAborting!')
            return
        inteX
        startdm
    except:
        print('failed to switch')

#Done | Seemless | Not tested
def h2i():
    try:
        if CALL('lsof /dev/nvidia*') != "":
            kill_choice=input('processes are still running on dGPU... Disabling it will kill theese processes\ndo you want to proceed(y/n)?\n')
            if kill_choice == 'y':
                try:
                    kill
                    remove1
                    remove2
                    unload_driver   
                except:
                    print('failed to kill processes, and unload dGPU')
                    return
            elif kill_choice == 'n':
                print('please manually close the programs listed below, before continuing:')
                print(CALL('lsof /dev/nvidia*'))
                return
            else:
                print('unrecognised option!')
        else:
            print('no processes are running... continuing')
            remove1
            remove2
            unload_driver
    except:
        print('Error when trying to get running processes\nAborting!')
        return

#Done | Not tested
def i2d():
    try:
        stopdm
        attach
        if CALL('lsmod | grep nvi') != "":
            print('drivers already loaded!')
        else:
            load_driver
        dediX
        startdm
    except:
        print('failed to switch')
        return

#Done | Not tested
def h2d():
    try:
        stopdm
        dediX
        startdm
    except:
        print('failed to switch')
        return

#Done | Not tested
def d2h():
    try:
        stopdm
        inteX
        startdm
    except:
        print('failed to switch')
        return

#Done | Seemless | Not tested
def i2h():
    try:
        attach
        if CALL('lsmod | grep nvi') != "":
            print('drivers already loaded!')
        else:
            load_driver
    except:
        print('failed to load dGPU')
        return