# Import pyfirmata library so that we can run python on arduino
from pyfirmata import Arduino
# Import time to use the sleep method
import time

# Python arduino syntax
if __name__ == '__main__':

    # Initialize board var according to usc serial port
    board = Arduino('/dev/cu.usbserial-1420')
    # Print connection success message on python terminal
    print("communication successfully started")
    
    # Init 3 variables a,b,c that will represent the 3 bits
    a=1
    b=1
    c=1
    
    # Infinite loop so the LEDs keep blinking
    while True:
        # For i in all possible combinations of 3 bits (2^3=8 so 0-7)
        for i in range(0, 8, 1):    
            # Switch a every 4 iterations
            if i % 4 == 0:
                a = not a
            # Switch b every 2 iterations
            if i % 2 == 0:
                b = not b
            # Switch c every iteration
            c = i%2

            # Write abc values to the 
            board.digital[5].write(int(a))
            board.digital[9].write(int(b))
            board.digital[12].write(int(c))
            # Stop for 1 second to have blink effect
            time.sleep(1)