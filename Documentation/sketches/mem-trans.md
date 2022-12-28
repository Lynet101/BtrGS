Some memory will need to be transfered around to make this work

Vram will need to be moved/copied to the second gpu in order for execution to continue like normal

Program memory and/or arguments will likely also need to be modified to specify the new gpu, and disable any potentially incompatible features (like cuda functionality on amd)

