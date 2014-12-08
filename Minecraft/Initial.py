import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

wool = 35

pos = mc.player.getPos()

xpos = pos.x
ypos = pos.y
zpos = pos.z


def I (x,y,z):
    mc.setBlocks(x+2,y,z,x+2,y+6,z+2,wool,14)
    mc.setBlocks(x+2,y+1,z,x+2,y+5,z,0)
    mc.setBlocks(x+2,y+1,z+2,x+2,y+5,z+2,0)

def R (x,y,z):
    mc.setBlocks(x+2,y,z+4,x+2,y+6,z+8,wool,14)
    mc.setBlocks(x+2,y,z+5,x+2,y+2,x+8,0)
    mc.setBlocks(x+2,y+4,z+5,x+2,y+5,z+7,0)
    mc.setBlock(x+2,y,z+8,wool,14)
    mc.setBlock(x+2,y+1,z+7,wool,14)
    mc.setBlock(x+2,y+2,z+6,wool,14)
    mc.setBlock(x+2,y+3,z+8,0)
    mc.setBlock(x+2,y+6,z+8,0)

def H (x,y,z):
    mc.setBlocks(x+2,y,z+10,x+2,y+6,z+14,wool,14)
    mc.setBlocks(x+2,y,z+11,x+2,y+6,z+13,0)
    mc.setBlocks(x+2,y+3,z+11,x+2,y+3,z+13,wool,14)

I (xpos,ypos,zpos)
R (xpos,ypos,zpos)
H (xpos,ypos,zpos)
