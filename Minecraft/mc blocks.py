import mcpi.minecraft as minecraft,time as t
mc = minecraft.Minecraft.create()


for block in (0,-2,-4,-6,-8,-10):
    mc.setBlock(0,11,block,22)
    mc.postToChat(block)
    t.sleep(1)






















