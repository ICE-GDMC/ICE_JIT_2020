from numpy import *
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *


"""
displayName = "test"

inputs =(("Circular Houce", "label"),("Material", alphaMaterials.StoneBricks))


def perform(level, box, options):
    print box.maxx, box.maxy, box.maxz
    print box.minx, box.miny, box.minz
    (width, height, depth) = utilityFunctions.getBoxSize(box)

def gety(x, y, z):
    for i in range(height):
        ID = level.blockAt(x, y-i, z)
        if ID == 2:
            return y-i
        else:
            print '--------------------'


center_x = width/2 + box.minx
x = center_x - 8
z = box.minz

for i in range(depth):
    y = gety(x,box.maxy,z+i)
    #sand
    for j in range(4): #0~4
        utilityFunctions.setBlock(level, (12,0), x+j, y, z+i)
        utilityFunctions.setBlock(level, (2,0), x+j, y-1, z+i)
        for k in range(y+1, box.maxy):
            utilityFunctions.setBlock(level, (0,0), x+j, k, z+i)
    for j in range(12,16): #12~15
        utilityFunctions.setBlock(level, (12,0), x+j, y, z+i)
        utilityFunctions.setBlock(level, (2,0), x+j, y-1, z+i)
        for k in range(y+1, box.maxy):
            utilityFunctions.setBlock(level, (0,0), x+j, k, z+i)
    #stone
    for j in range(4,12): #4~11
        if (j==4 or j==11):
            for k in range(4):
                utilityFunctions.setBlock(level, (1,0), x+j, y-k, z+i)
        else:
            utilityFunctions.setBlock(level, (0,0), x+j, y, z+i)  
            for k in range(2):
                utilityFunctions.setBlock(level, (9,0), x+j, y-1-k, z+i)        
            utilityFunctions.setBlock(level, (1,0), x+j, y-3, z+i)
        for k in range(y+1, box.maxy):
            utilityFunctions.setBlock(level, (0,0), x+j, k, z+i)

"""

class Test:
    def __init__(self, level, start_x, start_y, start_z, height):
        self.level = level
        self.start_x = start_x
        self.start_y = start_y
        self.start_z = start_z
        self.height = height

    def build(self):
        lv = self.level
        x = self.start_x
        y = self.start_y
        z = self.start_z
        h = self.height
        
        ID = 0
        while(ID != 2):
            for i in range(h):
                ID = lv.blockAt(x, y-i, z)
                if ID == 2: 
                    break
            z += 1
        
        return y-i
            