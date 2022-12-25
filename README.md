# BtrHGS
Better Hybrid Graphic Support for Linux
#############################################################################################

!!!Early development!!!

All code found in the current repo is highly experimental. Code found in 'BtrHGS Function Collection..." is just a collection of all the functions, for a quick way for me to see how all functions are gonna tie together. NOT MENT FOR EXECUTION EVER!

#############################################################################################

This project aims to bring propper support for hybrid graphics to linux.

My goal is essentially to have a hybrid graphics system with all the same options as windows currently have, and more. Ideally the only mode a user would ever need (under normal usage) would be hybrid, and intelligent algorithm would take care of the rest

Release plan:

  Major Release 1:
  
    - Switching between Integrated and Hybrid should be 100% seemless, without the need to restart X
    - Display-out should work in Hybrid mode
    - Auto prime-offload in Hybrid mode. Release 1 is likely to bring a configurable list under /etc, where user can specify programs, that should launch on dGPU, if available.
    - Manual prime-offload in integrated, if enabled in config. This means that in integrated, dGPU can temporarily be turned on, to run a single program, and immidiately be killed by the daemon, once the process has terminated
    - Automatic enabling of 'Hybrid' when external display connected in 'Integrated', if configured in config (details follow, dunno if actually possible, but I'll be damned if i don't try. This should again immidieatly kill the dGPU once displays are removed
    - Battery level, and geo-location features. This would allow users to set GPU rules based on battery status & level, as well as there physical location. I can imagine many would use hybrid (or in the future dedicated) at home, so having the computer automatically switch, would just be a quality of life improvement.
    
  Major Release 2:
    - I'm working on an idea for a set of custom drivers/plugins for Xorg. if succesfull, All running applications (including X-server) can be transfered seemless from 1 gpu to another*
    - with above mentioned technology all features in release 1 are going to be adapted, for an even more seemless process
    - Dedicated mode is also updated to be 100% seemless
    - Custom C-state implementation in Hybrid mode, allowing for aggresive dynamic power management
    (This release may not seem big, but trust me, switching x from running on iGPU to dGPU without restarting it, is going to be a challenge and a half)
    
Release schedule:
Given the sheer size and complexity of the problem at hand, I'm gonna cut myself a little slack, and decide that I'll have no release schedule.
I'm a high school student, meaning dependent on time at school, amount of homework, and demands from general social life, the amount of work i can put into this project will vary.
While I'll try my best to get things done asap, Major Release 1 and 2, might be a long time apart.

With the exact same reasoning I'm also gonna ask for your, the communitys, help. Bug patching is going to be an almost impossible job for me, so if you find a bug in the code, or the bug tracker, please try to patch it. I'll be more than happy to accept pull requests, knowing that for every one of them, this project gets a little better.


*The idea is to have a driver/plugin to spoof Xorg to send all render related data to a program of mine, which, in theory, should send the data to the decired GPU.
Step 2 would then be to copy the vRAM from one gpu to another, before switching. Of course this comes with some limitations, but if it works, it should open the doors for all new possibilities.
A check should, however, be implemented to ensure that copying doesn't happen whilst something like a game is running, since that would be too much vRAM, and overflow into system ram would be imminent, causing a massive performance hit, and potential crash.
