#!/usr/bin/python
# -*- coding: UTF-8 -*-
from functions import *


class River_Builder:
    # if road_type is 1(sand&river), depth is only 16

    def __init__(self, level, start_x, start_y, start_z, width, depth, direction):
        self.level = level
        self.start_x = start_x
        self.start_y = start_y
        self.start_z = start_z
        self.width = width
        self.direction = direction

    def build(self):
        lv = self.level
        x = self.start_x
        y = self.start_y
        z = self.start_z
        w = self.width
        d = self.depth
        if self.direction is 0: 
            for j in range(d): 
                if (j==0 or j==d):
                    for k in range(4):
                        setBlock(lv, x+j, y-k, z+i, 1, 0)
                else:
                    setBlock(lv, x+j, y-k, z+i, 0, 0)
                    for k in range(2):
                        setBlock(lv, x+j, y-1-k, z+i, 9, 0)
                    setBlock(lv, x+j, y-3, z+i, 1, 0)
        if self.direction is 1:
            for j in range(d): 
                if (j==0 or j==d):
                    for k in range(4):
                        setBlock(lv, x+i, y-k, z+j, 1, 0)
                else:
                    setBlock(lv, x+i, y-k, z+j, 0, 0)
                    for k in range(2):
                        setBlock(lv, x+i, y-1-k, z+j, 9, 0)
                    setBlock(lv, x+i, y-3, z+j, 1, 0)