#!/usr/bin/python
# -*- coding: UTF-8 -*-

from CalculateHeightMap import *
import numpy as np


class HeightMap:
    def __init__(self, level, start_x, start_z, end_x, end_z):
        self.level = level
        self.s_x = start_x
        self.s_z = start_z
        self.e_x = end_x
        self.e_z = end_z
        self.map = np.zeros((self.e_x - self.s_x, self.e_z - self.s_z), dtype=np.int)
        self.shape = self.map.shape
        self.calculate()
        print self.map
        print self.shape

    def calculate(self):
        for x in range(self.s_x, self.e_x):
            for z in range(self.s_z, self.e_z):
                self.map[x - self.s_x, z - self.s_z] = calculateSurfacePointHeight(self.level, x, z)

    def getHeight(self, x, z):
        index_x = x - self.s_x
        index_z = z - self.s_z
        if 0 <= index_x < self.shape[0] and 0 <= index_z < self.shape[1]:
            return self.map[x-self.s_x, z-self.s_z]
        else:
            return 128
