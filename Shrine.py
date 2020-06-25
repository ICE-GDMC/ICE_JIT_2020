#!/usr/bin/python
# -*- coding: UTF-8 -*-
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *
from roofBuilder import *

class Shrine_Builder:

    #door is 0->front 1->back
    

    def __init__(self, level, start_x, start_y, start_z, door, direction, wall_type,tree_ID,tree_data,wood_ID,wood_data,roof_ID):
        self.level = level
        self.start_x = start_x
        self.start_y = start_y
        self.start_z = start_z
        self.door = door
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
        di = self.direction
        t_ID =self.tree_ID
        t_data =self.tree_data
        w_ID = self.wood_ID
        w_data = self.wood_data
        r_ID = self.roof_ID
        w = 9
        d = 15
        


        def wallX(lv,x,y,z,door,s):
            if self.wall_type is 0:
                for j in range(1,16): #line_W
                    if(j==1 or j==5 or j==11 or j==15):
                        for k in range(1,12): #line_H
                            setBlock(lv,x,y+k,z+j,17,1)#black
                    else:
                        if(door==1):
                            for k in range(1,12): #line_H
                                if k==5:
                                    setBlock(lv,x,y+k,z+j,17,1)#black
                                else:
                                    setBlock(lv,x,y+k,z+j,96,s)
                            for k in range(6,9): 
                                setBlock(lv,x,y+k,z+j,12,0)#white
                            for k in range(10,12):
                                setBlock(lv,x,y+k,z+j,96,s)
                            if(j==3 or j==8 or j==13):
                                setBlock(lv,x,y+2,z+j,196,0)#door
                                setBlock(lv,x,y+3,z+j,196,8)#door
                        else:
                            for k in range(1,5): #line_H
                                if k==5:
                                    setBlock(lv,x,y+k,z+j,17,1)#black
                                else:
                                    setBlock(lv,x,y+k,z+j,96,s)
                            for k in range(6,9): 
                                setBlock(lv,x,y+k,z+j,12,0)#white
                            for k in range(10,12):
                                setBlock(lv,x,y+k,z+j,96,s)
            if self.wall_type is 1:
                for j in range(1,16): #line_W
                    if(j==1 or j==5 or j==11 or j==15):
                        for k in range(1,12): #line_H
                            setBlock(lv,x,y+k,z+j,t_ID,t_data)#black
                    else:
                        if(door==1):
                            for k in range(1,12): #line_H
                                if k==5:
                                    setBlock(lv,x,y+k,z+j,t_ID,t_data)#black
                                else:
                                    setBlock(lv,x,y+k,z+j,96,s)
                            for k in range(6,9): 
                                setBlock(lv,x,y+k,z+j,w_ID,w_data)#white
                            for k in range(10,12):
                                setBlock(lv,x,y+k,z+j,96,s)
                            if(j==3 or j==8 or j==13):
                                setBlock(lv,x,y+2,z+j,196,0)#door
                                setBlock(lv,x,y+3,z+j,196,8)#door
                        else:
                            for k in range(1,5): #line_H
                                if k==5:
                                    setBlock(lv,x,y+k,z+j,t_ID,t_data)#black
                                else:
                                    setBlock(lv,x,y+k,z+j,96,s)
                            for k in range(6,9): 
                                setBlock(lv,x,y+k,z+j,w_ID,w_data)#white
                            for k in range(10,12):
                                setBlock(lv,x,y+k,z+j,96,s)
        
        def wallZ(lv,x,y,z,s):
            if self.wall_type is 0:
                for j in range(0,8): #line_W
                    setBlock(lv, x + j, y+1, z, 17, 1)#black
                    setBlock(lv, x+j, y+13, z, 17, 1)#black
                    if(j==0 or j==4 or j==8):
                        for k in range(1,13): #line_H
                            setBlock(lv, x + j, y + k, z, 17,1)#black
                    else:
                        for k in range(2,12): #line_H
                            if k==5:
                                setBlock(lv, x + j, y + k, z, 17,1)#black
                            else:
                                setBlock(lv,x+j,y+k,z,96,s)
                        for k in range(6,9): 
                            setBlock(lv,x+j,y+k,z,12,0)#white
                        for k in range(10,12):
                            setBlock(lv,x+j,y+k,z,96,s)     
            if self.wall_type is 1:
                for j in range(0,8): #line_W
                    setBlock(lv, x + j, y+1, z, t_ID,t_data)#black
                    setBlock(lv, x+j, y+13, z, t_ID,t_data)#black
                    if(j==0 or j==4 or j==8):
                        for k in range(1,14): #line_H
                            setBlock(lv, x + j, y + k, z, t_ID,t_data)#black
                    else:
                        for k in range(2,13): #line_H
                            if k==5:
                                setBlock(lv, x + j, y + k, z, t_ID,t_data)#black
                            else:
                                setBlock(lv,x+j,y+k,z,96,s)
                        for k in range(6,9): 
                            setBlock(lv,x+j,y+k,z,w_ID,w_data)#white
                        for k in range(10,13):
                            setBlock(lv,x+j,y+k,z,96,s)

        def roof(lv,x,s,z,t):
            if t==1:  # tower's roof
                for i in range(0, 4):
                    for j in range(x-4+i, x + 9 + 4-i):    # left
                        if i is 0:
                            setBlock(lv, j, s-1, z - 4 + i, 44, 13)
                        elif i is 1:
                            setBlock(lv, j, s, z - 4 + i, 44, 5)
                        elif i is 2:
                            setBlock(lv, j, s, z - 4 + i, 43, 5)
                        else:
                            setBlock(lv, j, s, z - 4 + i, 44, 13)
                for i in range(0, 4):
                    for j in range(x-4+i, x + 9 + 4-i):  # right
                        if i is 0:
                            setBlock(lv, j, s-1, z + d + 3 - i, 44, 13)
                        elif i is 1:
                            setBlock(lv, j, s, z + d + 3 - i, 44, 5)
                        elif i is 2:
                            setBlock(lv, j, s, z + d + 3 - i, 43, 5)
                        else:
                            setBlock(lv, j, s, z + d + 3 - i, 44, 13)
                for i in range(0, 4):
                    for j in range(z-4+i, z + d + 3 - i):  # under
                        if i is 0:
                            setBlock(lv, x - 4 + i, s - 1, j, 44, 13)
                        elif i is 1:
                            setBlock(lv, x - 4 + i, s, j, 44, 5)
                        elif i is 2:
                            setBlock(lv, x - 4 + i, s, j, 43, 5)
                        else:
                            setBlock(lv, x - 4 + i, s, j, 44, 13)
                for i in range(0, 4):
                    for j in range(z-4+i, z + d + 3 - i):  # under
                        if i is 0:
                            setBlock(lv, x + d + 3 - i-6, s - 1, j, 44, 13)
                        elif i is 1:
                            setBlock(lv, x + d + 3 - i-6, s, j, 44, 5)
                        elif i is 2:
                            setBlock(lv, x + d + 3 - i-6, s, j, 43, 5)
                        else:
                            setBlock(lv, x + d + 3 - i-6, s, j, 44, 13)

        def floor(lv,x,y,z):
            for j in range(17):
                for i in range(1,14):
                    setBlock(lv,x+i,y+1,z+j,126,0)
                    if j==0 or j==16:
                        setBlock(lv,x+i,y,z+j,85,0)
                        setBlock(lv,x+i,y,z+j,85,0)
                    if i==1 or i==14:
                        setBlock(lv,x+i,y,z+j,85,0)
                        setBlock(lv,x+i,y,z+j,85,0)
            for j in range(1,15):
                setBlock(lv,x+4,y+1,z+j,17,1)
                setBlock(lv,x+12,y+1,z+j,17,1)
            for i in range(4,12):
                setBlock(lv,x+i,y+1,z+15,17,1)
                setBlock(lv,x+i,y+1,z+1,17,1)
            setBlock(lv,x,y,z+7,53,0)#stears
            setBlock(lv,x,y,z+8,53,0)
            setBlock(lv,x,y,z+9,53,0)
            setBlock(lv,x+2,y+1,z+7,17,1)#saisen box
            setBlock(lv,x+2,y+1,z+8,17,1)
            setBlock(lv,x+2,y+1,z+9,17,1)
            setBlock(lv,x+2,y+2,z+7,96,0)
            setBlock(lv,x+2,y+2,z+8,96,0)
            setBlock(lv,x+2,y+2,z+9,96,0)

            
            

        wallZ(lv,x+4,y,z+1,5) #x,z
        wallZ(lv,x+4,y,z+15,5) #x,z

        if door==0:
            wallX(lv,x+4,y,z,1,7) #x,z,door
            wallX(lv,x+12,y,z,0,7) #x,z,door
        elif door==1:
            wallX(lv,x+4,y,z,0,7) #x,z,door
            wallX(lv,x+12,y,z,1,8) #x,z,door
        floor(lv,x,y,z)

        setBlock(lv,x+5,y+2,z+2,89,0)#glowStone
        setBlock(lv,x+11,y+2,z+2,89,0)#glowStone
        setBlock(lv,x+5,y+2,z+14,89,0)#glowStone
        setBlock(lv,x+11,y+2,z+14,89,0)#glowStone
        setBlock(lv,x+5,y+10,z+2,89,0)#glowStone
        setBlock(lv,x+11,y+10,z+2,89,0)#glowStone
        setBlock(lv,x+5,y+10,z+14,89,0)#glowStone
        setBlock(lv,x+11,y+10,z+14,89,0)#glowStone

        r = RoofBuilder(lv, x+4, z+1, d, y+13, di, 0, t_ID,t_data,w_ID,w_data,r_ID)
        r.build()
        roof(lv,x+4,y+8,z+1,1)