Release notes:

start notes:
    - Things like Display manager, and pci address to the dGPU is not yet auto-detected. Theese will have to be specified manually in the config.py (either before install, or afterwards in /etc/BtrHGS/config.py).
    - Xorg files will also have to be updated according to iGPU and dGPU pci address (found in ./X or after install under /etc/X11.(inte/nvi/hyb)).
    - Currently only compatible with openrc (though the daemon isn't complex (one line of code), so I'm sure you can translate it to other init systems)
    - Currently only compatible with sudo (though if you, like me, use doas, chances are you've just made sudo a symbolic link to doas anyways)
    - Lastly; Yes i know some of the ways i achieve things, like the entire daemon, is unconventional at best, but do keep in mind this is a testing release. It's not meant to be daily driven, and just meant for finding limitations, and exploring solutions to fixing theese withing linux.

Switching:
    - Integrated to hybrid works seemless
    - Hybrid to integrated works seemless, unless X was started in hybrid, in which case X will be restarted*
    - All switching to and from dedicated requires restart of X*

Functionallity:
    - Display output on laptop screen, in Dedicated not working | Probably an easy fix though
    - Display output on dGPU, in hybrid mode not working*
    - POI (Prime Offload on Integrated | The ability to one-shot the gpu, for only one program) not implemented*
    - EDI (External Display on Integrated | dGPU will automatically turn on, when displays connected, and turn off when disconnected) not implemented*

All items marked with * are due to the same reasoning;

Currently in linux there's no way to switch a process between graphic cards. Hince if a process has started on 1 GPU, it can only run on that GPU, and if that GPU where to be shutdown, the program must close before hand.

I'm working on a solution to try and implement something i will most likely call DVMM (Dynamic Video Memory Management), which aims to move data between GPU's, and allow for seemless switching of everything. Don't get me wrong, it'll take some time, and the first few releases will be broken AF. But in the end, it's hopefulle going to work

Also, a big thank you to the Optimus-Manager creators. As many of you will probably realise, the x-configs are called '10-optimus-manager.conf', and that's because i just had it create them for me. Saved me a lot of work there guys! (I will eventually be implementing my own xorg files, but again, this is a tester. I'm not gonna put to much work into having a nice user experience, in a tester ment for developmental work)

The Installer contains an Install and Uninstall command. The program doesn't create temporary fails, and currently keep within the folders created upon install, so uninstalling is guaranteed to remove all files from your system (unless you moved something around).

In case you're a dev, the installer also contains a hidden option called "Ri" this will run both the uninstall and install script, to refresh all files. Very usefull for when you have to test 100's of times in a row, with minor tweaks in between each itteration :)