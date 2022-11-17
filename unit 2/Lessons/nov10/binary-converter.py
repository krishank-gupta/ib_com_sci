# Import pyfirmata library to program arduino using python
from pyfirmata import Arduino

# Function that validates input is between two numbers
def validate_int_between(msg, startNum, endNum):

    # Infinite loop that breaks when input is between startNum ad endNum
    while True:

        try:
            # ask for input
            val = int(input(f"{msg}: "))
            # if val is between start and end
            if endNum <= val >= startNum:
                # return val from function, breaks infinite while loop
                return val
            else:
                # non-interval error message
                print(f"Please enter a number between 0 and 7")
        
        except ValueError:
            # non-integer error message
            print(f"Please enter an integer")

# pyfirmata boiler plate
if __name__ == '__main__':
    
    # Init board variable according to usb port where arduino is connected
    board = Arduino('/dev/cu.usbserial-1420')
    # Print communication started message
    print("communication successfully started")
    
    # Init a,b,c that represents the 3 bits we need
    a=1
    b=1
    c=1
    
    # Infinite loop for continuosly blinking LEDs
    while True:
        # Get input from user and validate that it's between 0 and 7
        num = validate_int_between("Please enter a number between 0 and 7", 0, 7)
        
        # For i in 3bit range
        for i in range(0,8,1):

            # Switch a val every 4 iteration
            if i % 4 == 0:
                a = not a

            # Switch b val every 2 iteration
            if i % 2 == 0:
                b = not b
            
            # Switch c val every iteration
            c = i%2

            # Print bits for the input number
            if i == num:
                print(f"Number: {i}, binary: {int(a),int(b),int(c)}")
                # Turn on LEDs according to the bits
                board.digital[5].write(int(a))
                board.digital[9].write(int(b))
                board.digital[12].write(int(c))