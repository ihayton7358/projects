def getCharProfile():
    CHECK = False
    while CHECK == False:
        name = input("What is your name")

        

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
            facial_hair = input("Do you have any facial hair? yes/no")

        if facial_hair == "yes":
                  hair_type = ""
                  while not(hair_type.lower().strip() in ("beard","moustache")):
                            hair_type = input("What type of facial hair do you have?")

        glasses = ""
        while not(glasses.lower().strip() in ("yes","no")):
            glasses = input("Do you have glasses?")

        return [name, gender, hat, eye_colour, hair_colour, facial_hair, hair_type]
        check = input("Is this correct?")
        if check.lower().strip() == "yes":
            CHECK = True
            
