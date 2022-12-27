# BtrHGS
Better Hybrid Graphic Support for Linux
################################################################################

!!!Early development!!!

All code found in the current repo is highly experimental. Code found in 'BtrHGS Function Collection..." is just a collection of all the functions, for a quick way for me to see how all functions are gonna tie together. NOT MENT FOR EXECUTION EVER!

################################################################################

Hybrid graphics have always been a pain in the *ss to work with on linux. Either the internal disp isn't working, or the external, and you constantly have to restart either x or your entire system.... Urgh!

Though it's not just linux. Yes linux is probably the most difficult (we have nvidia to thanks for that), but hybrid graphics on say windows, isn't exactly elegant either. 

The goal of this project is to attempt to come up with an elegant solution for this. Whilst some releases will happen, the goal of the project is not to create a product for the end user, but to discover and document the technique, so the community can create their own hybrid graphics systems, with the feautres they wish for

Currently i have worked out how to (without any processes in the picture) turn switch between integrated, hybrid and dedicated mode seemless. That also means that, if X is started in integrated, you can actually switch to hybrid without restarting x (just don't expect dispay out to work) and back again to integrated of course.

Now the big problem has, unfortunately, arrived. A technique needs to be developed to allow for the transfer of processes between GPUs. If this is succesfull, seemless switching would become 100% possible, and dare i say it? easy. It would allow you to take any running process, and transfer it to a different gpu, without interupting the process (other than possibly pausing it for a few milliseconds, but we'll talk a obout that later)

--------------------------------------------------------------------------------

This is just the current draft for a memory technique, that'll allow me to develop the rest of the system, and probably not the final memory solution, as it's slow and ineffecient AF;

The current plan is to, when switching, create a copy of the vram, on the second gpu. After creating the copy, doing some magic mumbo jumbo, and after all processes are running on the new card, release the old cards vram, and power it down.

Again, that is just for development, as there are.... Issues, to put it mildly. I mean just imagine a scenario, you're playing a game. It uses around 3GB of vram. Now you're switching to your iGPU (for whatever reason) without closing your game... Chances are your iGPU doesn't have 3GB of vram, meaning we have to overflow into regular ram, which is just terrible, and will most likely cause a crash.

So let's all just agree, to not do that in the development face shall we? Only attempt this memory method, on lighter applications like a web-browser, whilst the rest of the methods for transferring apps between gpus are developed

--------------------------------------------------------------------------------

Lastly if you have any ideas/suggestions to how this could be achieved, please do open a issue. It would be great to hear from you! might also make a subreddit in the future, but I'm a high school student, so time isn't something a have a lot of
