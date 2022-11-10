from pyfirmata import Arduino

val = 0

def validate_int_between(msg, startNum, endNum):
    while True:
        try:
            val = int(input(f"{msg}: "))
            if val >= startNum and val <= endNum:
                return val
            else:
                print(f"Please enter a number between 0 and 7")
        except ValueError:
            print(f"Please enter an integer")

if __name__ == '__main__':

    board = Arduino('/dev/cu.usbserial-1420')
    print("communication successfully started")
    
    a=1
    b=1
    c=1
    
    while True:
        num = validate_int_between("Please enter a number between 0 and 7", 0, 7)
        
        for i in range(0,8,1):
            if i % 4 == 0:
                a = not a
            if i % 2 == 0:
                b = not b
            c = i%2

            if i == num:
                print(f"Number: {i}, binary: {int(a),int(b),int(c)}")
                board.digital[5].write(int(a))
                board.digital[9].write(int(b))
                board.digital[12].write(int(c))