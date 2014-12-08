#This file contains all the functions required for Guess Who
    
import picamera, time

def getUserImage(name):
    
    try:
        with picamera.PiCamera() as cam:
            check = False   #sets check to false
            while check == False: #while check is false loops....
                cam.resolution = (1024,768)  #sets the resolution of the picture
                cam.start_preview()   #starts the preview of the picture
                time.sleep(3)
                filename = "{0}.jpg".format(name) #filename is the parameters of the cam.capture
                cam.capture(filename) #runs the parameters of filename on the cam.capture function
                cam.stop_preview() #stops the preview
                print (filename + " captured")#prints the name of the file
                response = input("Is the picture ok?")#asks the user if the photo is ok
                if response.lower() == "yes":   #if they say yes then check is true so it isnt run again
                    check = True  #check is made true if the user is ok with the picture
    except (picamera.exc.PiCameraMMALError, picamera.exc.PiCameraValueError):
        print ("There was an error. Check the camera is\nplugged in and you entered valid name, and restart.")
        filename = ""
    return filename
    
    
    

def getCharProfile():

    name = input("What is your name")

    filename = getUserImage(name)

    gender = ""  
    while not(gender.lower().strip() in("girl","boy")):
        gender = input("Are you a girl or a boy?")

    hat = ""
    while not(hat.lower().strip() in ("yes","no")):
        hat = input("Are you wearing a hat?")
    
    eye_colour = ""
    while not(eye_colour.lower().strip() in("blue","brown","green","grey","hazel")):
            eye_colour = input("What is your eye colour?")
        
    hair_colour = ""
    while not(hair_colour.lower().strip() in ("brown","black","blonda","red","ginger")):
            hair_colour = input("What colour is your hair?")
        
    facial_hair = ""
    while not(facial_hair.lower().strip() in ("yes","no")):
        facial_hair = input("Do you have any facial hair? Y/N")

    if facial_hair == "yes":
              hair_type = ""
              while not(hair_type.lower().strip() in ("beard","moustache")):
                        hair_type = input("What type of facial hair do you have?")

    glasses = ""
    while not(glasses.lower().strip() in ("yes","no")):
        glasses = input("Do you have glasses?")

    return [name, filename, gender, hat, eye_colour, hair_colour, facial_hair, hair_type]

    




 



