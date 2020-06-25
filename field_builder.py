from numpy import *
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *
from test import *

#
#
#error
#
#

class field:

    def __init__(self, level, start_x, start_y, start_z, size_x, size_z):
            self.level = level
            self.start_x = start_x
            self.start_y = start_y
            self.start_z = start_z
            self.size_x = size_x
            self.size_z = size_z

    def build(self):
        lv = self.level
        x = self.start_x
        y = self.start_y
        z = self.start_z
        s_x = self.size_x
        s_z = self.size_z

        for i in range(s_x):
            for j in range(s_z):
                setBlock(lv, x+i, y, z+j, 2, 0)
                setBlock(lv, x+i, y+1, z+j, 85, 0)
        
        for i in range(1, s_x-1):
            for j in range(1, s_z-1):
                setBlock(lv, x+i, y, z+j, 3, 0)
                #your favorite plants
                setBlock(lv, x+i, y+1, z+j, 31, 2) 
            setBlock(lv, x+s_x/2, y+1, z-1, 0, 0)
        
