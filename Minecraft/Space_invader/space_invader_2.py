import mcpi.minecraft as minecraft  #importing mcpi.minecraft and giving it the alius of minecraft
mc = minecraft.Minecraft.create()

w = 35 #wool is defined
r = 14 #red is defined as 14 (to be used after wool)

mc.setBlocks(-30,-5,-30,30,30,30,0) #clears an area


mc.player.setPos(30,30,30)
xcorner = 15
ycorner = 10
zcorner = 15
mc.setBlocks(xcorner,ycorner,zcorner,xcorner+12,ycorner-9,zcorner,w,15)

for block in ((3,1),(4,2),(3,3),(4,3),(5,3),(6,3),(2,4),(3,4),(5,4),(6,4),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(1,6),(3,6),(4,6),(5,6),(6,6),(1,7),(3,7),(4,8),(5,8)):
    
    
    x = xcorner + block[0]
    y = ycorner - block[1]
    z = zcorner

    mc.setBlock(x,y,z,w,r)

    x = xcorner + 12 - block[0]

    mc.setBlock(x,y,z,w,r)
