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
y = ycorner
for block in (-1,3,-1,4,-1,3,4,5,6,-1,2,3,5,6,-1,1,2,3,4,5,6,-1,1,3,4,5,6,-1,1,3,-1,4,5):
    if block == -1:
        y = y-1
    else:
        x = xcorner + block
        z = zcorner

        mc.setBlock(x,y,z,w,r)

        x = xcorner + 12 - block

        mc.setBlock(x,y,z,w,r)
