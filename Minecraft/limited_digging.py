import mcpi.minecraft as minecraft, time as t
mc = minecraft.Minecraft.create()

mc.postToChat ("hello")

while True:
    
    pPos = mc.player.getPos()
    x = pPos.x
    y = pPos.y
    z = pPos.z

    if y < -2:
        mc.player.setPos (x+1, y+20,z+1)
        mc.postToChat("no!")
        
