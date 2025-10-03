import pyfirmata2 

port = "COM8"
board = pyfirmata2.Arduino(port)
led_pin = board.get_pin("d:3:o")

def led(total):
    if total==0:
        led_pin.write(0)
    elif total==5:
        led_pin.write(1)
      
