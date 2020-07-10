#!/usr/bin/python
# -*- coding: UTF-8 -*-
import utilityFunctions as utilityFunctions
from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *

def Material_Checker(lv,sx,sy,sz,ex,ey,ez):
    ID = 0
    data = 0
    m = 0

    tree = [0]*6

    for i in range(sx, ex):
        for j in range(sy, ey):
            for k in range(sz, ez):
                ID = lv.blockAt(i, j, k)
                data = lv.blockDataAt(i, j, k)

                if ID==17 and data<=3:
                    tree[data]+=1
                elif ID==162 and data<=1:
                    tree[data+3]+=1
    
    for s in range(1,5):
        if tree[m] < tree[s]:
            m = s
    
    if 0<=m and m<=3:
        return 17,m,5,m
    if m<=4:
        return 162,m-4,5,m

