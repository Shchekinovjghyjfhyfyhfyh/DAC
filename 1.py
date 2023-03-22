import RPi.GPIO as gp

dac = [26,19,13,6,5,11,9,10]

gp.setmode(gp.BCM)

gp.setup(dac, gp.OUT)

pr = 8

maxval = 2**pr - 1



def decToList(a:int) -> list:
    return [int(q) for q in bin(a)[2:].zfill(pr)]



try:

    while True:
        val = input()

        if val == 'q':
            break

        if not val.isdigit():
            raise Exception('Input is not value')
        if '.' in val:23
            raise Exception('Input value is not integral')
        val = int(val)
        if val < 0:
            raise Exception('Input value is negative')
        if val > maxval:
            raise Exception('Input value is too high')


        print(f'volt: {val/maxval*3.3:.2}V')

        gp.output(dac, decToList(val))
finally:
    gp.output(dac, gp.LOW)
