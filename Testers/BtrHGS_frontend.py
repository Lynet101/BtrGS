from os import system as call
import BtrHGS_backend

switch = BtrHGS_backend.switch()
function_dictionary={'i2h':switch.i2h, 'i2d':switch.i2d, 'h2i':switch.h2i, 'h2d':switch.h2d, 'd2h':switch.d2h, 'd2i':switch.d2i}

def main():
    mode=input('what mode (i2h, i2d, h2i, h2d, d2h, d2i):' )
    print(function_dictionary[mode]())
    
if __name__ == '__main__':
    main()

