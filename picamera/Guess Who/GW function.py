import picamera,time as t


def getPicture(name):
    Check = False
    if len(name) <= 0:
        print("no name given")
        t.sleep(.3)
        getPicture(input("what is your name?"))
    else:
        try:
            while Check == False:
                with picamera.PiCamera() as camera:
                    camera.resolution = (1024,768)
                    camera.start_preview()
                    t.sleep(2)
                    filename = ("{0}.jpeg".format(name))
                    camera.capture(filename)
                    camera.stop_preview()
                    
                    Check = input("are you happy with this picture? Y/N").lower()
                    if Check == "y" or Check == "yes":
                        Check = True
                    else:
                        Check = False
        except picamera.exc.PiCameraError:
            print("camera disconnected, check connection reboot pi and try again")
            filename = ""
        return filename
def getCharProf():
    fname = ""
    lname = ""
    hairCol = ""
    eyeCol = ""
    Gender = ""
    Hat = ""
    FacialHair = ""
    Glasses = ""
    Check0 = False
    Check1 = False
    Check2 = False
    Check3 = False
    Check4 = False
    Check5 = False
    Check6 = False
    GenderList = ["male","female"]
    hairColList = ["blue","black","brown","blonde","red"]
    eyeColList = ["blue","brown","hazel","green"]


    while fname == "" or lname == "" or Check0 == False:
        fname = input("What is your first name?")
        lname = input("What is your last name?")
        Check0 = input("is {0} {1} your name?Y/N".format(fname,lname)).lower()
        if Check0 == "y" or Check0 == "yes":
            Check0 = True

    fullname = ("{0} {1}".format(fname,lname))
    getPicture(fullname)


    while not (hairCol in hairColList) or Check1 == True:
        hairCol = input("what is {0}'s hair colour? Choose from {1}".format(fullname,hairColList)).lower()
        Check1 = input("are you sure?").lower
        if Check1 == "yes" or "y":
            Check = True
        else:
            Check1 = False


    while not (eyeCol in eyeColList) or Check2 == True:
        eyeCol = input("What is {0}'s eye colour? Choose from {1}".format(fullname,eyeColList)).lower()
        Check2 = input("Are you sure?").lower()
        if Check2 == "y" or "yes":
            Check2 = True
     
          

            
    while not (Gender in GenderList) or Check3 == True:
        Gender = input("what Gender is {0}? {1}".format(fullname,GenderList)).lower()
        Check3 = input("are you sure {0} is {1}?".format(fullname,Gender)).lower()
        if Check3 == "y" or "yes":
            Check3 = True

    while not Glasses == True or Glasses == False or Check4 == True:
        Glasses = input("does {0} wear glasses? y/n".format(fullname)).lower
        if Glasses =="y" or "yes":
            Glasses = True
        elif Glasses == "n" or "no":
            Glasses = False
        Check4 = input("are you sure?Y/N").lower()
        if Check4 == "y" or Check4 == "yes":
            Check4 = True

    while not FacialHair == True or FacialHair == False or Check5 == True:
        FacialHair = input("does{0} have any facial hair?".format(fullname)).lower()
        if FacialHair == "y" or "yes":
            FacialHair = True
        elif FacialHair == "n" or "no":
            FacialHair = False
        Check5 = input("are you sure?").lower
        if Check5 == "y" or "yes":
            Check5 = True


    while not Hat == True or Hat == False or Check6 == True:
        Hat = input("does {0} wear a hat?".format(fullname)).lower
        if Hat == "y" or "yes":
            Hat = True
        elif Hat == "n" or "no":
            Hat = False
        Check6 = input("are you sure?").lower
        if Check6 == "y" or "yes":
            Check6 = True
            
    profileList = [fullname,eyeCol,hairCol,Gender,Glasses,FacialHair]
    return profileList

        
        
        
    
