function unbindall --wraps='unbind1 && unbind2' --description 'alias unbindall unbind1 && unbind2'
  unbind1 && unbind2 $argv; 
end
