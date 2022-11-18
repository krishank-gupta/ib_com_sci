import pyfirmata
from pyfirmata import Arduino
import time

board = Arduino('/dev/cu.usbserial-1420')
print("communication successfully started")

#Start iterator to receive input data
it = pyfirmata.util.Iterator(board)
it.start()

#Set up LEDs and buttton
buttonYes = board.digital[9]
buttonYes.mode = pyfirmata.INPUT
buttonYes_state = False

buttonNo = board.digital[1]
buttonNo.mode = pyfirmata.INPUT
buttonNo_state = False

LED = board.digital[2]
LED.write(0)

#Wait until button is pressed
while (not buttonNo_state) or (not buttonYes_state):
    #we run the loop at 10Hz
    time.sleep(0.01)
    print("waiting for the button to be pressed")
    buttonNo_state = buttonNo.read()
    buttonYes_state = buttonYes.read()

questions = []
answers = []

if buttonNo_state or buttonYes_state:
    for i in range(5):
        LED.write(1)
        time.sleep(1)
        LED.write(0)
        time.sleep(1)

exit()