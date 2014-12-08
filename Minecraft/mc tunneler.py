#a program to destroy any block around you
import mcpi.minecraft as minecraft#imports the minecraft module
mc = minecraft.Minecraft.create()#tells the program to use the current minecraft world/instance



while True:#creates an infinite loop
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    #gets the players position and puts the coords in teh corresponding variables
    air = 0
    #sets the block code for air and puts it in it's respective variable
    mc.setBlocks(x+1,y,z+1,x-1,y+2,z-1,air)
    #sets each block surrounding the player to air
    

