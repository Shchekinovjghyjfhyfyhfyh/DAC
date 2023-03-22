

import RPi.GPIO as gp

import time





dac = [26,19,13,6,5,11,9,10]

# portin = 3

portou = 2

frec = 10

gp.setmode(gp.BCM)

# gp.setup(dac, gp.OUT)

gp.setup(portou, gp.OUT)

# gp.setup(portin, gp.IN)





pr = 8

maxval = 2**pr - 1

period = 0.1





def decToList(a:int) -> list:
    return [int(q) for q in bin(a)[2:].zfill(pr)]





gp.output(portou, gp.OUT)

pwm = gp.PWM(portou, frec)





try:
    while True:
        a = int(input())/1000
        if not (0 <= a <= 1):
            raise Exception('coef is out')

        pwm.start(a*100)
# print(gp.input(3))
        time.sleep(period)
        pwm.stop()

finally:
    gp.output(portou, gp.LOW)
    gp.cleanup()
