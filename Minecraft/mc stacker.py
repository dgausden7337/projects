import mcpi.minecraft as minecraft,time as t,random as r#import minecraft, time and random modules
mc = minecraft.Minecraft.create()

mc.setBlocks(-30,-5,-30,30,30,30,0)#sets large area as air

for b in (range(15)):#creates a finite loop
    mc.postToChat(b)#posts to chat each number in the list
    mc.setBlock(b+2,b,0,35,b)#sets a stack of blocks with differing codes
    t.sleep(2)#pauses for 2 seconds
