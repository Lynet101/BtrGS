In order to ensure complete transfer of the application without issues, the process(es) should be paused completely [eg. kill -STOP] before attempting to transfer the program.

Vram can be cloned in advance, but modifying the program memory, and switching the process from one to another, should happen with the process paused. Once transfer is completed the process may resume [eg. kill -CONT]. This should ideally take a few milliseconds
