function remove2 --wraps='echo 1 > /sys/bus/pci/devices/0000:01:00.1/remove' --description 'alias remove2 echo 1 > /sys/bus/pci/devices/0000:01:00.1/remove'
  echo 1 > /sys/bus/pci/devices/0000:01:00.1/remove $argv; 
end
