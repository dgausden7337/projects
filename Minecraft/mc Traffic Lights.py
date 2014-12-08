#a program to make a traffic light system in minecraft.
import mcpi.minecraft as minecraft,time as t #imports the modules minecraft and time
mc = minecraft.Minecraft.create()#tells the program to use the current minecraft world/instance

def redon(): #defines function for setting red to 'on' and amber to 'off'
    mc.setBlock(78,19,101,35,red)
    mc.setBlock(78,17,101,35,black)

def redamber(): #defines function for setting red, amber to 'on'
    mc.setBlock(78,19,101,35,red)
    mc.setBlock(78,17,101,35,orange)

def Greenon(): #defines function for setting green to 'on' and redamber to 'off'
    mc.setBlock(78,15,101,35,green)
    mc.setBlock(78,17,101,35,black)
    mc.setBlock(78,19,101,35,black)

def amber(): #defines function for setting amber to 'on' and  green to 'off'
    mc.setBlock(78,17,101,35,orange)
    mc.setBlock(78,15,101,35,black)



black=7
red=14
orange=1
green=5
#sets the block code for each colour as a variable, so you dont have to remember the block code
mc.setBlock(78,8,101,35,black)
mc.setBlock(78,9,101,35,black)
mc.setBlock(78,10,101,35,black)
mc.setBlock(78,11,101,35,black)
mc.setBlock(78,12,101,35,black)
mc.setBlock(78,13,101,35,black)
mc.setBlock(78,14,101,35,black)
mc.setBlock(78,15,101,35,black)
#set each block used to black, resetting the traffic light system
while True:
    redon()
    t.sleep(5)
    redamber()
    t.sleep(3)
    Greenon()
    t.sleep(5)
    amber()
    t.sleep(4)
#loops the traffic light system infinitely
