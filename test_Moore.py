#!/usr/bin/python
# -*- coding: UTF-8 -*-
from functions import *
import MooreNeighborhood as M
import HeightMap as H
displayName = "Test Moore Neighbor"


def perform(level, box, options):
    (width, height, depth) = getBoxSize(box)
    surface = box.miny
    start_x = box.minx
    start_z = box.minz
    print 'width(x) = %d, depth(z) = %d' % (width, depth)
    print 'start_x = %d, start_z = %d' % (start_x, start_z)
    print 'surface = %d' % surface
    h = H.HeightMap(level, start_x, start_z, box.maxx, box.maxz)
    a = M.MooreNeighbor(h, start_x, surface, start_z, 3)
    for one in a.getResult():
        # print one
        setBlock(level, one[0], one[1], one[2], 41)


