#include "gpu_redirector.h"
#include <iostream>

namespace gpu_redirector {

void init() {
  std::cout << "Initializing GPU Redirector Library" << std::endl;
}

void set_target_gpu(const std::string& driver_name) {
  std::cout << "Setting target GPU driver to: " << driver_name << std::endl;
}

void start_redirection() {
  std::cout << "Starting GPU data redirection" << std::endl;
}

void stop_redirection() {
  std::cout << "Stopping GPU data redirection" << std::endl;
}

} // namespace gpu_redirector
