function removeall --wraps='remove1 && remove2' --description 'alias removeall remove1 && remove2'
  remove1 && remove2 $argv; 
end
