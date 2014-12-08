import mcpi.minecraft as minecraft#imports the minecraft module
mc = minecraft.Minecraft.create()#tells the program to use the current minecraft world/instance

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
#gets the players position and puts the coords in the corresponding variables
glass = 20
water = 9
air = 0
#sets the block codes for glass, water and air into their respective variables
mc.setBlocks(x,y,z-5,x+30,y+11,z+20,air)#sets the area the pool will appear in as air
mc.setBlocks(x,y,z+5,x+25,y+9,z+15,glass)#sets the glass around the pool
mc.setBlocks(x+1,y+1,z+6,x+24,y+9,z+14,water)#fills the glass with water
