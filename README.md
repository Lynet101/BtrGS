# BtrHGS
Better Hybrid Graphic Support for Linux
#############################################################################################

!!!Early development!!!

All code found in the current repo is highly experimental. The naming scheme is a bit random (I'll fix this very soon), and the code found is both messy, and buggy af (90% of it is probably broken xD)

Once i start getting features functioning stably, I'll move the experiments to a sepperate branch, and leave main for stable releases

#############################################################################################

This project aims to bring propper support for hybrid graphics to linux.

My goal is essentially to have a hybrid graphics system with all the same options as windows currently have, and more. Ideally the only mode a user would ever need (under normal usage) would be hybrid, and intelligent algorithm would take care of the rest

Release plan:

  Release 1:
  
    - Switching between Integrated and Hybrid should be 100% seemless, without the need to restart X
    - Display-out should work in Hybrid mode
    - Auto prime-offload in Hybrid mode, meaning applications that would benefit from the dGPU, automatically launches on it (like in windows)
    - Manual prime-offload in integrated, if enabled in config (details follow)
    - Automatic enabling of 'Hybrid' when external display connected in 'Integrated', if configured in config (details follow, dunno if actually possible, but I'll be damned if i don't try
    
  Release 2:
  
    - Switching between all modes seemless, without restart X
    - Custom C-state implementation in Hybrid mode, allowing for aggresive dynamic power management
    (This release may not seem big, but trust me, switching x from running on iGPU to dGPU without restarting it, is going to be a challenge and a half)
    
Release schedule:

Whenever I've made it :D

I mean, I'm essentially trying to do something, the linux community have been trying for a long, long time. It's gonna take some time, and i may not succed. 

Though i do hope that Release 1 will be publicly available start january, 2023 (this is however just a hope, and no promish what so ever. I'd rather do this right, rather than rush something out the door)
