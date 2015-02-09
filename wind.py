import time as t,math as m,RPi.GPIO as GPIO

pin = 17
speed = 0

def spin(channel1):
    global count
    count += 1
    print(count)

def calspeed():
    r = 9
    t = 5
    circ = r*m.pi
    speed = circ*count/t
    speed = speed/100000
    speed = speed*3600
    print("{0}km/h".format(speed))

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.IN,GPIO.PUD_UP)
GPIO.add_event_detect(pin,GPIO.FALLING,callback=spin,bouncetime=300)

while True:
    global count
    count = 0
    t.sleep(5)
    calspeed()
