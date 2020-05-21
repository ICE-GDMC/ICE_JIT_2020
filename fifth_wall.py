from numpy import *
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *

displayName = "Tower Wall"

inputs =(("Circular Houce", "label"),("Material", alphaMaterials.StoneBricks))

class TowerWall:
    def __init__(self, level, x, y, z, depth):
        self.level = level
        self.x = x
        self.y = y
        self.z = z
        self.depth = depth

    def run(self):
        lv = self.level
        x = self.x
        y = self.y
        z = self.z
        d = self.depth

        for i in range(d):
            if (i==0 or i==d-1):
                for j in range(4):
                    setBlock(lv, x, y+j, z+i, 17, 1)
                    setBlock(lv, x+d-1, y+j, z+i, 17, 1)
            else:
                for j in range(4):
                    setBlock(lv, x, y+j, z+i, 12, 0)
                    setBlock(lv, x+d-1, y+j, z+i, 12, 0)
                    setBlock(lv, x+i, y+j, z, 12, 0)
                    setBlock(lv, x+i, y+j, z+d-1, 12, 0)

'''
def perform(level, box, options):
    print box.maxx, box.maxy, box.maxz
    print box.minx, box.miny, box.minz
    (width, height, depth) = utilityFunctions.getBoxSize(box)

    for i in range(5):
        d = [20, 15, 10, 5, 3]    #depth size
        x = box.minx + (d[0]/2-d[i]/2)
        y_height = [0, 5, 10, 15, 20]  #height 
        z =  box.minz + (d[0]/2-d[i]/2)
        tower_wall = TowerWall(level, x, box.miny+y_height[i], z, d[i])
        tower_wall.run()
'''