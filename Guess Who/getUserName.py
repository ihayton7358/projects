


def getUserName():
    check = False

    while check == False:
        name = input("What is your name?")
        name = name.strip()
        validation =input ("Your name is {0}, is this the name you want to use?".format(name) .format(name))  
        if validation.lower().strip() == "yes" or "y":
            check = True
            print ("Ok, your name is {0}".format(name))
        else:
            check = False
