function reload --wraps='echo 1 > /sys/bus/pci/rescan' --description 'alias reload echo 1 > /sys/bus/pci/rescan'
  echo 1 > /sys/bus/pci/rescan $argv; 
end
