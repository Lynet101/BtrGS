function remove1 --wraps='echo 1 > /sys/bus/pci/devices/0000:01:00.0/remove' --description 'alias remove1 echo 1 > /sys/bus/pci/devices/0000:01:00.0/remove'
  echo 1 > /sys/bus/pci/devices/0000:01:00.0/remove $argv; 
end
