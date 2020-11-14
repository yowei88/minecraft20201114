from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y-1,z,46)