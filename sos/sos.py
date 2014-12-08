import RPi.GPIO as GP, time  #importing file RPi.GPIO and calling it GP, importing time
GP.setmode(GP.BOARD)
GP.setup(11,GP.OUT)

def dot() :                  #defining a function called dot which gives a short flash
    GP.output(11,GP.HIGH)
    time.sleep(0.2)
    GP.output(11,GP.LOW)
    time.sleep(0.4)

def dash() :                 #defining a function called dash which gives a longer flash
    GP.output(11,GP.HIGH)
    time.sleep(0.7)
    GP.output(11,GP.LOW)
    time.sleep(0.4)

def morse_letter(letter):    #defines a function called morse_letter which takes the parameter letter, each letter is then translated into dashes and dots
    if letter == "a":                                                                                                            
        dot()
        dash()
    elif letter == "b":
        dash()
        dot()
        dot()
        dot()
    elif letter == "c":
        dash()
        dot()
        dash()
        dot()
    elif letter == "d":
        dash()
        dot()
        dot()
    elif letter == "e":
        dot()
    elif letter == "f":
        dot()
        dot()
        dash()
        dot()
    elif letter == "g":
        dash()
        dash()
        dot()
    elif letter == "h":
        dot()
        dot()
        dot()
    elif letter == "i":
        dot()
        dot()
    elif letter == "j":
        dot()
        dash()
        dash()
        dash()
    elif letter == "k":
        dash()
        dot()
        dash()
    elif letter == "l":
        dot()
        dash()
        dot()
        dot()
    elif letter == "m":
        dash()
        dash()
    elif letter == "n":
        dash()
        dot()
    elif letter == "o":
        dash()
        dash()
        dash()
    elif letter == "p":
        dot()
        dash()
        dash()
        dot()
    elif letter == "q":
        dash()
        dash()
        dot()
        dash()
    elif letter == "r":
        dot()
        dash()
        dot()
    elif letter == "s":
        dot()
        dot()
        dot()
    elif letter == "t":
        dash()
    elif letter == "u":
        dot()
        dot()
        dash()
    elif letter == "v":
        dot()
        dot()
        dot()
        dash()
    elif letter == "w":
        dot()
        dash()
        dash()
    elif letter == "x":
        dash()
        dot()
        dot()
        dash()
    elif letter == "y":
        dash()
        dot()
        dash()
        dash()
    elif letter == "z":
        dash()
        dash()
        dot()
        dot()
    else:
        print ("what?")


usersletter = input("Which letter do you want?")      # asks the user to write (input) which letter they want

morse_letter(usersletter)                   #use the function morse_letter on what the user inputted 
