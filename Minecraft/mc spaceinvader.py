import mcpi.minecraft as minecraft,time as t,random as r
mc = minecraft.Minecraft.create()
x,y,z = mc.player.getPos()


def Invader(x,y,z):#makes a space invader, not sure which part does which
    mc.setBlocks(x-5,y,z+10,x+6,y+8,z+10,35,15)
    mc.setBlocks(x-2,y+1,z+10,x+2,y+1,z+10,0)
    mc.setBlocks(x-4,y,z,x-4,y+2,z+10,0)
    mc.setBlock(x,y,z+10,0)
    mc.setBlocks(x+4,y,z+10,x+4,y+2,z+10,0)
    mc.setBlock(x-2,y+4,z+10,0)
    mc.setBlock(x+2,y+4,z+10,0)
    mc.setBlocks(x-5,y+5,z+10,x-5,y+8,z+10,0)
    mc.setBlocks(x-4,y+6,z+10,x-4,y+8,z+10,0)
    mc.setBlocks(x-3,y+6,z+10,x-3,y+7,z+10,0)
    mc.setBlocks(x-1,y+7,z+10,x+1,y+7,z+10,0)
    mc.setBlocks(x-2,y+8,z+10,x+2,y+8,z+10,0)
    mc.setBlocks(x+3,y+6,z+10,x+3,y+7,z+10,0)
    mc.setBlocks(x-5,y+5,z+10,x-5,y+8,z+10,0)
    mc.setBlocks(x+4,y+6,z+10,x+6,y+8,z+10,0)
    mc.setBlock(x+5,y+5,z+10,0)
    mc.setBlocks(x-6,y,z+10,x-6,y+8,z+10,0)


def blockade (x,y,z):#makes the blockade
    mc.setBlocks(x-7,y,z+10,x+7,y+10,z+10,35,5)#makes the basic shape

    mc.setBlocks(x-7,y+8,z+10,x-7,y+10,z+10,0)
    mc.setBlocks(x-6,y+9,z+10,x-6,y+10,z+10,0)
    mc.setBlock(x-5,y+10,z+10,0)#deletes the corner

    mc.setBlocks(x+7,y+8,z+10,x+7,y+10,z+10,0)
    mc.setBlocks(x+6,y+9,z+10,x+6,y+10,z+10,0)
    mc.setBlock(x+5,y+10,z+10,0)#deletes the corner

    mc.setBlocks(x-3,y,z+10,x+3,y+2,z+10,0)
    mc.setBlocks(x-2,y+3,z+10,x+2,y+3,z+10,0)#deletes the gap


def defender(x,y,z):#makes the defender
    mc.setBlocks(x-6,y,z+10,x+6,y+3,z+10,35,5)
    mc.setBlocks(x-5,y+4,z+10,x+5,y+4,z+10,35,5)
    mc.setBlocks(x,y+5,z+10,x,y+6,z+10,35,5)




def invaders(x,y,z):#puts everything together
    for each in range(-55,55,12):
        for ever in range(10,22,10):
            Invader(x+each,y+ever,z+20)#sets the invaders in a grid
    for each in range(-55,55,28):
        blockade(x+each,y-12,z+20)#sets the blockad along a line
    defender(x-10,y-20,z+20)#sets the defenders position


invaders(x,y,z)
#runs function around the player



