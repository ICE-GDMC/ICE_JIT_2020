from numpy import *
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *

inputs =(("Circular Houce", "label"),("Material", alphaMaterials.StoneBricks))

def perform(level, box, options):
    print box.maxx, box.maxy, box.maxz
    print box.minx, box.miny, box.minz
    (width, height, depth) = utilityFunctions.getBoxSize(box)
    size_x = width/6
    size_z = depth/6


    def wall(x,z):
        for j in range(6): #line_W
            if(j==0):
                for k in range(5): #line_H
                    utilityFunctions.setBlock(level, (5,4), x, box.miny+k, z)#red
            else:
                for k in range(5): #line_H
                    if k==3:
                        utilityFunctions.setBlock(level, (5,4), x+j, box.miny+k, z)#red
                    else:
                        utilityFunctions.setBlock(level, (155,0), x+j, box.miny+k, z)#white


    def wall2(x,z):
        for j in range(6): #line_W
            if(j==0):
                for k in range(5): #line_H
                    utilityFunctions.setBlock(level, (5,4), x , box.miny+k, z)#red
            else:
                for k in range(5): #line_H
                    if k==3:
                        utilityFunctions.setBlock(level, (5,4), x , box.miny+k, z+j)#red
                    else:
                        utilityFunctions.setBlock(level, (155,0), x , box.miny+k, z+j)#white

    for a in range(size_x):
        x = box.minx + a*6
        wall(x, box.minz)
        wall(x, box.minz + size_z*6)

    for a in range(size_z):
        z = box.minz + a*6
        wall2(box.minx, z)
        wall2(box.minx + size_x*6, z)
    
    for k in range(5): #line_H
        utilityFunctions.setBlock(level, (5,4), box.minx + size_x*6, box.miny+k, box.minz + size_z*6)#red
