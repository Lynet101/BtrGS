Bash-syntax will be used to decribe the workflow in different stages (&, &&), as this is more an overview to myself, so i won't put too much effort into this

Stage 1)
	Per-process GPU-control(no HS) & PCI-hotswap experiments (not with GPU)

Stage 2)
	beta PCI-HS implementation && GPU-hotswap && crash data collection

stage 3)
	Bug-bashing & mem-transfer && further gpu-hotswap test

stage 4)
	final implementation of PCI-hotswap driver(no gpu yet) && continuos development of GPU HS

stage 5)
	release of GPU on-demand HS

stage 6)
	release of PCI, 'real HS', that is hotswapping devices without requesting to remove them

stage 7 (maybe))
	release of GPU 'real HS' (probably only usefull for enterprise)
