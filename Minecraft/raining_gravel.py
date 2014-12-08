import mcpi.minecraft as minecraft, time as t, random
mc=minecraft.Minecraft.create()

while True:

    pos = mc.player.getPos()
    x = int(pos.x)
    y = int(pos.y)
    z = int(pos.z)
    
    xg = random.randint(x-10,x+10)
    yg = y+50
    zg = random.randint(z-10,z+10)
    block = 13

    mc.setBlock(xg,yg,zg,block)

    t.sleep(0.2)
