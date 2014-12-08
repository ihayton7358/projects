###make your own space invader program###
import mcpi.minecraft as minecraft, time   #importing mcpi.minecraft and giving it the alius of minecraft, and imports time
mc = minecraft.Minecraft.create()

#defines a function to convert the string the user inputs into a block id,
#it takes the parameter colourstring
def colourconvertor(colourstring):
    #each colour of wool is defined for the user to choose
    white = 0
    orange = 1  
    magenta = 2  
    light_blue = 3  
    yellow = 4
    lime = 5 
    pink = 6  
    gray = 7  
    light_gray = 8  
    cyan = 9
    purple = 10
    blue = 11 
    brown = 12
    green = 13 
    red = 14 
    black = 15
    # converts the colourstring into lower case and removes spaces
    colourstring = colourstring.lower().strip()
    #users input is converted into a block id colour definition
    if colourstring == "orange":
        colour = orange 
    elif colourstring == "white":
        colour = white
    elif colourstring == "magenta":
        colour = magenta
    elif colourstring == "light blue":
        colour = light_blue
    elif colourstring == "yellow":
        colour = yellow
    elif colourstring == "lime":
        colour = lime
    elif colourstring == "pink":
        colour = pink
    elif colourstring == "gray" or colourstring == "grey":
        colour = grey
    elif colourstring == "light gray" or colourstring == "light grey":
        colour = light_gray
    elif colourstring == "cyan":
        colour = cyan
    elif colourstring == "purple":
        colour = purple
    elif colourstring == "blue":
        colour = blue
    elif colourstring == "brown":
        colour = brown
    elif colourstring == "green":
        colour = green
    elif colourstring == "red":
        colour = red
    elif colourstring == "black":
        colour = black
    else:
        print ("I don't understand, i'll just make it red")
        colour = red
    return colour  #returns the block id of the converted colour


#defines a function called buildspaceinvader 
#takes the parameters of the coordinates, and the colour and background
#colour of the space invader, and the blocks to colour
def buildspaceinvader(xcorner,ycorner,zcorner,colour,background,pixels):
    wool = 35 #wool is defined
    mc.setBlocks(xcorner,ycorner,zcorner,xcorner+12,ycorner-9,zcorner,wool,background) #creates a rectangle which is the colour of the background the user chose
    y = ycorner
    for block in pixels:
        if block == -1:
            y = y-1    # when block == -1, the y coordiinate moves down 1 so starting a new line
        else:
            x = xcorner + block  #if it doesnt == -1, the numbers are used on the x coordinate (this only creates half the space invader)
            z = zcorner   #the z coordinate stays the same

            mc.setBlock(x,y,z,wool,colour)  #sets each block that doesnt equal -1 to be the colour the user chose 

            x = xcorner + 12 - block   #mirrors the half the space invader to create a whole space invader

            mc.setBlock(x,y,z,wool,colour)     #sets the blocks with the new x coordinate to mirror the space invader
            
def spaceinvader(xcorner,ycorner,zcorner,colour,background):
    while True:
        pixels =(-1,3,-1,4,-1,3,4,5,6,-1,2,3,5,6,-1,1,2,3,4,5,6,-1,1,3,4,5,6,-1,1,3,-1,4,5)
        buildspaceinvader(xcorner,ycorner,zcorner,colour,background,pixels)
        time.sleep(1)
        pixels =(-1,3,-1,1,4,-1,1,3,4,5,6,-1,1,2,3,5,6,-1,1,2,3,4,5,6,-1,3,4,5,6,-1,3,-1,2)
        buildspaceinvader(xcorner,ycorner,zcorner,colour,background,pixels)
        time.sleep(1)
    
mc.setBlocks(-30,-5,-30,30,30,30,0) #clears an area
mc.player.setPos(11,0,0) #sets players position in front of where the sapce invader will be


# asks what colour the user wants the space invader to be
usercolour = raw_input ("what colour do you want the space invader to be?") 

colour = colourconvertor(usercolour) #runs the function colourconvertor on the colour the user chose
        
#asks the user what colour they want the background colour to be 
userbackground = raw_input ("what colour background do you want it to have?")

background = colourconvertor(userbackground)#runs the function colourconvertor on the colour the user chose


spaceinvader(5,10,15,colour,background)    #runs the space invader function with the colour and background the user chose




