from numpy import *
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from roofBuilder import *
from fifth_wall import *

displayName = "test"

inputs =(("Circular Houce", "label"),("Material", alphaMaterials.StoneBricks))

def perform(level, box, options):
    print box.maxx, box.maxy, box.maxz
    print box.minx, box.miny, box.minz
    (width, height, depth) = utilityFunctions.getBoxSize(box)

        #tower create
    x = box.minx
    z = box.minz
    for i in range(5):
        d =[20, 15, 10, 5, 3]   #depth size
        y_height = [0, 5, 10, 15, 20]  #height 
        tower_wall = TowerWall(level, x + (d[0]/2-d[i]/2), box.miny+y_height[i],  z + (d[0]/2-d[i]/2), d[i])
        tower_wall.run()
        roof_builder = RoofBuilder(level, x, z, d[i], y_height[i], 0, 1)
        roof_builder.run()

   
