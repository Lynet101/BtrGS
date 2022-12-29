A few basic OpenGL test, to get experience with the API, and test how far i can come, just by tingering around with API calls. So let me explain the namings:

----------------------------------------------------------------------------------
## Basic-tests with single-gpu-rendering:  
I've been an AI-developer up untill this point, so my experience lie mainly with cuda. Unfortunately cuda is not really the tool to get the job done, when talking about graphical rendering accross multiple different vendors, so opengl it is!
Only one tiny problem, I've never worked with opengl before, so this folder is me figuring out how that works (on a single gpu, baby steps people)


## Basic-tests with multi-gpu-rendering:  
Once I've figured out how to draw a white rectagle, It's time to see if i can draw to simultaneously (I know, excitting!), but on different GPUs. By doing this I'll learn how to manage and interact with multiple GPUs which is pretty crucial for this project to work


## Basic-tests with multi-gpu-'cheaty'-switchable-rendering:  
Pretty self explanatory except the cheatty part. Basically I'm gonna try to imitate a gif, by rendering one frame on one gpu, once rendering is complete imidiately pause execution and switch rendering function from gpu1 to gpu2, then resume execution, and start rendering of the next photo on the new gpu.  

I call this 'cheaty' because whilst this is basically what I'm going for, the fact that i allow the rendering to finish, basically means i can just tread it as a series of individual renders on multiple gpus, meaning all i have to worry about is making the program not crash, when the window gets a new gpu


## Basic-tests with multi-gpu-switchable-rendering:  
With all of my culminated knowledge from above experiment, I'm now gonna attempt to stop rendering of a picture, half way through, and then proceed with the second half on the second gpu.
I also won't be sending any data to the display, before rendering is completed (so i won't get a half rendered picture).
This'll force me to copy vram and framebuffers between the two gpus, and will make the first gpu-execution hotswap in history (as far as I'm aware)

------------------------------------------------------------------------------------
After this point, I'll go out with my proof, and my concepts, in an attempt to get a team of developers, hopefully a bit smarter than me, so we can all collaborate to make a very basic switch, basically ignoring all problems that might could occur, into the best graphical solution the world has ever seen!!!! (alright, that might be overexsaturated, but you get the point)
