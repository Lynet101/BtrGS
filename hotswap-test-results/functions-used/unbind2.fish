function unbind2 --wraps='echo "0000:01:00.1" > /sys/bus/pci/devices/0000:01:00.0/driver/unbind' --wraps='echo "0000:01:00.1" > /sys/bus/pci/devices/0000:01:00.1/driver/unbind' --description 'alias unbind2 echo "0000:01:00.1" > /sys/bus/pci/devices/0000:01:00.1/driver/unbind'
  echo "0000:01:00.1" > /sys/bus/pci/devices/0000:01:00.1/driver/unbind $argv; 
end
