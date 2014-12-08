import mcpi.minecraft as minecraft  #importing mcpi.minecraft and giving it the alius of minecraft
mc = minecraft.Minecraft.create()


def spaceinvader(xcorner,ycorner,zcorner,colour,background):
    wool = 35 #wool is defined
    mc.setBlocks(xcorner,ycorner,zcorner,xcorner+12,ycorner-9,zcorner,wool,background)
    y = ycorner
    for block in (-1,3,-1,4,-1,3,4,5,6,-1,2,3,5,6,-1,1,2,3,4,5,6,-1,1,3,4,5,6,-1,1,3,-1,4,5):
        if block == -1:
            y = y-1
        else:
            x = xcorner + block
            z = zcorner

            mc.setBlock(x,y,z,wool,colour)

            x = xcorner + 12 - block

            mc.setBlock(x,y,z,wool,colour)





red = 14 #red is defined to use with wool
blue = 11 #blue is defined to use with wool
black = 15 #black is defined to use with wool
green = 13 #green is defined to use with wool

mc.setBlocks(-30,-5,-30,30,30,30,0) #clears an area

spaceinvader(5,10,15,red,black)
spaceinvader(20,10,15,blue,green)

mc.player.setPos(30,30,30)

