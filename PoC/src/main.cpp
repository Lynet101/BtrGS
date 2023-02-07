//All mid- and low-level stuff will be written in c++ for the Proof of Concept.
//Final product is likely to be a driver anyways, and not a library, so it doesn't really
//matter if performance is horse sh**

#include "gpu_redirector.h"
#include <iostream>

int main() {
  gpu_redirector::init();

  std::cout << "Enter the name of the target GPU driver: ";
  std::string target_gpu;
  std::cin >> target_gpu;

  gpu_redirector::set_target_gpu(target_gpu);
  gpu_redirector::start_redirection();

  std::cout << "Press any key to stop redirection..." << std::endl;
  getchar();

  gpu_redirector::stop_redirection();

  return 0;
}
