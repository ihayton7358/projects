#This file contains all the functions required for Guess Who
    
import picamera, time

def getPicture(name):

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
                print (filename + "captured")#prints the name of the file
                response = input("Is the picture ok?")#asks the user if the photo is ok
                if response.lower() == "yes":   #if they say yes then check is true so it isnt run again
                    check = True  #check is made true if the user is ok with the picture

    except picamera.exc.PiCameraRuntimeError:   #if the camera isn't detected it doesn't post an error message
        print ("Camera not connected.\nPlease connect and restart.")
        filename = ""





  

