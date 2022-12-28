import os
import time
import subprocess
from config import *

CALL=os.system

class switch():
    def __init__(self):
        self.dedix='[Path to dedicated x config] /etc/X11'
        self.intex='[Path to integrated x config] /etc/X11'
        self.hybx='[Path to hybrid x config (or integrated)] /etc/X11'
        self.x_dir='/etc/X11'
        self.rescan=f'echo 1 > /sys/bus/pci/rescan'
        self.driver_load='modprobe nvidia nvidia_uvm nvidia_drm nvidia_modeset'
        self.process_kill="lsof /dev/nvidia0 | awk '{print $1}' | xargs -I {} pkill -f {}"
        self.unbind=(f'echo "{d_pci1}" > /sys/bus/pci/devices/{d_pci1}/driver/unbind && echo "{d_pci2}" > /sys/bus/pci/devices/{d_pci2}/driver/unbind')
        self.remove=(f'echo 1 > /sys/bus/pci/devices/{d_pci1}/remove && echo 1 > /sys/bus/pci/devices/{d_pci2}/remove')
        self.dm_stop=(f'rc-service {dm} stop')
        self.dm_start=(f'rc-service {dm} start')
        self.xconf_dedi=(f'rm -r {self.x_dir} && cp -r {self.dedix}')
        self.xconf_hyb=(f'rm -r {self.x_dir} && cp -r {self.hybx}')
        self.xconf_inte=(f'rm -r {self.x_dir} && cp -r {self.intex}')
        
    def i2h(self):
        try:
            CALL(self.rescan)
            if CALL('lsmod | grep nvi') != "":
                print('drivers already loaded!')
            else:
                CALL(self.driver_load)
            return 'succes!'
        except:
            return 'failed to reload gpu and/or drivers'

    def h2i(self):
        try:
            try:
                subprocess.check_output(self.process_kill, shell=True)
                CALL(self.unbind)
                CALL(self.remove)
            except:
                CALL(self.unbind)
                CALL(self.remove)
            return 'succes!'
        except:
            return 'failed to remove gpu... something might be bound to it'

    def d2i(self):
        CALL(self.dm_stop)
        try:
            try:
                subprocess.check_output(self.process_kill, shell=True)
                CALL(self.unbind)
                CALL(self.remove)
            except:
                CALL(self.unbind)
                CALL(self.remove)
        except:
            return 'failed to remove gpu... something might be bound to it'
        try:
            CALL(self.xconf_inte)
        except:
            return 'failed to load x-config (does /etc/X11.inte exist?'
        CALL(self.dm_start)
        return 'succes!'

    def i2d(self):
        CALL(self.dm_stop)
        CALL(self.rescan)
        CALL(self.driver_load)
        try:
            CALL(self.xconf_dedi)
        except:
            return 'failed to load x-config (does /etc/X11.dedi exist?'
        CALL(self.dm_start)
        return 'succes!'

    def h2d(self):
        CALL(self.dm_stop)
        try:
            CALL(self.xconf_dedi)
        except:
            return 'failed to load x-config (does /etc/X11.dedi exist?'
        CALL(self.dm_start)
        return 'succes!'

    def d2h(self):
        CALL(self.dm_stop)
        try:
            CALL(self.xconf_hyb)
        except:
            return 'failed to load x-config (does /etc/X11.hyb exist?'
        CALL(self.dm_start)
        return 'succes!'

