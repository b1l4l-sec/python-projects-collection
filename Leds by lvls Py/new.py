import pyfirmata2 
import time


port = "COM8"
board = pyfirmata2.Arduino(port)
led_pin_1 = board.get_pin("d:3:o")
led_pin_2 = board.get_pin("d:4:o")
led_pin_3 = board.get_pin("d:5:o")
led_pin_4 = board.get_pin("d:6:o")
led_pin_5 = board.get_pin("d:7:o")

while True :
    state = input("Enter from (0) to (5) to controll the leds by lvl : ")
    if state == "0" :
        led_pin_1.write(0)
        led_pin_2.write(0)
        led_pin_3.write(0)
        led_pin_4.write(0)
        led_pin_5.write(0)
    # time.sleep(1)
    elif state == "1" :
        led_pin_1.write(1)
        led_pin_2.write(0)
        led_pin_3.write(0)
        led_pin_4.write(0)
        led_pin_5.write(0)
    # time.sleep(1)
    elif state == "2" :
        led_pin_1.write(1)
        time.sleep(0.1)
        led_pin_2.write(1)
        led_pin_3.write(0)
        led_pin_4.write(0)
        led_pin_5.write(0)
    # time.sleep(1)
    elif state == "3" :
        led_pin_1.write(1)
        time.sleep(0.1)
        led_pin_2.write(1)
        time.sleep(0.1)
        led_pin_3.write(1)
        led_pin_4.write(0)
        led_pin_5.write(0)
    # time.sleep(1)
    elif state == "4" :
        led_pin_1.write(1)
        time.sleep(0.1)
        led_pin_2.write(1)
        time.sleep(0.1)
        led_pin_3.write(1)
        time.sleep(0.1)
        led_pin_4.write(1)
        led_pin_5.write(0)
    # time.sleep(1)
    elif state == "5" :
        led_pin_1.write(1)
        time.sleep(0.1)
        led_pin_2.write(1)
        time.sleep(0.1)
        led_pin_3.write(1)
        time.sleep(0.1)
        led_pin_4.write(1)
        time.sleep(0.1)
        led_pin_5.write(1)
    # time.sleep(1)
    else :
        print("Enter just from 0 to 5 nothing else please <3")

board.exit()