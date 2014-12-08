import mcpi.minecraft as minecraft,time as t,random as r
mc = minecraft.Minecraft.create()
x,y,z = mc.player.getPos()
wood = 5
air = 0
glass = 20
blackwool = 35,6
whitewool = 35,0
def clear(x,y,z):
    mc.setBlocks(x,y,z,x+20,y+20,z+20,air)
    
def Road(x,y,z):
    mc.setBlocks(x,y,z-5,x+6,y,z,blackwool)
    mc.setBlocks(x+1,y,z-3,x+3,y,z-3,whitewool)
def B_H(x,y,z):
    mc.setBlocks(x+1,y,z+1,x+6,y+5,z+8,wood)
    mc.setBlocks(x+2,y+1,z+2,x+5,y+4,z+7,air)
    mc.setBlocks(x+2,y+1,z+1,x+2,y+2,z+1,air)
    mc.setBlocks(x+3,y+2,z+1,x+5,z+1,glass)
    Road(x,y,z)
clear(x,y,z)
B_H(x,y,z)
B_H(x+7,y,z)
B_H(x+14,y,z)
B_H(x+21,y,z)
