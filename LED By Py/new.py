import pyfirmata2 
import time


port = "COM8"
board = pyfirmata2.Arduino(port)
led_pin = board.get_pin("d:3:o")

while True :
    state = input("Enter (on) or (off) to controll the led : ")
    if state == "on" :
        led_pin.write(1)
    # time.sleep(1)
    elif state == "off" :
        led_pin.write(0)
    # time.sleep(1)
    else :
        print("Enter just on or off nothing else please <3")

board.exit()