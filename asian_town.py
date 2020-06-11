from numpy import *
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from roofBuilder import *
from fifth_wall import *
from road_builder import *
from house_wallX import *
from house_wallZ import *
from field_builder import *
from test import *

displayName = "Asian Town"

inputs =(("Circular Houce", "label"),("Material", alphaMaterials.StoneBricks))

def perform(level, box, options):
    #print box.maxx, box.maxy, box.maxz
    #print box.minx, box.miny, box.minz
    (width, height, depth) = utilityFunctions.getBoxSize(box)
    

    """
    center_x = width/2 + box.minx
    x = center_x-15
    y = box.miny
    z = box.minz
    
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

    road = Road_Builder(level, x, box.maxy, z, depth, height, width, 0, 0)
    road.build()


