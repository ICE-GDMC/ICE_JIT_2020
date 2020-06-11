from numpy import *
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from roofBuilder import *
from fifth_wall import *
from house_wallX import *
from house_wallZ import *
from test import *

displayName = "Asian Town"

inputs =(("Circular Houce", "label"),("Material", alphaMaterials.StoneBricks))

def perform(level, box, options):
    #print box.maxx, box.maxy, box.maxz
    #print box.minx, box.miny, box.minz
    (width, height, depth) = utilityFunctions.getBoxSize(box)
    

    """
    def floor(x,z):
        for i in range(1,8):
            for j in range(1,9):
                utilityFunctions.setBlock(level, (5,0), x+i, y, z+j)#floor

    def field(x,z,s_x,s_z):
        for i in range(s_x):
                for j in range(s_z):
                    utilityFunctions.setBlock(level, (2,0), x+i, y, z+j)
                    utilityFunctions.setBlock(level, (85,0), x+i, y+1, z+j)
                for i in range(1, s_x-1):
                    for j in range(1, s_z-1):
                        utilityFunctions.setBlock(level, (3,0), x+i, y, z+j)
                        #your favorite plants
                        utilityFunctions.setBlock(level, (31,2), x+i, y+1, z+j) 
                utilityFunctions.setBlock(level, (0,0), x+s_x/2, y+1, z-1)




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

    
    x = center_x + 8 #river + x
    y = box.miny+1
    #house create
    for i in range(5):
        wall(x,z+i*9) #x,z
        wall(x,z+i*9+9) #x,z
        wall2(x,z+i*9,1) #x,z,door
        wall2(x+8,z+i*9,0) #x,z,door
        floor(x,z+i*9)
        roof_builder = RoofBuilder(level, x, z+i*9, 10, y+5, 0, 0)
        roof_builder.build()
        z+=4
    
    x = center_x - 17 #river - x
    #house create
    for i in range(4):
        wall(x,z+i*9) #x,z
        wall(x,z+i*9+9) #x,z
        wall2(x,z+i*9,0) #x,z,door
        wall2(x+8,z+i*9,1) #x,z,door
        floor(x,z+i*9)
        roof_builder = RoofBuilder(level, x, z+i*9, 10, y+5, 0, 0)
        roof_builder.build()
        z+=4
    
    
    #field create
    y = box.miny
    field(x,box.minz,9,17)

    #tower create
    x = box.minx + 55
    z = box.minz + 20
    for i in range(5):
        d =[20, 15, 10, 5, 3]   #depth size
        y_height = [0, 4, 8, 12, 16]  #height 
        tower_wall = TowerWall(level, x + (d[0]/2-d[i]/2), box.miny+y_height[i],  z + (d[0]/2-d[i]/2), d[i])
        tower_wall.build()
        roof_builder = RoofBuilder(level, x + (d[0]/2-d[i]/2), z + (d[0]/2-d[i]/2), d[i], y+y_height[i]+4-1, 0, 1)
        roof_builder.build()
    """


    center_x = width/2 + box.minx
    x = center_x - 8
    z = box.minz

    for i in range(depth):
        gety = Test(level, x, box.maxy, z+i, height)
        y = gety.build()
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

