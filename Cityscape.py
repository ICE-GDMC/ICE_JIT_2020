import random
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from house import *
from store import *
from field_builder import *
from MaterialChecker import *


class Cityspace:

    def __init__(self, level, road_width, start_x, start_y, start_z, door, tree_ID, tree_data, wood_ID, wood_data,roof_ID):
        self.level = level
        self.road_width = road_width
        self.start_x = start_x
        self.start_y = start_y
        self.start_z = start_z
        self.door = door
        self.tree_ID = tree_ID
        self.tree_data = tree_data
        self.wood_ID = wood_ID
        self.wood_data = wood_data
        self.roof_ID = roof_ID
            

    def build(self):
        lv = self.level
        w = self.road_width
        x = self.start_x
        y = self.start_y
        z = self.start_z
        d = self.door
        t_ID = self.tree_ID
        t_data = self.tree_data
        w_ID = self.wood_ID
        w_data = self.wood_data
        r_ID = self.roof_ID
        sw = 10
        sc = 0
        city = []
        gap = []

        for i in range(w/(sw+3)):
            if 0.5 <= random.random():
                city.append(0)
                sc += 1
                gap.append(0)

        for i in range(len(gap)):
            gap[i]=random.randint(2,5)
        
        print "SC"
        print sc
        hw = (w-sc*10-sum(gap)-1)/8*8+1
        print "HW"
        print hw
        if hw>=9:
            city.append(1)
            gap.append(random.randint(3,5))
        if w> sc*10+hw+sum(gap)+2:
            fw = w-sc*10-hw-sum(gap)
            print "FW"
            print fw
            city.append(2)
            gap.append(random.randint(3,5))

        print "gap"
        print gap
        random.shuffle(city)
        city.append(4)

        for i in range(len(city)-1):
            print "Z="
            print z
            if city[i] == 0:
                store = Store_Builder(lv,x,y,z,d,0,t_ID,t_data,w_ID,w_data,r_ID)
                store.build()
                z += sw+gap[i]
                """
                if city[i+1] == 2:
                    z += sw+1
                else:
                    z += sw+3
                """
            elif city[i] == 1:
                house = House_Builder(lv,x,y,z,d,hw,0,t_ID,t_data,w_ID,w_data,r_ID)
                house.build()
                z += hw+gap[i]
                """
                if city[i+1] == 2:
                    z += hw+1
                else:
                    z += hw+3
                """
            elif city[i] == 2:
                f = field(lv,x,y-1,z,9,fw,0)
                f.build()
                z += fw+gap[i]
                #z += fw+1
    
        print "---------------"


