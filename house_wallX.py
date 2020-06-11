#!/usr/bin/python
# -*- coding: UTF-8 -*-
from functions import *


class HouseWallX_Builder:
    #House wall (directionX)
    #door is 0->NO 1->Yes

    def __init__(self, level, start_x, start_y, start_z, door):
        self.level = level
        self.start_x = start_x
        self.start_y = start_y
        self.start_z = start_z
        self.door = door

    def build(self):
        lv = self.level
        x = self.start_x
        y = self.start_y
        z = self.start_z
        d = self.door
        for j in range(10): #line_W
            setBlock(lv, x, y, z + j, 4, 0)#stone
            if(j==0 or j==3 or j==6 or j==9):
                for k in range(1,5): #line_H
                    setBlock(lv,x,y+k,z+j,17,1)#black
            else:
                if(d==1):
                    if(j==4):
                        setBlock(lv,x,y,z+j,196,0)#door
                        setBlock(lv,x,y+1,z+j,196,0)#door
                    elif(j==5):
                        setBlock(lv,x,y,z+j,196,7)#door
                        setBlock(lv,x,y+1,z+j,196,7)#door
                    else:
                        for k in range(1,5): #line_H
                            if k==2:
                                setBlock(lv,x,y+k,z+j,17,1)#black
                            else:
                                setBlock(lv,x,y+k,z+j,12,0)#white
                    for k in range(2,5): #line_H
                        if k==2:
                            setBlock(lv,x,y+k,z+j,17,1)#black
                        else:
                            setBlock(lv,x,y+k,z+j,12,0)#white
                    setBlock(lv,x-1,y+2,z+3,177,0)#flag
                    setBlock(lv,x-1,y+2,z+6,177,0)#flag
                else:
                    for k in range(1,5): #line_H
                        if k==2:
                            setBlock(lv,x,y+k,z+j,17,1)#black
                        else:
                            setBlock(lv,x,y+k,z+j,12,0)#white
         #floor
        for i in range(1,8):
            for j in range(1,9):
                setBlock(lv, x+i, y, z+j, 5, 0)#floor