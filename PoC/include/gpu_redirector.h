#ifndef GPU_REDIRECTOR_H
#define GPU_REDIRECTOR_H

#include <string>

namespace gpu_redirector {

// Function to initialize the GPU Redirector Library
void init();

// Function to set the target GPU driver
void set_target_gpu(const std::string& driver_name);

// Function to start redirecting GPU rendering data from an application
void start_redirection();

// Function to stop redirecting GPU rendering data from an application
void stop_redirection();

} // namespace gpu_redirector

#endif // GPU_REDIRECTOR_H
