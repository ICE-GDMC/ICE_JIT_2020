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
        tower_wall  TowerWall(level, x + (d[0]/2-d[i]/2), box.miny+y_height[i],  z + (d[0]/2-d[i]/2), d[i])
        tower_wall.build()
        roof_builder = RoofBuilder(level, x + (d[0]/2-d[i]/2), z + (d[0]/2-d[i]/2), d[i], y+y_height[i]+4-1, 0, 1)
        roof_builder.build()
    """

    """
    center_x = width/2 + box.minx
    x = center_x - 8
    z = box.minz

    river = Road_Builder(level, x, box.maxy, z, depth, height, width, 0, 0)
    river.build()
    """

    t_ID,t_data,w_ID,w_data = Material_Checker(level,box.minx,box.miny,box.minz,box.maxx,box.maxy,box.maxz)

    #house = House_Builder(level,box.minx,70,box.minz,0,30,0,0,t_ID,t_data,w_ID,w_data)
    #house.build()
    
    #store = Store_Builder(level,box.minx,70,box.minz,0,0,0,t_ID,t_data,w_ID,w_data)
    #store.build()

    """ 
    #clean
    for i in range(-10,120):
        for k in range(height):
            for j in range(-10,60):
                setBlock(level,box.minx+i, box.miny+k, box.minz+j, 0, 0)

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
    st = Store_Builder(level,box.minx,box.miny+1,box.minz,0,0,1,t_ID,t_data,w_ID,w_data, 109)
    st.build()
    st = Store_Builder(level,box.minx,box.miny+1,box.minz+15,1,0,1,t_ID,t_data,w_ID,w_data, 109)
    st.build()
    st = Store_Builder(level,box.minx,box.miny+1,box.minz+30,0,1,1,t_ID,t_data,w_ID,w_data, 109)
    st.build()
    st = Store_Builder(level,box.minx,box.miny+1,box.minz+45,1,1,1,t_ID,t_data,w_ID,w_data, 109)
    st.build()
    h = House_Builder(level,box.minx+20,box.miny+1,box.minz,0,10,0,1,t_ID,t_data,w_ID,w_data, 109)
    h.build()
    h = House_Builder(level,box.minx+20,box.miny+1,box.minz+15,0,10,1,1,t_ID,t_data,w_ID,w_data, 109)
    h.build()
    h = House_Builder(level,box.minx+20,box.miny+1,box.minz+30,1,10,0,1,t_ID,t_data,w_ID,w_data, 109)
    h.build()
    h = House_Builder(level,box.minx+20,box.miny+1,box.minz+45,1,10,1,1,t_ID,t_data,w_ID,w_data, 109)
    h.build()

    #pagoda = Pagoda_builder(level,box.minx,70,box.minz,t_ID,t_data,w_ID,w_data,109)
    #pagoda.build()