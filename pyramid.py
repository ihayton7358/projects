import mcpi.minecraft as minecraft, time as t
mc = minecraft.Minecraft.create()



def drawpyramid(xorigin,yorigin,zorigin,material):

    for a in range (0,11):
        xmin = xorigin-a
        xmax = xorigin+a
        zmin = zorigin-a
        zmax = zorigin+a
        y = yorigin-a
    

        mc.setBlocks(xmin,y,zmin,xmax,y,zmax,material,a)

for layer in range (30,20,-1):
    
    drawpyramid(30,layer,30,35)
   
    
