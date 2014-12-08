import time, picamera
name = input("What is your Name?")

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    for filename in camera.capture(name+".jpeg"):
        print("Captured %s" % filename)
        time.sleep(10)
