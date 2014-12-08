###minecraft teleporter

import time, random, mcpi.minecraft as m
mc = m.Minecraft.create()

time.sleep(1)
mc.postToChat("3")
time.sleep(1)
mc.postToChat("2")
time.sleep(1)
mc.postToChat("1")
time.sleep(1)
mc.postToChat("teleporting infinitely!")

while True:
    mc.player.setPos(20,99,40)
    time.sleep(2)
    mc.player.setPos(210,40,50)
    time.sleep(2)
    mc.player.setPos(40,50,144)
    time.sleep(1)
    
mc.postToChat("teleportation complete")






