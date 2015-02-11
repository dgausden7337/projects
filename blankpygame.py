import RPi.GPIO as GPIO
import time, math

rainPin = 27
windPin = 17

rainCount = 0
windCount = 0

def bucketTippedSeconds(channel):
	global rainCount
	rainCount += 1

def bucketTipped(channel):
	global rainCount
	rainCount += 1
	print(rainCount)

def spin(channel):
	global windCount
	windCount += 1

def calcSpeed():
	speedCMpS = ((9 * math.pi) * windCount) / 5
	global speedKMpH
	speedKMpH = (speedCMpS / 100000) * 3600
	return speedKMpH

GPIO.setmode(GPIO.BCM)
GPIO.setup(rainPin, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(windPin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(rainPin, GPIO.FALLING, callback=bucketTippedSeconds, bouncetime=300)
GPIO.add_event_detect(windPin, GPIO.FALLING, callback=spin, bouncetime=300)

while True:
	windCount = 0
	rainCount = 0
	time.sleep(5)
	print("Rain Fall: " , rainCount * 0.2794)
	speedKMpH = calcSpeed()
	print("Wind Speed: " , speedKMpH)
		

input("Press enter to exit...")
import time, math

rainPin = 27
windPin = 17

rainCount = 0
windCount = 0

def bucketTippedSeconds(channel):
	global rainCount
	rainCount += 1

def bucketTipped(channel):
	global rainCount
	rainCount += 1
	print(rainCount)

def spin(channel):
	global windCount
	count += 1

def calcSpeed():
	speedCMpS = ((9 * math.pi) * windCount) / 5
	global speedKMpH
	speedKMpH = (speedCMpS / 100000) * 3600
	return speedKMpH

GPIO.setmode(GPIO.BCM)
GPIO.setup(rainPin, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(windPin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(rainPin, GPIO.FALLING, callback=bucketTippedSeconds, bouncetime=300)
GPIO.add_event_detect(windPin, GPIO.FALLING, callback=spin, bouncetime=300)

while True:
	windCount = 0
	time.sleep(1)
	print(rainCount * 0.2794)
	speedKMpH = calcSpeed()
	print("{0}".format(speedKMpH))
	print(windCount)
	time.sleep(4)

input("Press enter to exit...")
