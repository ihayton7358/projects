import mcpi.minecraft as minecraft, time
mc=minecraft.Minecraft.create()



mc.setBlocks(-30,-5,-30,30,30,30,0) #clears an area


#loops through 0-14 uses them for the y, x and z coord.
for b in range(0,14):
    mc.postToChat (b)
    mc.setBlock(0,b,0,35,b)
    mc.setBlock(b,0,0,35,b)
    mc.setBlock(0,0,b,35,b)
    mc.setBlock(0,-b,0,35,b)
    mc.setBlock(-b,0,0,35,b)
    mc.setBlock(0,0,-b,35,b)
    time.sleep(2)

