"""
As I'm currently more familiar with python, this is what the high-level implementations
of this library will be written in, during the proof of concept state

As stated in main.cpp, the final implementation is likely to be a driver anyways, and not
a library, so it doesn't really matter if the PoC has crap performance, it just needs
to work. And a Proof of Concept, is not a great time, to start learning new languages
like C (in which i have about 0 experience)
"""

import ctypes

# Load the GPU Redirector Library
gpu_redirector = ctypes.CDLL('./libgpu_redirector.so')

# Start the redirection
gpu_redirector.start_redirection()

# Pause to see the redirection in action
input("Press Enter to stop redirection...")

# Stop the redirection
gpu_redirector.stop_redirection()
