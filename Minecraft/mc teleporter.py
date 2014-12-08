import time,mcpi.minecraft as minecraft,random as r#imports the time, minecraft and random modules
mc = minecraft.Minecraft.create()#tells the program to use the current minecraft world/instance

def coordinates():#sets a func to create random coords and give them to the program
    x = r.randint(0,256)
    y = r.randint(0,256)
    z = r.randint(0,256)
    return x,y,z
while True:#loops infinitely
    time.sleep(3)
    x,y,z = coordinates()#takes the coords and sets them as x,y,z
    mc.postToChat("Teleportation in 3")
    time.sleep(1)
    mc.postToChat("Teleportation in 2")
    time.sleep(1)
    mc.postToChat("Teleportation in 1")
    mc.player.setPos(x,y,z)#teleports them to a random location
    time.sleep(1)
    mc.player.setPos(x,y,z)
    time.sleep(1)
    mc.player.setPos(x,y,z)
    time.sleep(1)
    mc.postToChat("Teleport complete")
