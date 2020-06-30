from numpy import *
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from fifth_wall import *
from roofBuilder import *
from road_builder import *
from river_builder import *
from MaterialChecker import *
from shrine import *
from store import *
from house import *
from Cityscape import *
from pagoda import *
from functions import *

displayName = "Asian Town"

inputs =(("Circular Houce", "label"),("Material", alphaMaterials.StoneBricks))

def perform(level, box, options):
    #print box.maxx, box.maxy, box.maxz
    #print box.minx, box.miny, box.minz
    (width, height, depth) = utilityFunctions.getBoxSize(box)

    t_ID,t_data,w_ID,w_data = Material_Checker(level,box.minx,box.miny,box.minz,box.maxx,box.maxy,box.maxz)

    #house = House_Builder(level,box.minx,70,box.minz,0,30,0,0,t_ID,t_data,w_ID,w_data)
    #house.build()
    
    #store = Store_Builder(level,box.minx,70,box.minz,0,0,0,t_ID,t_data,w_ID,w_data)
    #store.build()

    """ 
    #town
    for i in range(3):
        road = Road_Builder(level,box.minx+i*34-i,box.miny-1,box.minz,50,1,10,0,0)
        road.build()
        city = Cityspace(level,50,box.minx+i*34+10-i,box.miny,box.minz,0,t_ID,t_data,w_ID,w_data,roof_ID)
        city.build()
        city = Cityspace(level,50,box.minx+i*34+24-i,box.miny,box.minz,1,t_ID,t_data,w_ID,w_data,roof_ID)
        city.build()

    s = Shrine_Builder(level,box.minx,66,box.minz,0,1,t_ID,t_data,w_ID,w_data, 109)
    s.build()
    s = Shrine_Builder(level,box.minx,66,box.minz+30,1,1,t_ID,t_data,w_ID,w_data, 109)
    s.build()
    """
    """
    for i in range(width):
        for j in range(height):
            for k in range(depth):
                setBlock(level,box.minx+i,box.miny+j,box.minz+k,0,0)

    for i in range(5):
        f=field(level,box.minx+10*i,box.miny,box.minz,9,9,1)
        f.build()
        f=field(level,box.minx+10*i,box.miny,box.minz+10,9,9,2)
        f.build()
        f=field(level,box.minx+10*i,box.miny,box.minz+20,9,9,3)
        f.build()
    """

    pagoda = Pagoda_builder(level,box.minx,70,box.minz,t_ID,t_data,w_ID,w_data,109)
    pagoda.build()