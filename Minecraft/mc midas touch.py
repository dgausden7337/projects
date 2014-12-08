import mcpi.minecraft as minecraft,time as t#imports the minecraft and time modules
mc = minecraft.Minecraft.create()#tells the program to use the current minecraft world/instance

while True:#loops infinitely
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
#gets the player's position and puts each coord into a variable
    gold = 41#puts the block code for gold as the variable 'gold'
    mc.setBlock(x,y-1,z,gold)#sets the last block he touched, as gold
    
    #sleep the wole process before starting it again.
