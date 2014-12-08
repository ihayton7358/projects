def get():
    TotalCheck = False
    
    eye_colour = ""
    while not(eye_colour.lower().strip() in("blue","brown","green","grey","hazel")):
            eye_colour = input("What is your eye colour?")
        
    hair_colour = ""
    while not(hair_colour.lower().strip() in ("brown","black","blonda","red","ginger")):
            hair_colour = input("What colour is your hair?").lower().strip()
            print hair_colour
   

