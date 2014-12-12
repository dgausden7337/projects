import picamera,time as t
#imports the modulez needed

#defines getPicture function
def getPicture(name):
    Check = False
    #creates variable
    #checks you have name
    if len(name) <= 0:
        print("no name given")
        t.sleep(.3)
        getPicture(input("what is your name?"))
        #runs function with name
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
                    #tries to take picture
                    Check = input("are you happy with this picture? Y/N").lower()
                    if Check == "y" or Check == "yes":
                        Check = True
                    else:
                        Check = False
                        #check if they are happy with picture
        except picamera.exc.PiCameraError:
            print("camera disconnected, check connection reboot pi and try again")
            filename = ""
            #if no camera run this
        return filename
    #return what the file is called
#defines getCharProf function
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
#creates variables and lists needed

    while fname == "" or lname == "" or Check0 == False:
        fname = input("What is your first name?")#asks for first name
        lname = input("What is your last name?")#asks for last nane
        Check0 = input("is {0} {1} your name?Y/N".format(fname,lname)).lower()
        if Check0 == "y" or Check0 == "yes":
            Check0 = True
#ensures they are correct
    fullname = ("{0} {1}".format(fname,lname))
    getPicture(fullname)#cretes their fullname and runs getPicture function with it


    while not (hairCol in hairColList):#if the haircol is not in list or they are not happy run this
        while Check1 == False:
            hairCol = input("what is {0}'s hair colour? Choose from {1}".format(fullname,hairColList)).lower()#asks for their hair colour
            Check1 = input("are you sure?").lower()#checks if they are sure
            if Check1 == "yes" or "y":
                Check1 = True
     


    while not (eyeCol in eyeColList) or Check2 == False:#if the eyeCol is not in list or they are not happy run this
        eyeCol = input("What is {0}'s eye colour? Choose from {1}".format(fullname,eyeColList)).lower()#asks for eye Col
        Check2 = input("Are you sure?Y/N").lower()#asks if they are happy
        if Check2 == "y" or "yes":
            Check2 = True
     
          

            
    while not (Gender in GenderList) or Check3 == False:#if gender is not in list or they not happy run again
        Gender = input("what Gender is {0}? {1}".format(fullname,GenderList)).lower()#
        Check3 = input("are you sure {0} is {1}?".format(fullname,Gender)).lower()
        if Check3 == "y" or "yes":
            Check3 = True

    while not Glasses == True or not Glasses == False or Check4 == False:
        Glasses = input("does {0} wear glasses? y/n".format(fullname)).lower
        if Glasses =="y" or "yes":
            Glasses = True
        elif Glasses == "n" or "no":
            Glasses = False
        else:
            Glasses = ""
        Check4 = input("are you sure?Y/N").lower()
        if Check4 == "y" or Check4 == "yes":
            Check4 = True

    while not FacialHair == True or not FacialHair == False or Check5 == False:
        FacialHair = input("does{0} have any facial hair?".format(fullname)).lower()
        if FacialHair == "y" or "yes":
            FacialHair = True
        elif FacialHair == "n" or "no":
            FacialHair = False
        Check5 = input("are you sure?").lower
        if Check5 == "y" or "yes":
            Check5 = True


    while not Hat == True or not Hat == False or Check6 == False:
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

def loadProfiles():
    with open("profiles.txt","
