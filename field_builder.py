from numpy import *
import random
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

    def __init__(self, level, start_x, start_y, start_z, size_x, size_z, field_type):
            self.level = level
            self.start_x = start_x
            self.start_y = start_y
            self.start_z = start_z
            self.size_x = size_x
            self.size_z = size_z
            self.field_type = field_type

    def build(self):
        lv = self.level
        x = self.start_x
        y = self.start_y
        z = self.start_z
        s_x = self.size_x
        s_z = self.size_z

        l = random.randint(0,8)
        r = random.randint(0,8)
        while r==l:
            r = random.randint(0,8)

        if self.field_type is 0:
            for i in range(s_x):
                for j in range(s_z):
                    setBlock(lv, x+i, y, z+j, 2, 0)
                    setBlock(lv, x+i, y+1, z+j, 85, 0)
            for i in range(1, s_x-1):
                for j in range(1, s_z-1):
                    setBlock(lv, x+i, y, z+j, 3, 0)
                    #your favorite plants
                    setBlock(lv, x+i, y+1, z+j, 38, l) 
                setBlock(lv, x+s_x/2, y+1, z-1, 0, 0)

        elif self.field_type is 1:#I
            letter = [[0,0,0,0,0,0,0],[0,1,1,1,1,1,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,1,1,1,1,1,0],[0,0,0,0,0,0,0]]
            for i in range(9):
                for j in range(9):
                    setBlock(lv, x+i, y, z+j, 2, 0)
                    setBlock(lv, x+i, y+1, z+j, 85, 0)
            for i in range(7):
                for j in range(7):
                    setBlock(lv, x+i+1, y, z+j+1, 3, 0)
                    if letter[i][j]==0:
                        setBlock(lv, x+i+1, y+1, z+j+1, 38, l) 
                    elif letter[i][j]==1:
                        setBlock(lv, x+i+1, y+1, z+j+1, 38, r)
                setBlock(lv, x+9/2, y+1, z-1, 0, 0)
        elif self.field_type is 2:#C
            letter = [[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,1,0,0,0,1,0],[0,1,0,0,0,0,0],[0,1,0,0,0,1,0],[0,0,1,1,1,0,0],[0,0,0,0,0,0,0]]
            for i in range(9):
                for j in range(9):
                    setBlock(lv, x+i, y, z+j, 2, 0)
                    setBlock(lv, x+i, y+1, z+j, 85, 0)
            for i in range(7):
                for j in range(7):
                    setBlock(lv, x+i+1, y, z+j+1, 3, 0)
                    if letter[i][j]==0:
                        setBlock(lv, x+i+1, y+1, z+j+1, 38, l) 
                    elif letter[i][j]==1:
                        setBlock(lv, x+i+1, y+1, z+j+1, 38, r)
                setBlock(lv, x+9/2, y+1, z-1, 0, 0)
        elif self.field_type is 3:#E
            letter = [[0,0,0,0,0,0,0],[0,1,1,1,1,1,0],[0,1,0,0,0,0,0],[0,1,1,1,1,1,0],[0,1,0,0,0,0,0],[0,1,1,1,1,1,0],[0,0,0,0,0,0,0]]
            for i in range(9):
                for j in range(9):
                    setBlock(lv, x+i, y, z+j, 2, 0)
                    setBlock(lv, x+i, y+1, z+j, 85, 0)
            for i in range(7):
                for j in range(7):
                    setBlock(lv, x+i+1, y, z+j+1, 3, 0)
                    if letter[i][j]==0:
                        setBlock(lv, x+i+1, y+1, z+j+1, 38, l) 
                    elif letter[i][j]==1:
                        setBlock(lv, x+i+1, y+1, z+j+1, 38, r)
                setBlock(lv, x+9/2, y+1, z-1, 0, 0)