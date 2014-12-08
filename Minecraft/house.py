import mcpi.minecraft as minecraft, time
mc = minecraft.Minecraft.create()

mc.setBlocks(-30,-5,-30,30,30,30,0)
playerpos = mc.player.getPos()

x = playerpos.x
y = playerpos.y
z = playerpos.z


#making house
mc.setBlocks(x+1,y,z+1,x+6,y+3,z+8,45)
mc.setBlocks(x+2,y,z+2,x+5,y+2,z+7,0)

#door
mc.setBlocks(x+1,y,z+3,x+1,y+1,z+3,0)

#windows
mc.setBlock(x+1,y+1,z+5,20)
mc.setBlock(x+1,y+1,z+7,20)
mc.setBlock(x+2,y+1,z+1,20)
mc.setBlock(x+5,y+1,z+1,20)
mc.setBlock(x+6,y+1,z+3,20)
mc.setBlock(x+6,y+1,z+5,20)
mc.setBlock(x+6,y+1,z+7,20)
mc.setBlock(x+3,y+1,z+8,20)
mc.setBlock(x+5,y+1,z+8,20)


