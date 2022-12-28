# BtrHGS
BtrHGS is a project that aims to bring Better Hybrid Graphics Support to linux.

It takes a brand new approach to switching GPUs, by trying to 'move' processes between GPUs before switching, rather than relying on a restart of X or the system, to kill all processes before switching may happen.

This projects original intent is hybrid graphics systems on linux, but if succesfull this technology could be deployed any where from optimus-systems to data centers.

That is IF it's succesfull. I've read a lot of documentation online, and been unable to find a similar project, meaning what this project tries to accomplish is brand new and revolutionary, but also that it's going to be difficult af.

I'm gonna try my very best to bring this idea to reallity, and i strongly believe, that with the help of this great community, we can atleast get part of the way there. However i just have to make this disclaimer: I'm a high school student, with knowledge and experience in coding. I've worked for larger international corporations before, and developed things like AIs. Though I am in no way a 'professional', so don't expect miracles. Also, since I'm in highschool, I don't really have all the time in the world to look at this project. So from the beginning im gonna say; Given the complexity of the problem at hand, and given the current status of the team (that being a single, time constrained person) I won't make any promises for any releases. New documentation and releases will happen, whenever I've discovered something new, and had time to work with it proberly.

If you wan't to contribute, head into 'indev' for more info
---------------------------------------------------------------------------------------
IMPORTANT!!

In the folder PoC I'm going to create a small proof of concept
More details can be found in the readme inside the folder but, the TL;DR is
that I'm not going to spread anymore public knowledge, recrute developers, nor consider
donations of any sort, until i've made that. Before getting a ton of people involved, 
and especially before taking peoples money, i want to make sure that this project is 
feasable, and i want to be able to proof that to both you and i

I understand that this might slow down initial dev a bit, but i hope for your understanding
of my motives


---------------------------------------------------------------------------------------

I've devided the project up in folders, to try and make things a bit easier to navigate. In every folder there's a readme file, containing that folders structure

As this is a bleeding edge project, a lot of documentation, and a lot of code samples a going to be generated, by which only approx. 10% are likely to be used, so having a good archival structure has been important for me, to maintain transparency.
The aim is to maintain as transparent as possible with what's going on, to allow people to, not only know where it's at, but also contribute to the project, and bring ideas, bug fixes, or just small tips on how you can do something smarter/easier/faster

As this project is going to move memory around, and is most likely going to modify the kernel at some point, security should also be kept a high priority. Hince why i have 'testing-tools' 'Developmental-builds' and 'User-builds'. Anything not found in 'User-builds' are not tested proberly, and are likely to contain major security flaws that, if exploited, could lead to all sorts of issues like corruption, spying, etc.

--------------------------------------------------------------------------------------

Lastly, in an attempt to stay ahead of potential system-destroying bugs, i stronly encourage people to reflect over what they read in the project, and open issues whenever they've found a potential bug, that needs to be taken into acountanse to ensure that processes won't break, and data won't corrupt when moving gpus
