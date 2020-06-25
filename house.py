#!/usr/bin/python
# -*- coding: UTF-8 -*-
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *
from roofBuilder import *

class House_Builder:

    #door is 0->front 1->back

    def __init__(self, level, start_x, start_y, start_z, door, width, direction, wall_type,tree_ID,tree_data,wood_ID,wood_data,roof_ID):
        self.level = level
        self.start_x = start_x
        self.start_y = start_y
        self.start_z = start_z
        self.door = door
        self.width = width
        self.direction = direction
        self.wall_type = wall_type
        self.tree_ID = tree_ID
        self.tree_data = tree_data
        self.wood_ID = wood_ID
        self.wood_data = wood_data
        self.roof_ID = roof_ID

    def build(self):
        lv = self.level
        x = self.start_x
        y = self.start_y
        z = self.start_z
        door = self.door
        width = self.width
        di = self.direction
        t_ID =self.tree_ID
        t_data =self.tree_data
        w_ID = self.wood_ID
        w_data = self.wood_data
        r_ID = self.roof_ID
        w = 9
        size = (width-1)/9+1 # nazeka +1 shinaito sukima ga dekite simau
        d = size*8+1


        def wallX(lv,x,y,z,door):
            if self.wall_type is 0:
                for j in range(9): #line_W
                    setBlock(lv, x, y, z + j, 4, 0)#stone
                    if(j==0 or j==3 or j==5 or j==8):
                        for k in range(1,5): #line_H
                            setBlock(lv,x,y+k,z+j,17,1)#black
                    else:
                        if(door==1):
                            if(j==4):
                                setBlock(lv,x,y,z+j,196,0)#door
                                setBlock(lv,x,y+1,z+j,196,7)#door
                            else:
                                for k in range(1,5): #line_H
                                    if k==3:
                                        setBlock(lv,x,y+k,z+j,17,1)#black
                                    else:
                                        setBlock(lv,x,y+k,z+j,12,0)#white
                            for k in range(2,5): #line_H
                                if k==2:
                                    setBlock(lv,x,y+k,z+j,17,1)#black
                                else:
                                    setBlock(lv,x,y+k,z+j,12,0)#white
                            setBlock(lv, x, y+1, z+1, 85, 0)
                            setBlock(lv, x, y+1, z+2, 85, 0)
                            setBlock(lv, x, y+1, z+6, 85, 0)
                            setBlock(lv, x, y+1, z+7, 85, 0)
                        else:
                            for k in range(1,5): #line_H
                                if k==2:
                                    setBlock(lv,x,y+k,z+j,17,1)#black
                                else:
                                    setBlock(lv,x,y+k,z+j,12,0)#white
            if self.wall_type is 1:
                for j in range(9): #line_W
                    setBlock(lv, x, y, z + j, 4, 0)#stone
                    if(j==0 or j==3 or j==5 or j==8):
                        for k in range(1,5): #line_H
                            setBlock(lv,x,y+k,z+j,t_ID,t_data)#black
                    else:
                        if(door==1):
                            if(j==4):
                                setBlock(lv,x,y,z+j,196,0)#door
                                setBlock(lv,x,y+1,z+j,196,8)#door
                            else:
                                for k in range(1,5): #line_H
                                    if k==3:
                                        setBlock(lv,x,y+k,z+j,t_ID,t_data)#black
                                    else:
                                        setBlock(lv,x,y+k,z+j,w_ID,w_data)#white
                            for k in range(2,5): #line_H
                                if k==2:
                                    setBlock(lv,x,y+k,z+j,t_ID,t_data)#black
                                else:
                                    setBlock(lv,x,y+k,z+j,w_ID,w_data)#white
                            setBlock(lv, x, y+1, z+1, 85, 0)
                            setBlock(lv, x, y+1, z+2, 85, 0)
                            setBlock(lv, x, y+1, z+6, 85, 0)
                            setBlock(lv, x, y+1, z+7, 85, 0)
                        else:
                            for k in range(1,5): #line_H
                                if k==2:
                                    setBlock(lv,x,y+k,z+j,t_ID,t_data)#black
                                else:
                                    setBlock(lv,x,y+k,z+j,w_ID,w_data)#white
            
        def wallZ(lv,x,y,z):
            if self.wall_type is 0:
                for j in range(8): #line_W
                    setBlock(lv, x + j, y, z, 4, 0)#rstone
                    if(j==0 or j==4 or j==8):
                        for k in range(1,5): #line_H
                            setBlock(lv, x + j, y + k, z, 17,1)#black
                    else:
                        for k in range(1,5): #line_H
                            if k==2:
                                setBlock(lv, x + j, y + k, z, 17,1)#black
                            else:
                                setBlock(lv, x + j, y + k, z, 12,0)#white
            
            if self.wall_type is 1:
                for j in range(9): #line_W
                    setBlock(lv, x + j, y, z, 4, 0)#rstone
                    if(j==0 or j==4 or j==8):
                        for k in range(1,5): #line_H
                            setBlock(lv, x + j, y + k, z, t_ID, t_data)#black
                    else:
                        for k in range(1,5): #line_H
                            if k==2:
                                setBlock(lv, x + j, y + k, z, t_ID, t_data)#black
                            else:
                                setBlock(lv, x + j, y + k, z, w_ID,w_data)#white

        def floor(lv,x,y,z):
            for j in range(0,7):
                for i in range(1,4):
                    setBlock(lv, x+i, y-1, z+j+1, 4, 0)
                setBlock(lv, x+4, y, z+j+1, 126, 0)
                for i in range(5,8):
                    setBlock(lv, x+i, y, z+j+1, 5, 0)
            setBlock(lv, x+7, y+1, z+1, 54, 4)
            setBlock(lv, x+7, y+1, z+2, 54, 4)
            setBlock(lv, x+7, y+1, z+7, 50, 5)
            setBlock(lv, x+1, y, z+1, 50, 5)
            setBlock(lv, x+1, y, z+7, 50, 5)
            setBlock(lv, x+3, y, z+7, 61, 2)


        for i in range(w):
            for j in range(6):
                for k in range(d):
                    setBlock(lv,x+i,y+j,z+k,0,0)

        wallZ(lv,x,y,z) #x,z
        for q in range(size):
            wallZ(lv,x,y,z+q*8+8) #x,z

            if door==0:
                wallX(lv,x,y,z+q*8,1) #x,z,door
                wallX(lv,x+8,y,z+q*8,0) #x,z,door
            elif door==1:
                wallX(lv,x,y,z+q*8,0) #x,z,door
                wallX(lv,x+8,y,z+q*8,1) #x,z,door
            floor(lv,x,y,z+q*8)

            
        roof = RoofBuilder(lv, x, z, d, y+5, di, 0, t_ID,t_data,w_ID,w_data, r_ID)
        roof.build()