import mcpi.minecraft as minecraft,time as t,random as r
mc = minecraft.Minecraft.create()
while True:#creates an infinite loop
    pos = mc.player.getPos()#gets player position
    x = pos.x#sets x coord into the x variable
    y = pos.y#sets y coord into the Y variable
    z = pos.z#sets z coord into the z variable
    Gravel = 13#sets gravel ID to variable gravel
    a = r.randint(-25,25)#sets variable a as a random number
    b = r.randint(-25,25)#sets variable b as a random number
    mc.setBlock(x+a,50,z+b,Gravel)#sets the gravel blocks
    #pauses for 2 tenths of a second
