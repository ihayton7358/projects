import mcpi.minecraft as minecraft, time as t
mc = minecraft.Minecraft.create()

#moves player close to origin
mc.player.setPos(10,10,0)

black=15
red=14
orange=1
green=5

#setup empty lights
for num in (0,1,2,3,4,5):
    mc.setBlock(0,num,0,35,black)

#infinitely loops the traffic light sequence
while True:
    mc.setBlock(0,5,0,35,red)

    t.sleep(10)
    mc.setBlock(0,4,0,35,orange)

    t.sleep(2)
    mc.setBlock(0,5,0,35,black)
    mc.setBlock(0,4,0,35,black)
    mc.setBlock(0,3,0,35,green)

    t.sleep(10)
    mc.setBlock(0,4,0,35,orange)
    mc.setBlock(0,3,0,35,black)

    t.sleep(2)
    mc.setBlock(0,4,0,35,black)


