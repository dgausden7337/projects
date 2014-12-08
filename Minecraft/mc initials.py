import mcpi.minecraft as minecraft,time as t,random as r
mc = minecraft.Minecraft.create()

x,y,z = mc.player.getPos()

def D(x,y,z,c):
    mc.setBlocks(x+3,y,z,x+3,y+6,z,35,c)
    mc.setBlocks(x+4,y+6,z,x+6,y+6,z,35,c)
    mc.setBlocks(x+7,y+5,z,x+7,y+1,z,35,c)
    mc.setBlocks(x+6,y,z,x+4,y,z,35,c)


def G(x,y,z,v):
    mc.setBlocks(x+9,y+5,z,x+9,y+1,z,35,v)
    mc.setBlocks(x+10,y,z,x+12,y,z,35,v)
    mc.setBlocks(x+13,y+1,z,x+13,y+2,z,35,v)
    mc.setBlock(x+12,y+2,z,35,v)
    mc.setBlocks(x+10,y+6,z,x+12,y+6,z,35,v)

def I (x,y,z,b):
    mc.setBlocks(x+1,y,z,x+3,y,z,35,b)
    mc.setBlocks(x+1,y+6,z,x+3,y+6,z,35,b)
    mc.setBlocks(x+2,y,z,x+2,y+6,z,35,b)

for each in range(0,15):
    D(x,y,each,each)
    G(x,y,each,each)
