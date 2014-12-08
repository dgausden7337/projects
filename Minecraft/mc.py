import mcpi.minecraft as minecraft,time as t,random as r
mc = minecraft.Minecraft.create()

mc.setBlocks(-30,-5,-30,30,30,30,0)

for b in (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14):
    mc.postToChat(b)
    mc.setBlock(0,b,0,35,b)
    t.sleep(2)
