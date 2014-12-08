import mcpi.minecraft as minecraft, time as t
mc = minecraft.Minecraft.create()

#moves player close to origin
mc.player.setPos(10,10,0)

black=15
red=14
orange=1
green=5

#setup empty lights
for num in (1,2,3,4,5):
    mc.setBlock(0,num,0,35,black)
