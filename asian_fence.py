from numpy import *
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *

inputs =(("Circular Houce", "label"),("Material", alphaMaterials.StoneBricks))

def perform(level, box, options):
    print box.maxx, box.maxy, box.maxz
    print box.minx, box.miny, box.minz
    (width, height, depth) = utilityFunctions.getBoxSize(box)
    center_x = box.minx + width/2
    center_z = box.minz + depth/2
    size_x = width/6
    size_z = depth/6

    def wall(x,z):
        for j in range(6): #line_W
            if(j==0):
                for k in range(5): #line_H
                    utilityFunctions.setBlock(level, (5,4), x, box.miny+k, z)#red
                utilityFunctions.setBlock(level, (1,0), x, box.miny+7, z)#stone
            else:
                for k in range(5): #line_H
                    utilityFunctions.setBlock(level, (155,0), x+j, box.miny+k, z)#white
                    utilityFunctions.setBlock(level, (44,3), x+j, box.miny+7, z)#half_stone
            utilityFunctions.setBlock(level, (67,0), x+j, box.miny+6, z+1)#stairs
            utilityFunctions.setBlock(level, (67,0), x+j, box.miny+6, z-1)#stairs
            utilityFunctions.setBlock(level, (67,0), x+j, box.miny+5, z+2)#stairs
            utilityFunctions.setBlock(level, (67,0), x+j, box.miny+5, z-2)#stairs
            for s in range(3):
                utilityFunctions.setBlock(level, (5,4), x+j , box.miny+5, z-1+s)#red
        utilityFunctions.setBlock(level, (5,4), x+6 , box.miny+5, z-1)#red
        utilityFunctions.setBlock(level, (5,4), x+7 , box.miny+5, z-1)#red
        for i in range(6,8):
            utilityFunctions.setBlock(level, (67,0), x+j, box.miny+5, z-2)#stairs
            utilityFunctions.setBlock(level, (67,0), x+i, box.miny+6, z-1)#stairs

    def wall2(x,z):
        for j in range(6): #line_W
            if(j==0):
                for k in range(5): #line_H
                    utilityFunctions.setBlock(level, (5,4), x , box.miny+k, z)#red
                utilityFunctions.setBlock(level, (1,0), x , box.miny+7, z)#stone
            else:
                for k in range(5): #line_H
                    utilityFunctions.setBlock(level, (155,0), x , box.miny+k, z+j)#white
                    utilityFunctions.setBlock(level, (44,3), x , box.miny+7, z+j)#half_stone
            utilityFunctions.setBlock(level, (67,0), x+1 , box.miny+6, z+j)#stairs
            utilityFunctions.setBlock(level, (67,0), x-1 , box.miny+6, z+j)#stairs
            utilityFunctions.setBlock(level, (67,0), x+2 , box.miny+5, z+j)#stairs
            utilityFunctions.setBlock(level, (67,0), x-2 , box.miny+5, z+j)#stairs
            for s in range(3):
                utilityFunctions.setBlock(level, (5,4), x-1+s , box.miny+5, z+j)#red
        utilityFunctions.setBlock(level, (5,4), x-1, box.miny+5, z+6)#red
        utilityFunctions.setBlock(level, (5,4), x-1 , box.miny+5, z+7)#red
        for i in range(6,8):
            utilityFunctions.setBlock(level, (67,0), x-2, box.miny+5, z+j)#stairs
            utilityFunctions.setBlock(level, (67,0), x-1, box.miny+6, z+i)#stairs

    def corner(x,z):
        for i in range(3):
            utilityFunctions.setBlock(level, (67,0), x-2, box.miny+5, z-i)#stairs
        for i in range(2):
            utilityFunctions.setBlock(level, (67,0), x-1, box.miny+6, z-i)#stairs
            utilityFunctions.setBlock(level, (5,4), x-1 , box.miny+5, z-i)#red
        utilityFunctions.setBlock(level, (67,0), x-1, box.miny+5, z-2)#stairs
    """
    def corner2(x,z):
        for i in range(3):
            utilityFunctions.setBlock(level, (67,0), x-i, box.miny+5, z-2)#stairs
        for i in range(2):
            utilityFunctions.setBlock(level, (67,0), x-i, box.miny+6, z-1)#stairs
            utilityFunctions.setBlock(level, (5,4), x-i, box.miny+5, z-1)#red
        utilityFunctions.setBlock(level, (67,0), x-2, box.miny+5, z-1)#stairs
    """

    for a in range(size_x):
        x = box.minx + a*6
        corner(x, box.minz)
        corner(x, box.minz + size_z*6)
        wall(x, box.minz)
        wall(x, box.minz + size_z*6)

    for a in range(size_z):
        z = box.minz + a*6
        wall2(box.minx, z)
        wall2(box.minx + size_x*6, z)
        corner(box.minx, z)
        corner(box.minx + size_x*6, z)
