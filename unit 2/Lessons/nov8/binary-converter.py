from pyfirmata import Arduino
import time

if __name__ == '__main__':
    board = Arduino('/dev/cu.usbserial-1420')
    print("communication successfully started")
    
    a=1
    b=1
    c=1
    
    while True:
        for i in range(0, 8, 1):    
            if i % 4 == 0:
                a = not a
            if i % 2 == 0:
                b = not b
            c = i%2
            board.digital[5].write(int(a))
            board.digital[9].write(int(b))
            board.digital[12].write(int(c))
            time.sleep(1)