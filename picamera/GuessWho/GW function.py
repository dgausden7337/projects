import picamera,time as t,json
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
    filename = getPicture(fullname)#cretes their fullname and runs getPicture function with it

    Check0 = False

    while not (hairCol in hairColList):#if the haircol is not in list or they are not happy run this
        while Check0 == False:
            hairCol = input("what is {0}'s hair colour? Choose from {1}".format(fullname,hairColList)).lower()#asks for their hair colour
            Check0 = input("are you sure?").lower()#checks if they are sure
            if Check0 == "yes" or "y":
                Check0 = True
     
    Check0 = False

    while not (eyeCol in eyeColList) or Check0 == False:#if the eyeCol is not in list or they are not happy run this
        eyeCol = input("What is {0}'s eye colour? Choose from {1}".format(fullname,eyeColList)).lower()#asks for eye Col
        Check0 = input("Are you sure?Y/N").lower()#asks if they are happy
        if Check0 == "y" or "yes":
            Check0 = True
     
    Check0 = False      

    
    while not (Gender in GenderList) or Check0 == False:#if gender is not in list or they not happy run again
        Gender = input("what Gender is {0}? {1}".format(fullname,GenderList)).lower()#
        Check0 = input("are you sure {0} is {1}?".format(fullname,Gender)).lower()
        if Check0 == "y" or "yes":
            Check0 = True
    Check0 = False
    while not Glasses == True or False or Check0 == False:
        Glasses = input("does {0} wear glasses? y/n".format(fullname)).lower
        if Glasses =="y" or "yes":
            Glasses = True
        elif Glasses == "n" or "no":
            Glasses = False
        else:
            Glasses = ""
        Check0 = input("are you sure?Y/N").lower()
        if Check0 == "y" or Check4 == "yes":
            Check0 = True
    Check0 = False
    while not FacialHair == True or False or Check0 == False:
        FacialHair = input("does{0} have any facial hair?".format(fullname)).lower()
        if FacialHair == "y" or "yes":
            FacialHair = True
        elif FacialHair == "n" or "no":
            FacialHair = False
        Check0 = input("are you sure?").lower
        if Check0 == "y" or "yes":
            Check0 = True
    Check0 = False

    while not Hat == True or False or Check0 == False:
        Hat = input("does {0} wear a hat?".format(fullname)).lower
        if Hat == "y" or "yes":
            Hat = True
        elif Hat == "n" or "no":
            Hat = False
        Check0 = input("are you sure?").lower
        if Check0 == "y" or "yes":
            Check0 = True
            
    profile = [fullname,eyeCol,hairCol,Gender,Glasses,FacialHair,filename]
    return profile
    
def loadProfiles():
    try:
        with open("profiles.txt",mode="r",encoding="utf-8") as p:
            profiles = json.load(p)
            print(profiles)
    except IOError:
        print("profiles.txt not found. Creating new profile")
        
        profiles = []
        
        saveProfile()
def saveProfile(profiles):
    profile = getCharProf()
    profiles.append(profile)
    with open("profiles.txt",mode="w",encoding="utf-8") as p:
        json.dump(profiles,p)
    
