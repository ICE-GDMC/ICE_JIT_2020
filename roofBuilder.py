#!/usr/bin/python
# -*- coding: UTF-8 -*-
from functions import *

# displayName = "roof"


class RoofBuilder:
    """two directions 0&1  two types(room & tower) width must be 9"""

    def __init__(self, level, start_x, start_z, depth, surface, direction, roof_type):
        self.level = level
        self.start_x = start_x
        self.start_z = start_z
        self.depth = depth
        self.surface = surface
        self.direction = direction
        self.roof_type = roof_type
        self.width = 9

    def build(self):
        lv = self.level
        x = self.start_x
        z = self.start_z
        s = self.surface
        w = self.width
        d = self.depth
        if self.roof_type is 0:  # room's roof
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
        elif self.roof_type is 1:  # tower's roof
            for i in range(0, 4):
                for j in range(x-4+i, x + d + 4-i):    # left
                    if i is 0:
                        setBlock(lv, j, s-1, z - 4 + i, 44, 13)
                    elif i is 1:
                        setBlock(lv, j, s, z - 4 + i, 44, 5)
                    elif i is 2:
                        setBlock(lv, j, s, z - 4 + i, 43, 5)
                    else:
                        setBlock(lv, j, s, z - 4 + i, 44, 13)
            for i in range(0, 4):
                for j in range(x-4+i, x + d + 4-i):  # right
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
                        setBlock(lv, x + d + 3 - i, s - 1, j, 44, 13)
                    elif i is 1:
                        setBlock(lv, x + d + 3 - i, s, j, 44, 5)
                    elif i is 2:
                        setBlock(lv, x + d + 3 - i, s, j, 43, 5)
                    else:
                        setBlock(lv, x + d + 3 - i, s, j, 44, 13)


# def perform(level, box, options):
#     (width, height, depth) = getBoxSize(box)
#     surface = box.miny
#     start_x = box.minx
#     start_z = box.minz
#     print 'width(x) = %d, depth(z) = %d' % (width, depth)
#     print 'start_x = %d, start_z = %d' % (start_x, start_z)
#     print 'surface = %d' % surface
#
#     roof_builder = RoofBuilder(level, start_x, start_z, depth, box.maxy, 0, 1)
#     roof_builder.run()
#
#     for i in range(box.minx, box.maxx):
#         for j in range(box.minz, box.maxz):
#             id = level.blockAt(i, surface, j)
#             data = level.blockDataAt(i, surface, j)
#             print "id = %d   data=%d " % (id, data)
#             setBlock(level, box.minx-1, surface, j, id, data)