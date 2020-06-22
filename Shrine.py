#!/usr/bin/python
# -*- coding: UTF-8 -*-
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *


class Shrine_Builder:

    #door is 0->front 1->back

    def __init__(self, level, start_x, start_y, start_z, door, direction, wall_type,tree_ID,tree_data,wood_ID,wood_data):
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

    def build(self):
        lv = self.level
        x = self.start_x
        y = self.start_y
        z = self.start_z
        door = self.door
        t_ID =self.tree_ID
        t_data =self.tree_data
        w_ID = self.wood_ID
        w_data = self.wood_data
        w = 9
        d = 15
        


        def wallX(lv,x,y,z,door,s):
            if self.wall_type is 0:
                for j in range(1,16): #line_W
                    if(j==1 or j==5 or j==11 or j==15):
                        for k in range(1,9): #line_H
                            setBlock(lv,x,y+k,z+j,17,1)#black
                    else:
                        if(door==1):
                            for k in range(1,9): #line_H
                                if k==5:
                                    setBlock(lv,x,y+k,z+j,17,1)#black
                                else:
                                    setBlock(lv,x,y+k,z+j,96,s)
                            for k in range(6,9): 
                                setBlock(lv,x,y+k,z+j,12,0)#white
                            if(j==3 or j==8 or j==13):
                                setBlock(lv,x,y+2,z+j,196,0)#door
                                setBlock(lv,x,y+3,z+j,196,0)#door
                        else:
                            for k in range(1,5): #line_H
                                k==5:
                                    setBlock(lv,x,y+k,z+j,17,1)#black
                                else:
                                    setBlock(lv,x,y+k,z+j,96,s)
                            for k in range(6,9): 
                                setBlock(lv,x,y+k,z+j,12,0)#white
            if self.wall_type is 1:
                for j in range(10): #line_W
                    setBlock(lv, x, y, z + j, 4, 0)#stone
                    if(j==0 or j==3 or j==6 or j==9):
                        for k in range(1,6): #line_H
                            setBlock(lv,x,y+k,z+j,t_ID,t_data)#black
                    else:
                        if(door==1):
                            if(j==4):
                                setBlock(lv,x,y,z+j,196,0)#door
                                setBlock(lv,x,y+1,z+j,196,0)#door
                            elif(j==5):
                                setBlock(lv,x,y,z+j,196,7)#door
                                setBlock(lv,x,y+1,z+j,196,7)#door
                            else:
                                for k in range(1,9): #line_H
                                    if k==2:
                                        setBlock(lv,x,y+k,z+j,t_ID,t_data)#black
                                    else:
                                        setBlock(lv,x,y+k,z+j,w_ID,w_data)#red
                            for k in range(2,9): #line_H
                                if k==2:
                                    setBlock(lv,x,y+k,z+j,t_ID,t_data)#black
                                else:
                                    setBlock(lv,x,y+k,z+j,w_ID,w_data)#red
                            setBlock(lv, x, y+1, z+1, 85, 0)
                            setBlock(lv, x, y+1, z+2, 85, 0)
                            setBlock(lv, x, y+1, z+7, 85, 0)
                            setBlock(lv, x, y+1, z+8, 85, 0)
                        else:
                            for k in range(1,9): #line_H
                                if k==2:
                                    setBlock(lv,x,y+k,z+j,t_ID,t_data)#black
                                else:
                                    setBlock(lv,x,y+k,z+j,w_ID,w_data)#red
        
        def wallZ(lv,x,y,z,s):
            if self.wall_type is 0:
                for j in range(0,8): #line_W
                    setBlock(lv, x + j, y+1, z, 17, 1)#black
                    if(j==0 or j==4 or j==8):
                        for k in range(1,9): #line_H
                            setBlock(lv, x + j, y + k, z, 17,1)#black
                    else:
                        for k in range(2,9): #line_H
                            if k==5:
                                setBlock(lv, x + j, y + k, z, 17,1)#black
                            else:
                                setBlock(lv,x+j,y+k,z,96,s)
                        for k in range(6,9): 
                            setBlock(lv,x+j,y+k,z,12,0)#white
            
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

        def roof(lv,x,s,z):
            if self.direction is 0:
                for i in range(1, w / 2):
                    for j in range(i):
                        setBlock(lv, x + i, s + j, z, 43, 9)
                        setBlock(lv, x + w - i - 1, s + j, z, 43, 9)
                        setBlock(lv, x + i, s + j, z + d - 1, 43, 9)
                        setBlock(lv, x + w - i - 1, s + j, z + d - 1, 43, 9)
                for i in range(3):
                    setBlock(lv, x + w / 2, s + i, z, 17, 1)
                    setBlock(lv, x + w / 2, s + i, z + d - 1, 17, 1)  # Triangles on both sides
                for i in range(0, d + 2):
                    setBlock(lv, x - 1, s - 2, z - 1 + i, 53, 4)
                    setBlock(lv, x + w, s - 2, z - 1 + i, 53, 4)  # Wooden Stairs (Oak)

                    setBlock(lv, x - 2, s - 2, z - 1 + i, 44, 13)
                    setBlock(lv, x + w + 1, s - 2, z - 1 + i, 44, 13)  # Stone Brick Slab
                    setBlock(lv, x + w - 4, s + 3, z - 1 + i, 44, 5)
                    setBlock(lv, x + 3, s + 3, z - 1 + i, 44, 5)  # Stone Brick Slab Top

                    setBlock(lv, x + 4, s + 3, z - 1 + i, 43, 5)  # Stone Brick Slab (Double)
                    setBlock(lv, x + 4, s + 4, z - 1 + i, 139, 0)  # Cobblestone Wall

                    setBlock(lv, x + w - 3, s + 2, z - 1 + i, 109, 1)
                    setBlock(lv, x + w - 2, s + 1, z - 1 + i, 109, 1)
                    setBlock(lv, x + w - 1, s, z - 1 + i, 109, 1)
                    setBlock(lv, x + 2, s + 2, z - 1 + i, 109, 0)
                    setBlock(lv, x + 1, s + 1, z - 1 + i, 109, 0)
                    setBlock(lv, x, s, z - 1 + i, 109, 0)
                    setBlock(lv, x - 1, s - 1, z - 1 + i, 109, 0)
                    setBlock(lv, x + w, s - 1, z - 1 + i, 109, 1)  # Stone Brick Stairs
                setBlock(lv, x - 1, s - 2, z - 1, 126, 8)
                setBlock(lv, x + w, s - 2, z - 1, 126, 8)
                setBlock(lv, x - 1, s - 2, z + d, 126, 8)
                setBlock(lv, x + w, s - 2, z + d, 126, 8)  # Oak-Wood Slabs at four corners
            else:
                for i in range(1, w / 2):
                    for j in range(i):
                        setBlock(lv, x, s + j, z + i, 43, 9)
                        setBlock(lv, x, s + j, z + w - i - 1, 43, 9)
                        setBlock(lv, x + d - 1, s + j, z + i, 43, 9)
                        setBlock(lv, x + d - 1, s + j, z + w - i - 1, 43, 9)
                for i in range(3):
                    setBlock(lv, x, s + i, z + w / 2, 17, 1)
                    setBlock(lv, x + d - 1, s + i, z + w / 2, 17, 1)  # Triangles on both sides
                for i in range(0, d + 2):
                    setBlock(lv, x - 1 + i, s - 2, z - 1, 53, 4)
                    setBlock(lv, x - 1 + i, s - 2, z + w, 53, 4)  # Wooden Stairs (Oak)

                    setBlock(lv, x - 1 + i, s - 2, z - 2, 44, 13)
                    setBlock(lv, x - 1 + i, s - 2, z + w + 1, 44, 13)  # Stone Brick Slab
                    setBlock(lv, x - 1 + i, s + 3, z + w - 4, 44, 5)
                    setBlock(lv, x - 1 + i, s + 3, z + 3, 44, 5)  # Stone Brick Slab Top

                    setBlock(lv, x - 1 + i, s + 3, z + 4, 43, 5)  # Stone Brick Slab (Double)
                    setBlock(lv, x - 1 + i, s + 4, z + 4, 139, 0)  # Cobblestone Wall

                    setBlock(lv, x - 1 + i, s + 2, z + w - 3, 109, 3)
                    setBlock(lv, x - 1 + i, s + 1, z + w - 2, 109, 3)
                    setBlock(lv, x - 1 + i, s, z + w - 1, 109, 3)
                    setBlock(lv, x - 1 + i, s + 2, z + 2, 109, 2)
                    setBlock(lv, x - 1 + i, s + 1, z + 1, 109, 2)
                    setBlock(lv, x - 1 + i, s, z, 109, 2)
                    setBlock(lv, x - 1 + i, s - 1, z - 1, 109, 2)
                    setBlock(lv, x - 1 + i, s - 1, z + w, 109, 3)  # Stone Brick Stairs
                setBlock(lv, x - 1, s - 2, z - 1, 126, 8)
                setBlock(lv, x - 1, s - 2, z + w, 126, 8)
                setBlock(lv, x + d, s - 2, z - 1, 126, 8)
                setBlock(lv, x + d, s - 2, z + w, 126, 8)  # Oak-Wood Slabs at four corners
           

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
            setBlock(lv,x,y,z+7,53,0)
            setBlock(lv,x,y,z+8,53,0)
            setBlock(lv,x,y,z+9,53,0)
            
            

        wallZ(lv,x+4,y,z+1,5) #x,z
        wallZ(lv,x+4,y,z+15,5) #x,z

        if door==0:
            wallX(lv,x+4,y,z,1,7) #x,z,door
            wallX(lv,x+12,y,z,0,7) #x,z,door
        elif door==1:
            wallX(lv,x+4,y,z,0,7) #x,z,door
            wallX(lv,x+12,y,z,1,8) #x,z,door
        floor(lv,x,y,z)
        roof(lv,x+4,y+8,z+1)