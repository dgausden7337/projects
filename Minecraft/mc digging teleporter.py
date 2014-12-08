import mcpi.minecraft as minecraft,time as t#imports the minecraft and time modules
mc = minecraft.Minecraft.create()#tells the program to use the currnet minecraft world/instance


while True:#loops infinitely 
     mc.player.getPos()
     x = pos.x
     y = pos.y
     z = pos.z
     #gets players position and puts each coord into corresponding variables
while y<-10: 
     
     mc.player.setPos(x,56,z)#if the player reaches -10 on the y axis, he is teleported up
