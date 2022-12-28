The goal is simple: Create a program that can transfer a gif between GPUs.
I mean, when broken down to it's basics, a gif can be looked at as a series of images. This means that if we render
an image on a gpu, the GPU technically does nothing, until the next picture is displayed. This also means that the 
images can rather easily be made independent of one another

Some of you might already see where I'm going. Because of the seperation, i won't have to transfer any vram, which is good, cause i 
dunno how to do that
And because of the periodical, rather than constant gpu usage, it *SHOULD* be easy to interupt the program, and start rendering of
the next picture, on a different GPU


I'm calling this my proof of concept (That's what PoC stands for, if you haven't catched it by now), because if I'm not even able to transfer a gif, which
once broken down like explained above, has got to be the easiest f****** thing, I probably will never be able to transfer more complex processes like xorg

Therefore, untill this succeds (if it ever will) I won't be going any more public than i already have. I also won't be looking into recruting help,
nor will i open up for any sort of donations, or anything of that caliber. 
I want to ensure the plausability of this, before getting tons of people involved, and especially before i even consider accepting other peoples money.
