#!/usr/bin/python
# -*- coding: UTF-8 -*-
from functions import *


class HouseWallZ_Builder:
    #House wall (directionZ)

    def __init__(self, level, start_x, start_y, start_z):
        self.level = level
        self.start_x = start_x
        self.start_y = start_y
        self.start_z = start_z

    def build(self):
        lv = self.level
        x = self.start_x
        y = self.start_y
        z = self.start_z
        for j in range(9): #line_W
            setBlock(lv, x + j, y, z, 4, 0)#rstone
            if(j==0 or j==4 or j==8):
                for k in range(1,5): #line_H
                    setBlock(lv, x + j, y + k, z, 17, 1)#black
            else:
                for k in range(1,5): #line_H
                    if k==2:
                        setBlock(lv, x + j, y + k, z, 17, 1)#black
                    else:
                        setBlock(lv, x + j, y + k, z, 12, 0)#white