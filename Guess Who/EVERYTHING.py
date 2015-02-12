#This file contains all the functions required for Guess Who
    
import picamera, time, json  #imports all these modules

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
                if response.lower() == "yes" or "y":   #if they say yes then check is true so it isnt run again
                    check = True  #check is made true if the user is ok with the picture
                elif response.lower() == "no" or "n":
                    check = False
    except (picamera.exc.PiCameraMMALError, picamera.exc.PiCameraValueError, picamera.exc.PiCameraError, picamera.exc.PiCameraRuntimeError):
        print ("There was an error. Check the camera is\nplugged in and you entered valid name, and then restart.")
        filename = ""    #if there is an error the filename is set to nothing, so something is returned
    return filename

    
    
    

def getProfile():
    
    name = ""
    while name == "":    #does the following while name is empty
        name = input("What is your name?")  #gets the users name

    filename = getUserImage(name)     #uses the getUserImage function and stores the result as filename

    gender = ""  
    while not(gender.lower().strip() in("girl","boy")):      #only accepts yes or no
        gender = input("Are you a girl or a boy?")   #gets the users answer

    hat = ""
    while not(hat.lower().strip() in ("yes","no","y","n")):     #only accepts yes or no
        hat = input("Are you wearing a hat?")      #gets the user answer
    
    eye_colour = ""
    while not(eye_colour.lower().strip() in("blue","brown","green","grey","hazel")): #only accepts certain eye colours
            eye_colour = input("What is your eye colour?")  #gets the users answer
        

    hair_colour = ""
    while not(hair_colour.lower().strip() in ("brown","black","blonde","red","ginger", "purple", "grey")):#only accepts certain hair colours
            hair_colour = input("What colour is your hair?")  #gets the users answer
        
    facial_hair = ""
    while not(facial_hair.lower().strip() in ("yes","no","y","n")):     #only accepts yes or no
        facial_hair = input("Do you have any facial hair? yes/no") #gets the users answer

    glasses = ""
    while not(glasses.lower().strip() in ("yes","no","y","n")):     #only accepts yes or no
        glasses = input("Do you have glasses?")    #gets the users answer

    return [name, filename, gender, hat, eye_colour, hair_colour, facial_hair] #returns a list of the data collected 

def load():
    try:    
        with open("PeopleData", mode="r")as file:    #opens the PeopleData file in read mode and calls it file
            people = json.load(file)     #defines people as the data in the file
        

    except (IOError, ValueError):     #if the try doesn't work, this happens
        print("there was an error")   #prints a friendly message to the user
        people = []    #sets people to be an empty list
    return people  



def store():
    person = getProfile()    #uses the getProfile function to get the variable "person"
    people.append(person)   #adds the data from person to the people list 
    with open("PeopleData", mode="w") as file:    #opens the data file in write mode and calls it file
        json.dump(people,file)    #puts the data from the people list into the file

people = load()


    
            

    




 



