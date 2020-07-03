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
from little_house import *

displayName = "Asian Town"

inputs =(("Circular Houce", "label"),("Material", alphaMaterials.StoneBricks))

def perform(level, box, options):
    #print box.maxx, box.maxy, box.maxz
    #print box.minx, box.miny, box.minz
    (width, height, depth) = utilityFunctions.getBoxSize(box)

    t_ID,t_data,w_ID,w_data = Material_Checker(level,box.minx,box.miny,box.minz,box.maxx,box.maxy,box.maxz)

    """
    house = House_Builder(level,box.minx,70,box.minz,0,10,0,t_ID,t_data,w_ID,w_data,109)
    house.build()
    house = House_Builder(level,box.minx+10,70,box.minz,0,20,0,t_ID,t_data,w_ID,w_data,109)
    house.build()
    house = House_Builder(level,box.minx+20,70,box.minz,0,30,0,t_ID,t_data,w_ID,w_data,109)
    house.build()
    
    #store = Store_Builder(level,box.minx,70,box.minz,0,0,t_ID,t_data,w_ID,w_data,109)
    #store.build()
    """
    #town
    
    for i in range(3):
        road = Road_Builder(level,box.minx+i*34-i,100,box.minz,50,1,10,0,0)
        road.build()
        city = Cityspace(level,50,box.minx+i*34+10-i,100,box.minz,0,t_ID,t_data,w_ID,w_data,109)
        city.build()
        city = Cityspace(level,50,box.minx+i*34+24-i,100,box.minz,1,t_ID,t_data,w_ID,w_data,109)
        city.build()
    """
    s = Shrine_Builder(level,box.minx,66,box.minz,0,1,t_ID,t_data,w_ID,w_data, 109)
    s.build()
    s = Shrine_Builder(level,box.minx,66,box.minz+30,1,1,t_ID,t_data,w_ID,w_data, 109)
    s.build()

    for i in range(width):
        for j in range(height):
            for k in range(depth):
                setBlock(level,box.minx+i,box.miny+j,box.minz+k,0,0)
    

    s = Shrine_Builder(level,box.minx,70,box.minz,0,t_ID,t_data,w_ID,w_data, 109)
    s.build()
    s = Shrine_Builder(level,box.minx,70,box.minz+30,1,t_ID,t_data,w_ID,w_data, 109)
    s.build()

    l=Little_House_Builder(level,box.minx,80,box.minz,0,0,t_ID,t_data,w_ID,w_data, 109)
    l.build()
    l=Little_House_Builder(level,box.minx,80,box.minz+10,0,1,t_ID,t_data,w_ID,w_data, 109)
    l.build()
    l=Little_House_Builder(level,box.minx,80,box.minz+20,1,0,t_ID,t_data,w_ID,w_data, 109)
    l.build()
    l=Little_House_Builder(level,box.minx,80,box.minz+30,1,1,t_ID,t_data,w_ID,w_data, 109)
    l.build()
    """
    """
    for i in range(3):
        for j in range(5):
            f=field(level,box.minx+10*j,70,box.minz+i*10,1,1,i+1)
            f.build()
    """