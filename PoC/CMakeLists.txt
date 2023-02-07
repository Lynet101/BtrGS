cmake_minimum_required(VERSION 3.10)

# Project Name
project(GPU_Redirector)

# Add source files
set(SOURCES
    main.cpp
    gpu_redirector.cpp
)

# Add header files
set(HEADERS
    gpu_redirector.h
)

# Create the library
add_library(gpu_redirector SHARED ${SOURCES} ${HEADERS})

# Link the library to required libraries
target_link_libraries(gpu_redirector PRIVATE ${REQUIRED_LIBS})

# Make the library available for linking
set_target_properties(gpu_redirector PROPERTIES PUBLIC_HEADER "${HEADERS}")

# Install the library
install(TARGETS gpu_redirector
    LIBRARY DESTINATION lib
    PUBLIC_HEADER DESTINATION include
)
