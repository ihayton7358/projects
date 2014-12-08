import mcpi.minecraft as minecraft,  #importing mcpi.minecraft and giving it the alius of minecraft
mc = minecraft.Minecraft.create()

w = 35 #wool is defined
r = 14 #red is defined as 14 (to be used after wool)

mc.setBlocks(0,0,30,12,9,30,w,15) #clears an area to work in

#for each line of the space invader, a name is made equal to the block coordinates which need to be turned red
for block in (4,5,7,8):
    mc.setBlock(block,1,30,w,r)
for b in (1,3,9,11):
    mc.setBlock(b,2,30,w,r)
for bl in (1,3,4,5,6,7,8,9,11):
    mc.setBlock(bl,3,30,w,r)
for space in range (1,12):
    mc.setBlock(space,4,30,w,r)
for invader in (2,3,5,6,7,9,10):
    mc.setBlock(invader,5,30,w,r)
for game in range (3,10):
    mc.setBlock(game,6,30,w,r)
for pi in (4,8):
    mc.setBlock(pi,7,30,w,r)
for raspberry in (3,9):
    mc.setBlock(raspberry,8,30,w,r)
