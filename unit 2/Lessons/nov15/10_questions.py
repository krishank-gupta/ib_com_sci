import pyfirmata
from pyfirmata import Arduino
import time

questions = ["yes","no","yes","yes"]
answers = [1,0,1,1]

board = Arduino('/dev/cu.usbserial-1420')
print("communication successfully started")

#Start iterator to receive input data
it = pyfirmata.util.Iterator(board)
it.start()

#Set up LEDs and buttton
buttonYes = board.digital[9]
buttonNo = board.digital[4]
buttonYes.mode = pyfirmata.INPUT
buttonNo.mode = pyfirmata.INPUT

yesButton_state = False
noButton_state = False

LED = board.digital[2]
LED.write(0)

while not yesButton_state and not noButton_state:
    #we run the loop at 10Hz
    time.sleep(0.01)
    print("waiting for the button to be pressed")
    yesButton_state = buttonYes.read()
    noButton_state = buttonNo.read()

for idx,i in enumerate(questions):
    
    print(i)
    print("Press yes or no")
    
    if (answers[idx] == 1 and yesButton_state and not noButton_state) or (answers[idx] == 0 and not yesButton_state and noButton_state):
        print("Correct answer was pressed, blinking 5 times then exiting")
        for i in range(5):
            LED.write(1)
            time.sleep(1)
            LED.write(0)
            time.sleep(1)
    else:
        print("Wrong answer")

exit()