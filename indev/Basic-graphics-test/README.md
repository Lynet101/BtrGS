The first attempt to switch between graphics, during execution, will be performed in vulkan

This is due to the fact that vulkan is a very low-level language, and provides lots of options for setup.
This is needed to 'simulate' a driver, and how a system-wide driver might behave, when processes are running.

The plan is simple: create a program, with very basic graphics, and a 'driver' in the back, that would allow for execution-hotswap
This would not only prove that the project is possible, but also give the general idea of how the project should work.