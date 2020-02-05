import machine
import time

def run():
    p0 = machine.Pin(4, Pin.Out)

    while True:
        p0.on()
        time.sleep(1)
        p0.off()
        time.sleep(1)