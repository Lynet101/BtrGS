function unbind1 --wraps='echo "0000:01:00.0" > /sys/bus/pci/devices/0000:01:00.0/driver/unbind' --description 'alias unbind1 echo "0000:01:00.0" > /sys/bus/pci/devices/0000:01:00.0/driver/unbind'
  echo "0000:01:00.0" > /sys/bus/pci/devices/0000:01:00.0/driver/unbind $argv; 
end
