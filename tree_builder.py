import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *

class Tree_Builder:

    def __init__(self, level, start_x, start_y, start_z,tree_ID,tree_data):
        self.level = level
        self.start_x = start_x
        self.start_y = start_y
        self.start_z = start_z
        self.tree_ID = tree_ID
        self.tree_data = tree_data

    def build(self):
        lv = self.level
        x = self.start_x
        y = self.start_y
        z = self.start_z
        t_ID =self.tree_ID
        t_data =self.tree_data

        tree = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [18, 18, 18, 18, 18], [18, 18, 18, 18, 18], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [18, 18, 18, 18, 18], [18, 18, 18, 18, 18], [0, 0, 18, 18, 0], [0, 0, 18, 0, 0]], [[0, 0, 17, 0, 0], [0, 0, 17, 0, 0], [0, 0, 17, 0, 0], [0, 0, 17, 0, 0], [18, 18, 17, 18, 18], [18, 18, 17, 18, 18], [0, 18, 17, 18, 0], [0, 18, 18, 18, 0]], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [18, 18, 18, 18, 18], [18, 18, 18, 18, 18], [0, 18, 18, 0, 0], [0, 0, 18, 0, 0]], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [18, 18, 18, 18, 0], [0, 18, 18, 18, 18], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]]

        for i in range(5):
            for j in range(8):
                for k in range(5):
                    if tree[i][j][k] == 18:
                        setBlock(lv,x+i,y+j,z+k,t_ID+1,t_data)
                    elif tree[i][j][k] == 17:
                        setBlock(lv,x+i,y+j,z+k,t_ID,t_data)