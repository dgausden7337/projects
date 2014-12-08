##sos flasher by David G

import RPi.GPIO as GPIO,time as t

GPIO.setmode(GPIO.BOARD) #set the pin numbering system

GPIO.setup(11,GPIO.OUT)

#function definition
def dot():
	GPIO.output(11,False)
	t.sleep(1)
	GPIO.output(11,True)
	t.sleep(.5)



def dash():
	GPIO.output(11,False)
	t.sleep(3)
	GPIO.output(11,True)
	t.sleep(.5)

#defines each letter in the alphabet
def inspectorMorse(letter):
     if letter =="a":
                dot()
                dash()
     elif letter == "b":
             print("-...")
             dash()
             dot()
             dot()
             dot()
     elif letter == "c":
             print("-.-.")
             dash()
             dot()
             dash()
             dot()
     elif letter == "d":
             print("-..")
             dash()
             dot()()
             dot
     elif letter == "e":
             print("-")
             dot()
     elif letter == "f":
             print("..-.")
             dot()
             dot()
             dash()
             dot()
     elif letter == "g":
        print("--.")
        dash()
        dash()
        dot()
     elif letter == "h":
             print("....")
             dot()
             dot()
             dot()
             dot()
    elif letter == "i":
            print("


message = input("Enter message here") #takes the input
for each in message  #takes each character in the input
   inspectorMorse(each)
