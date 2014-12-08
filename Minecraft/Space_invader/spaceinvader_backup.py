###make your own invader program###
import mcpi.minecraft as minecraft, time, random   #importing mcpi.minecraft and giving it the alius of minecraft, and imports time and random modules
mc = minecraft.Minecraft.create()   



colours = ["white","orange","magenta","light blue","yellow","lime","pink","grey","light grey","cyan","purple","blue","brown","green","red","black"]


#defines a function to convert the string the user inputs into a block id,
#it takes the parameter

def colourconvertor(colourstring):
        # converts the colourstring into lower case and removes spaces
    colourstring = colourstring.lower().strip()

    blockid = -1 #defines blockid as -1 so later we can see if it changes in the for loop
    
    
    for bid in range (0,len(colours)):   #bid (block id) is made equal to each string in colours
        if colourstring == colours[bid]:    #if what the user entered is in the colours list then blockid is made equal to the number of the colour in the colours list, and the loop is stopped 
            blockid = bid
            break

    if blockid == -1:    #if the blockid hasnt changed (because what was entered wasnt in the colours list) then a random colour is chosen
        blockid = random.randint(0, len(colours)-1)   #picks a random colour from the list
        print ("I didn't understand that, I'll just choose ..." +colours[blockid] +"!")   #prints what the random choice 

    return blockid    
     
       

    


#defines a function called drawmirroredblocks 
#takes the parameters of the coordinates, and the colour and background
#colour of the space invader, and the blocks to colour
def drawmirroredblocks(xcorner,ycorner,zcorner,colour,pixels):
    
    wool = 35 #wool is defined
    y = ycorner
    for block in pixels:
        if block <0:
            y = y+block    # when blocks are negative, the y coordiinate moves down by that number, so starting a new line
        else:
            x = xcorner + block  #if it isnt a negative, the numbers are used on the x coordinate 
            z = zcorner   #the z coordinate stays the same

            mc.setBlock(x,y,z,wool,colour)  #this only creates half the space invader

            x = xcorner + 12 - block   #mirrors the half the space invader to create a whole space invader

            mc.setBlock(x,y,z,wool,colour)     #sets the blocks with the new x coordinate to mirror the space invader, creating the whole space invader
            
def spaceinvader(xcorner,ycorner,zcorner,colour,background,speed): #draws an animated space invader
    wool = 35 #wool is defined
    mc.setBlocks(xcorner,ycorner,zcorner,xcorner+12,ycorner-9,zcorner,wool,background) #creates a rectangle which is the colour of the background the user chose
    pixels =(-1,3,-1,4,-1,3,4,5,6,-1,2,3,5,6,-1,1,2,3,4,5,6,-1,1,3,4,5,6,-1,1,3,-1,4,5) #the blocks that are the base shape of the space invader
    arms_up =(-2,1,-1,1,-1,1,-4,2)  #arms up extra blocks
    arms_down =(-6,1,-1,1,-1,4,5) #arms down extra blocks
       
    drawmirroredblocks(xcorner,ycorner,zcorner,colour,pixels) #draws whole space invader


    for count in range (0,10/speed):  #deletes one set of arms and draws the other, in a loop, making the space invader move, and an equal amount of time for each speed
        drawmirroredblocks(xcorner,ycorner,zcorner,colour,arms_up)                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        drawmirroredblocks(xcorner,ycorner,zcorner,background,arms_down)
        time.sleep(speed)
        drawmirroredblocks(xcorner,ycorner,zcorner,background,arms_up)                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        drawmirroredblocks(xcorner,ycorner,zcorner,colour,arms_down)
        time.sleep(speed)
        
    

while True:
    # asks what colour the user wants the space invader to be
    usercolour = raw_input ("what colour do you want the space invader to be?") 

    colour = colourconvertor(usercolour) #runs the function colourconvertor on the colour the user chose
            
    #asks the user what colour they want the background colour to be 
    userbackground = raw_input ("what colour background do you want it to have?")

    background = colourconvertor(userbackground)#runs the function colourconvertor on the background colour the user chose
     
    #asks the user what speed they want the space invader to move at
    userspeed = raw_input ("how fast do you want the space invader to move? Fast, medium or slow?")

    userspeed = userspeed.lower().strip() #makes what the user inputs lower case and removes spaces
    if userspeed == "fast":
        delay = 1
    elif userspeed == "medium":
        delay = 2
    elif userspeed == "slow":
        delay = 3
    else:
        print "I don't understand that, I'll just make it medium"
        delay = 1
        userspeed = "medium"
    


    print ("ok then, I'll make a space invader that is " +colours[colour] +"\nand has a background colour of " +colours[background]+"\nand moves at a " +userspeed+ " speed") #tells the user what colour the space invader will be
    pos = mc.player.getPos()  #gets the players position

    x = pos.x
    y = pos.y
    z = pos.z
    spaceinvader(x-5,y+10,z+6,colour,background,delay)    #runs the space invader function with the colour and background the user chose near where the player is standing
















