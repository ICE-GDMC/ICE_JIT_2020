from numpy import *
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *

inputs =(("Circular Houce", "label"),("Material", alphaMaterials.StoneBricks))

def perform(level, box, options):
    print box.maxx, box.maxy, box.maxz
    print box.minx, box.miny, box.minz
    (width, height, depth) = utilityFunctions.getBoxSize(box)

    center_x = width/2 + box.minx
    x = center_x-15
    y = box.miny
    z = box.minz

    #clean
    for i in range(30):
        for j in range(depth):
            for k in range(1,10):
                utilityFunctions.setBlock(level, (0,0), x+i, y+k, z+j)
            utilityFunctions.setBlock(level, (2,0), x+i, y, z+j)

    #create road
    x = center_x - 8
    for i in range(depth):
        #sand
        for j in range(6): #0~4
            if(j==0 or j==5):
                utilityFunctions.setBlock(level, (4,0), x+j, y, z+i)
            else:
                utilityFunctions.setBlock(level, (1,0), x+j, y, z+i)
