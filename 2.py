import RPi.GPIO as gp
import time

dac = [26,19,13,6,5,11,9,10]

gp.setmode(gp.BCM)

gp.setup(dac, gp.OUT)

pr = 8

maxval = 2**pr - 1

def nextval(a:int) -> int:
    if a < maxval:
        return a + 1
    else:
        return 0

def decToList(a:int) -> list:
    return [int(q) for q in bin(a)[2:].zfill(pr)]


try:
    a = 0
    period = 2

    while True:
        time.sleep(period)
        a = nextval(a)
        gp.output(dac, decToList(a))

finally:
    gp.output(dac, gp.LOW)
    gp.cleanup() 
